from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Intern, Report
import json

def report_list(request):
    data = [
        {"id": 1, "name": "Report 1"},
        {"id": 2, "name": "Report 2"},
    ]
    return JsonResponse(data, safe=False)

def report_detail(request, intern_id):
    # Dummy example
    data = {"id": intern_id, "name": f"Report {intern_id}"}
    return JsonResponse(data)

# List reports of an intern
def list_reports(request, intern_id):
    reports = Report.objects.filter(intern_id=intern_id)
    data = [{"id": r.id, "title": r.title, "uploaded_at": r.uploaded_at.isoformat()} for r in reports]
    return JsonResponse(data, safe=False)

# Upload report
@csrf_exempt
def upload_report(request):
    if request.method == "POST":
        intern_id = request.POST.get("intern_id")
        title = request.POST.get("title")
        pdf_file = request.FILES.get("pdf_file")
        report = Report.objects.create(intern_id=intern_id, title=title, pdf_file=pdf_file)
        return JsonResponse({"status": "success", "report_id": report.id})
    return JsonResponse({"error": "POST method required"}, status=400)

"""
    # views.py at 8001
from django.http import JsonResponse
from .models import Report
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Intern, Report

@csrf_exempt
def upload_report(request):
    if request.method == "POST":
        intern_id = request.POST.get("intern_id")
        title = request.POST.get("title")
        pdf_file = request.FILES.get("pdf_file")

        try:
            intern = Intern.objects.get(id=intern_id)
        except Intern.DoesNotExist:
            return JsonResponse({"error": "Intern not found"}, status=404)

        report = Report.objects.create(intern=intern, title=title, pdf_file=pdf_file)
        return JsonResponse({"message": f"Report uploaded by {intern.name}", "report_id": report.id})

def list_reports(request, intern_id):
    try:
        intern = Intern.objects.get(id=intern_id)
    except Intern.DoesNotExist:
        return JsonResponse({"error": "Intern not found"}, status=404)

    reports = intern.reports.all()
    data = [{"title": r.title, "file": r.pdf_file.url, "uploaded_at": r.uploaded_at} for r in reports]

    return JsonResponse({
        "intern": intern.name,
        "total_reports": len(data),
        "reports": data
    })


# Create your views here.

def report(request):
    return JsonResponse({
    "report": "connection initialized",
    "time": str(datetime.datetime.now())
})

# reporting_app/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_report(request):
    body = json.loads(request.body) if request.body else {}
    return JsonResponse({
        "status": "success",
        "message": "Report created in dummy system",
        "data_received": body
    })"""