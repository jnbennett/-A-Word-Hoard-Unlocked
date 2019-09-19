from django.urls import path, include 
from rest_framework import routers 
from django.views.generic import TemplateView
from . import views 

app_name = 'WordHoard'
router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet, base_name='author')
router.register(r'translators', views.TranslatorViewSet, base_name='translator')
router.register(r'texts', views.TextViewSet, base_name='text')

urlpatterns = [
	path('', TemplateView.as_view(template_name='WordHoard/index.html'), name='index'),
	path('api/', include(router.urls)),
	path('search/', views.search, name='search'),
	]