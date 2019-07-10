#Django 后台开发（前后端分离）

##django rest framework -- drf

    ###继承关系：
        GenericViewSet(viewset)   -- drf
            GenericAPIView        -- drf
                APIView           -- drf
                    View          --django
                    
                
    ###mixin:           
        CreateModelMixin
        ListModelMixin
        RetrieveModelMixin
        UpdateModelMixin
        DestroyModelMixin
