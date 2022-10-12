import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User
#from contactsApi.contactsApi.settings import JWT_SECRET_KEY
from contactsApi.settings import JWT_SECRET_KEY
#import os
#import environ
#env = environ.Env()
# reading .env file
#environ.Env.read_env()



class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        #import ipdb;ipdb.set_trace()
        jwt_options = {
            'verify_signature': False,
            'verify_exp': True,
            'verify_nbf': False,
            'verify_iat': True,
            'verify_aud': False
        }
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        prefix,token=auth_data.decode("utf-8").split(" ")


        # payload = jwt.decode(token, JWT_SECRET_KEY,algorithms='HS256',options=jwt_options)

        try:
            #payload = jwt.decode(token, JWT_SECRET_KEY,algorithms=['HS256'])
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms='HS256', options=jwt_options)

            # payload=jwt.decode(token, os.environ.get("JWT_SECRET_KEY"))
            # #payload = jwt.decode(token, "JWT_SECRET_KEYJWT_SECRET_KEYJWT_SECRET_KEYJWT_SECRET_KEYJWT_SECRET_KEYJWT_SECRET_KEY")
            user = User.objects.get(username=payload["username"])
            return (user,token)
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed("Your token is invalid,login")
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed("Your token is expired,login")

        return super().authenticate(request)

