Django 后台开发（前后端分离）

```markdown
django rest framework -- drf
继承关系：
        GenericViewSet(viewset)   -- drf
            GenericAPIView        -- drf
                APIView           -- drf
                    View          --django
mixin:           
        CreateModelMixin
        ListModelMixin
        RetrieveModelMixin
        UpdateModelMixin
        DestroyModelMixin

```
-----
```markdown
增加 JWT 用户认证，pip install rest_framework_jwt
```

```markdown
drf缓存设置   pip install drf-extensions
redis缓存设置 pip install django-redis

```
