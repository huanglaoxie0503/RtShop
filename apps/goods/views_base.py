# -*- coding: utf-8 -*-
import json
from django.views.generic.base import View
from django.forms.models import model_to_dict
from django.core import serializers
from django.http import HttpResponse, JsonResponse
# from django.views.generic import ListView

from goods.models import Goods


class GoodsListView(View):
    """
    通过 Django 的 View 实现商品列表页序列化返回
    """
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()[:10]
        # 1.方法一
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)

        # 方法二
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        # json_data = json.dumps(json_list)

        # 方法三
        json_data = serializers.serialize("json", goods)
        json_data = json.loads(json_data)

        # return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(json_data, safe=False)







