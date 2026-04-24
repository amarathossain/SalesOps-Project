from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_dashboard, name='dashboard'), 
    path('product-content/', views.product_content, name='product_content'),
    path('user-content/', views.user_content, name='user_content'),
    path('division-content/', views.division_content, name='division_content'),
    path('zone-content/', views.zone_content, name='zone_content'),
    path('area-content/', views.area_content, name='area_content'),
    path('route-content/', views.route_content, name='route_content'),
    path('outlet-content/', views.outlet_content, name='outlet_content'),
]