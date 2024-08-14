"""
URL configuration for gym project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views 
from accounts.views import LogoutAPIView
from management.views import (
    MemberListCreateView,
    MemberRetrieveUpdateDestroyView,
    MemberEntryListCreateView,
    MemberEntryRetrieveUpdateDestroyView,
    TrainerListCreateView,
    TrainerRetrieveUpdateDestroyView,
    GymClassListCreateView,
    GymClassRetrieveUpdateDestroyView,
    PaymentListCreateView,
    PaymentRetrieveUpdateDestroyView
)

router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name ='login'), 
    path('api/logout/', LogoutAPIView.as_view(), name='logout'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('api/', include(router.urls)),
    path('api/members/', MemberListCreateView.as_view(), name='member-list-create'),
    path('api/members/<int:pk>/', MemberRetrieveUpdateDestroyView.as_view(), name='member-retrieve-update-destroy'),
    
    path('api/member-entries/', MemberEntryListCreateView.as_view(), name='member-entry-list-create'),
    path('api/member-entries/<int:pk>/', MemberEntryRetrieveUpdateDestroyView.as_view(), name='member-entry-retrieve-update-destroy'),
    
    path('api/trainers/', TrainerListCreateView.as_view(), name='trainer-list-create'),
    path('api/trainers/<int:pk>/', TrainerRetrieveUpdateDestroyView.as_view(), name='trainer-retrieve-update-destroy'),
    
    path('api/gym-classes/', GymClassListCreateView.as_view(), name='gym-class-list-create'),
    path('api/gym-classes/<int:pk>/', GymClassRetrieveUpdateDestroyView.as_view(), name='gym-class-retrieve-update-destroy'),
    
    path('api/payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('api/payments/<int:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name='payment-retrieve-update-destroy'),
]