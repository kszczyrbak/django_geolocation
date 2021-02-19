from rest_framework import viewsets, mixins


class GeodataViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    pass
