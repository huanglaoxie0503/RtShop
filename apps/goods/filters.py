# -*- coding: utf-8 -*-
import django_filters
from django_filters.rest_framework import FilterSet, filters

from .models import Goods


class GoodsFilter(FilterSet):
    """
    商品过滤类
    """
    price_min = django_filters.NumberFilter(field_name='shop_price', help_text="最低价格", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'is_hot', 'is_new']



