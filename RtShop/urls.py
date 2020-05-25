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
router.register(r'codes', VerifyCodeViewSet, basename="codes")
# 配置code的url
router.register(r'users', UserViewSet, basename="users")
# 配置goods的url
router.register(r'goods', GoodsListViewSet, basename="goods")
# 配置category的url
router.register('categorys', GoodsCategoryViewSet, basename="categorys")
# 收藏url
router.register('userfavs', UserFavViewSet, basename="userfavs")
# 留言url
router.register('messages', UserLeavingMessageViewSet, basename="messages")
# 收货地址url
router.register('address', UserAddressViewSet, basename="address")
# 购物车url
router.register('shopcarts', ShoppingCartViewSet, basename="shopcarts")
# 订单相关url
router.register('orders', OrderInfoViewSet, basename="orders")
# 轮播图url
router.register('banners', BannerViewSet, basename="banners")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 配置router绑定
    url('', include(router.urls)),

    url(r'docs/', include_docs_urls(title="Rt-电商后台文档")),
    # drf 自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt 认证模式
    url(r'^login/$', obtain_jwt_token),
    # 第三方登陆url
    url('', include('social_django.urls', namespace='social'))
]

