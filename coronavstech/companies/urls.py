from rest_framework import routers
from django.urls import include, path
from .views import CompanyViewSet


companies_router = routers.DefaultRouter()
companies_router.register("companies", viewset=CompanyViewSet, basename="companies")

urlpatterns = [path("", include(companies_router.urls))]
