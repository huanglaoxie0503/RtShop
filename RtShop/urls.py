"""RtShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import url, include
from django.urls import path
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from RtShop.settings import MEDIA_ROOT
from users.views import VerifyCodeViewSet, UserViewSet
from goods.views import GoodsListViewSet, GoodsCategoryViewSet, BannerViewSet
from trade.views import ShoppingCartViewSet, OrderInfoViewSet
from user_operation.views import UserFavViewSet, UserLeavingMessageViewSet, UserAddressViewSet

router = DefaultRouter()

# 配置code的url
router.register(r'codes', VerifyCodeViewSet, base_name="codes")
# 配置code的url
router.register(r'users', UserViewSet, base_name="users")
# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name="goods")
# 配置category的url
router.register('category', GoodsCategoryViewSet, base_name="category")
# 收藏url
router.register('userfavs', UserFavViewSet, base_name="userfavs")
# 留言url
router.register('message', UserLeavingMessageViewSet, base_name="message")
# 收货地址url
router.register('address', UserAddressViewSet, base_name="address")
# 购物车url
router.register('shopcarts', ShoppingCartViewSet, base_name="shopcarts")
# 订单相关url
router.register('orders', OrderInfoViewSet, base_name="orders")
# 轮播图url
router.register('banners', BannerViewSet, base_name="banners")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 商品列表页
    url('', include(router.urls)),

    url(r'docs/', include_docs_urls(title="Rt-电商后台文档")),
    # drf 自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt 认证模式
    url(r'^login/', obtain_jwt_token),

]

