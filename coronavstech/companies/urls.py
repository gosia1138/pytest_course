from rest_framework import routers
from django.urls import include, path
from . import views


companies_router = routers.DefaultRouter()
companies_router.register("companies", viewset=views.CompanyViewSet, basename="companies")

urlpatterns = [
    path("", include(companies_router.urls)),
    path('send-email', views.send_company_email, name='send-email'),
]
