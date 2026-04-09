
# reporting/reports_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
  
    path("upload/", views.upload_report, name='upload_report'),
    path("<int:intern_id>/", views.report_detail, name='report_detail'),
    path('', views.report_list, name='report_list'),
]
""" path("report/", views.report, name="report"),"""