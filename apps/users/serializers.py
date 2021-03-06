# -*- coding: utf-8 -*-
import re
from datetime import datetime, timedelta
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

from RtShop.settings import REGEX_MOBILE
from .models import VerifyCode

# Create your views here.
User = get_user_model()


class VerifyCodeSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField(max_length=11)

    class Meta:
        model = VerifyCode
        fields = ('mobile', )

    def validate_mobile(self, mobile):
        """
        验证手机号码
        """
        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")
        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")
        # 验证码发送频率
        one_minutes_age = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minutes_age, mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    class Meta:
        model = User
        fields = ("name", "gender", "birthday", "email", "mobile")


class UserRegisterSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, max_length=4, min_length=4, help_text="验证码", label="验证码",
                                 write_only=True,
                                 error_messages={"blank": "请输入验证码",
                                                 "required": "请输入验证码",
                                                 "max_length": "验证码格式错误",
                                                 "min_length": "验证码格式错误"}
                                 )
    username = serializers.CharField(required=True, allow_blank=False, label="用户名",
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")]
                                     )
    password = serializers.CharField(
        style={'input_type': 'password'}, label="密码", write_only=True
    )

    # def create(self, validated_data):
    #     user = super(UserRegisterSerializer, self).create(validated_data=validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user

    def validate_code(self, code):
        """
        验证验证码是否可用
        :param code:
        :return:
        """
        # initial_data: 前端传过来的值
        # try:
        #     verify_records = VerifyCode.objects.get(mobile=self.initial_data['username'], code=code)
        # except VerifyCode.DoesNotExist as e:
        #     pass
        # except VerifyCode.MultipleObjectsReturned as e:
        #     pass
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data['username']).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]

            five_minutes_age = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_minutes_age > last_record.add_time:
                raise serializers.ValidationError("验证码过期")

            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")
            else:
                raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        attrs["mobile"] = attrs["mobile"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "code", "mobile", "password")
