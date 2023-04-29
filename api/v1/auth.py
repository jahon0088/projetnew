from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.v1.serializer import UserSerializer
from register.models import User


class RegistrationView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, requests, *args, **kwargs):
        data = requests.data
        phone = data.get("phone")
        password = data.get("password")
        user = User.objects.filter(phone=phone).first()

        if "phone" not in data or "password" not in data:
            return Response({"Error": "Data not enough"})

        if user:
            return Response({"Error": "There is a user with this phone number ! "})

        if len(password) < 6 or len(password) > 12:
            return Response({"Error": "Not less than 6 or more than 12 items in password ! "})

        if password.islower():
            return Response({"Error": "there must be 1 capital letter in password ! "})

        if password.isnumeric():
            return Response({"Error": "There must be a letter in password ! "})

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(password)
        user.save()

        token = Token.objects.create(user=user)

        return Response({"Token": token.key})


class LoginView(GenericAPIView):
    def post(self, requests, *args, **kwargs):
        data = requests.data

        phone = data.get("phone")
        password = data.get("password")

        if "phone" not in data or "password" not in data:
            return Response({"Error": "Data not found"})

        user = User.objects.filter(phone=phone).first()

        if not user:
            return Response({"Error": "User not found"})

        if not user.check_password(password):
            return Response({'Error': "Invalid password"})

        token = Token.objects.get_or_create(user=user)[0]
        return Response({"Success": token.key})


