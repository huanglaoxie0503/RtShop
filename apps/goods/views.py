from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GoodsSerializer

from .models import Goods

# Create your views here.


class GoodsListView(APIView):
    """
    List all goods, or create a new goods.
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)
