
# reporting/reports_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
  
    path('reports/', views.report_list, name='report_list'),
    path('interns/', views.interns),
    path('upload/', views.upload_report, name='upload_report'),
]
