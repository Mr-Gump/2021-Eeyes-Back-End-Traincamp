
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from first import views
from django.conf.urls import include

router = DefaultRouter()
router.register(r'articles', views.ArticleAPIViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
