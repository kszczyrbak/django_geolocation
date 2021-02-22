from rest_framework import viewsets, mixins, status
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Geolocation
from .serializers import GeolocationSerializer, GeolocationPostSerializer
from .responses import model_created_response, bad_request_response, model_already_exists_response, server_error_response, external_api_error_response
from .services import IpstackService, JsonAttributeParser
from django.db import IntegrityError, Error
from rest_framework.response import Response
from .constants import IPV4_IPV6_OR_URL_REGEX
from rest_framework.permissions import IsAuthenticated
from requests.exceptions import ConnectionError, HTTPError
from django.db.models import Q
from rest_framework_simplejwt.authentication import JWTAuthentication
from .exceptions import HostNotFoundError


class GeolocationViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    lookup_field = 'hostname'
    lookup_value_regex = IPV4_IPV6_OR_URL_REGEX
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return GeolocationPostSerializer
        return GeolocationSerializer

    def get_object_by_hostname_or_ip(self, hostname):
        geolocation = Geolocation.objects.filter(
            Q(hostname=hostname) | Q(ip=hostname)).first()
        if geolocation:
            return geolocation

        raise Http404

    def retrieve(self, request, hostname=None):
        geolocation = self.get_object_by_hostname_or_ip(hostname)
        serializer = GeolocationSerializer(geolocation)
        return Response(serializer.data)

    def destroy(self, request, hostname=None):
        geolocation = self.get_object_by_hostname_or_ip(hostname)
        geolocation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request):

        geolocation_post_serializer = GeolocationPostSerializer(
            data=request.data)
        if not geolocation_post_serializer.is_valid():
            return bad_request_response(geolocation_post_serializer.errors)

        data = geolocation_post_serializer.validated_data
        hostname = data['hostname']

        try:
            ipstack_response = IpstackService.get_geodata_for_host(hostname)
        except HostNotFoundError:
            return bad_request_response(data, "Provided hostname not found in ipstack response")
        except ConnectionError:
            return external_api_error_response(data)
        except HTTPError:
            return server_error_response(data)

        JsonAttributeParser.add_attributes(
            ipstack_response,
            country=ipstack_response['country_name'],
            continent=ipstack_response['continent_name'],
            region=ipstack_response['region_name'],
            hostname=hostname)

        geolocation_serializer = GeolocationSerializer(
            data=ipstack_response,
        )

        if not geolocation_serializer.is_valid():
            return bad_request_response(data=data, errors=geolocation_serializer.errors)

        try:
            geolocation = geolocation_serializer.save()
        except Error:
            return server_error_response(data)

        return model_created_response(GeolocationSerializer(geolocation).data)
