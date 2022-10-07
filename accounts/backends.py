import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User
#from contactsApi.contactsApi.settings import JWT_SECRET_KEY
import os
print(os.getenv("JWT_SECRET_KEY"))
import environ
env = environ.Env()
print("read",env)
# reading .env file
#environ.Env.read_env()
#print("env read")



class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        prefix,token=auth_data.decode("utf-8").split(" ")
        print("prefix,token-----",prefix,"------",token)
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)

            # payload=jwt.decode(token, os.environ.get("JWT_SECRET_KEY"))
            # #payload = jwt.decode(token, "JWT_SECRET_KEYJWT_SECRET_KEYJWT_SECRET_KEYJWT_SECRET_KEYJWT_SECRET_KEYJWT_SECRET_KEY")
            print(payload)
            user = User.objects.get(username=payload["username"])
            return (user,token)
        except jwt.DecodeError as identifier:
            print("error 1")
            raise exceptions.AuthenticationFailed("Your token is invalid,login")
        except jwt.ExpiredSignatureError as identifier:
            print("error2")
            raise exceptions.AuthenticationFailed("Your token is expired,login")

        return super().authenticate(request)

