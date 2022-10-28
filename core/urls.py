from django.urls import path
from core.views import *

urlpatterns = [
    path('emails/',       EmailsAPIView.as_view(),          name="core_emails"),
]