from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from .serializers import GoodsSerializer, CategorySerializer
from .models import Goods, GoodsCategory
from .filters import GoodsFilter

# Create your views here.


class GoodsPagination(PageNumberPagination):
    """
    自定义分页功能
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品列表页，分页、搜索、过滤、排序、商品详情页
    retrieve:
        商品详情
    """
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('name', 'shop_price')
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'add_time')


class GoodsCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer


