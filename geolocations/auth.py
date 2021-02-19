from rest_framework import generics
from .serializers import RegisterSerializer
from .responses import model_created_response


class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return model_created_response(self.get_serializer(user).data)
