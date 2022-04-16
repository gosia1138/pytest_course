from django.core.mail import send_mail
from decouple import config

from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination


@api_view(http_method_names=["POST"])
def send_company_email(request):
    '''
        sends email with request payload
        sender: gosia.rtk@gmail.com
        receiver: gosia.rtk@gmail.com
    '''
    send_mail(
        subject=request.data.get("subject"),
        message=request.data.get("message"),
        from_email=config('FROM_EMAIL'),
        recipient_list=config('TO_EMAILS', cast=lambda v: [s.strip() for s in v.split(',')]),
        fail_silently=False,
    )
    return Response({"status": "success", "info": "email sent successfully"}, status=200)
