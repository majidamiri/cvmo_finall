from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveDestroyAPIView
from users.serializers import UserRegistrationSerializer, UserLoginSerializer, TokenSerializer
import string
import random
from django.contrib.auth.models import User
from kavenegar import *
from django.template import loader
from django.http import HttpResponse
import time
from django.shortcuts import redirect


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def check_login_user(request):
    if 'users_token' not in request.session:
        response = redirect('/users_registration')
        return response
    else:
        return "LOGIN"



def index(request):
    template = loader.get_template('user/main.html')
    context = {
        'latest_question_list': 'latest_question_list',
    }
    return HttpResponse(template.render(context, request))


def logout(request):
    if 'users_token' in request.session:
        del request.session['users_token']
        response = redirect('/users_registration')
        return response
    else:
        response = redirect('/users_registration')
        return response




def login_page(request):
    if 'users_token' in request.session:
        response = redirect('/profile')
        return response
    else:
        template = loader.get_template('user/login.html')
    context = {
        'latest_question_list': 'latest_question_list',
    }
    return HttpResponse(template.render(context, request))


def profile(request):

    check = check_login_user(request)
    if check != "LOGIN":
        return check

    template = loader.get_template('user/profile.html')
    context = {
        'latest_question_list': 'latest_question_list',
    }
    return HttpResponse(template.render(context, request))



class UserRegistrationAPIView(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserRegistrationSerializer

    def bad_request(self, message):
        return Response(
            data=message,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def verify_user(self, verifyCode, username):
        user = User.objects.filter(username=username, auth_code=verifyCode).first()
        if user is None:
            return self.bad_request('wrong number')
        else:
            user.is_active = True
            user.save()
            return Response(
                data='ur account is activate',
                status=status.HTTP_201_CREATED,
            )

    def resend_code(self, username):
        user = User.objects.filter(username=username).first()
        print(user.auth_code)
        if user is None or user.resend == True:
            return self.bad_request('wrong username')
        else:
            user.resend = True
            user.save()
            self.send_sms_verify(user.auth_code, user.username)
            return Response(
                data='code send again',
                status=status.HTTP_201_CREATED,
            )

    def send_sms_verify(self, auth_code, username):
        api_key = '5055694770583472596378586339304E433642643342612F6E7839686A4249326C73623243626E69644E383D'
        api = KavenegarAPI(api_key)
        params = {
            'sender': '',
            'receptor': username,
            'message': auth_code,
        }
        api.sms_send(params)

    def create(self, request, *args, **kwargs):
        if 'verify_code' in request.data:
            return self.verify_user(request.data['verify_code'], request.data['username'])
        elif 'resend_code' in request.data:
            return self.resend_code(request.data['username'])
        else:
            request.data['auth_code'] = id_generator()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            user = serializer.instance
            data = serializer.data

            self.send_sms_verify(request.data['auth_code'], request.data['username'])
            del data['auth_code']
            headers = self.get_success_headers(serializer.data)
            return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class UserLoginAPIView(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserLoginSerializer

    def existToken_expireToken(self, user_id):
        data = {}
        data['code'] = user_id
        token = Token.objects.fil
        return Response(
            data=data,
            status=status.HTTP_200_OK,
        )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.user
            #return self.existToken_expireToken(user.id)

            token, _ = Token.objects.get_or_create(user=user)
            request.session['users_token'] = token.key

            return Response(
                data=TokenSerializer(token).data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserTokenAPIView(RetrieveDestroyAPIView):

    lookup_field = "key"
    serializer_class = TokenSerializer
    queryset = Token.objects.all()

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)

    def retrieve(self, request, key, *args, **kwargs):

        if key == "current":
            instance = Token.objects.get(key=request.auth.key)
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return super(UserTokenAPIView, self).retrieve(request, key, *args, **kwargs)

    def destroy(self, request, key, *args, **kwargs):
        
        if key == "current":
            Token.objects.get(key=request.auth.key).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return super(UserTokenAPIView, self).destroy(request, key, *args, **kwargs)
