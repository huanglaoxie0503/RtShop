# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserFav, UserLeavingMessage, UserAddress
from goods.serializers import GoodsSerializer


class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ("goods", "id")


class UserFavSerializer(serializers.ModelSerializer):
    # 获取当前用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="该商品已经收藏!",
            )
        ]
        fields = ("user", "goods", "id")


class UserLeavingMessageSerializer(serializers.ModelSerializer):
    # 获取当前用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = UserLeavingMessage
        fields = ("user", "message_type", "subject", "message", "file", "id", "add_time")


class UserAddressSerializer(serializers.ModelSerializer):
    # 获取当前用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = UserAddress
        fields = ("user", "province", "city", "district", "address", "signer_name", "signer_mobile", "id", "add_time")
