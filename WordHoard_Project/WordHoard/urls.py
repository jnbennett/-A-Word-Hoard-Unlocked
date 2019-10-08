from django.urls import path, include 
from rest_framework import routers 
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from . import views 

app_name = 'WordHoard'
router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet, base_name='author')
router.register(r'translators', views.TranslatorViewSet, base_name='translator')
router.register(r'texts', views.TextViewSet, base_name='text')

urlpatterns = [
	path('', views.HomePageView.as_view(), name='index'),
	path('results/', views.SearchPageView.as_view(), name='results'),
	path('api/', include(router.urls)),
	path('search/', views.search, name='search'),
	]