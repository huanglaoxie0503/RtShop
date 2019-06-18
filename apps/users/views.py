from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.serializers import jwt_decode_handler, jwt_payload_handler
from random import choice

from .serializers import VerifyCodeSerializer, UserRegisterSerializer
from .models import VerifyCode
from utils.send_verify_code import SendVerifyCode

from RtShop.settings import APIKEY

# Create your views here.
User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class VerifyCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    serializer_class = VerifyCodeSerializer

    def generate_code(self):
        """
        生成4位数字的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data['mobile']

        send_msg = SendVerifyCode(APIKEY)

        code = self.generate_code()
        msg_status = send_msg.send_msg(code=code, mobile=mobile)
        if msg_status["code"] != 0:
            return Response({
                "mobile": msg_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_recode = VerifyCode(code=code, mobile=mobile)
            code_recode.save()
            return Response({
                "mobile": mobile,
            }, status=status.HTTP_201_CREATED)


class UserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_decode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()




