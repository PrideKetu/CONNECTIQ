from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import Intern, Report
import json

@csrf_exempt
def interns(request):
    if request.method == "GET":
        data = list(Intern.objects.values())
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        body = json.loads(request.body)
        intern = Intern.objects.create(
            name=body.get("name"),
            department=body.get("department"),
        )
        return JsonResponse({
            "id": intern.id,
            "message": "Intern created"
        })
# GET all reports
@csrf_exempt
def report_list(request):
    if request.method == "GET":
        reports = Report.objects.all()

        data = [
            {
                "id": r.id,
                "title": r.title,
                "intern": r.intern.name,
                "department": r.intern.department,
                "file": r.pdf_file.url if r.pdf_file else None,
                "uploaded_at": r.uploaded_at
            }
            for r in reports
        ]

        return JsonResponse(data, safe=False)
# POST new report
@csrf_exempt
def upload_report(request):
    if request.method == "POST":
        title = request.POST.get("title")
        intern_id = request.POST.get("intern")
        file = request.FILES.get("pdf_file")

        if not title or not intern_id:
            return JsonResponse({"error": "Missing fields"}, status=400)

        intern = Intern.objects.get(id=intern_id)

        report = Report.objects.create(
            title=title,
            intern=intern,
            pdf_file=file
        )

        return JsonResponse({
            "id": report.id,
            "message": "Uploaded successfully"
        })

    return JsonResponse({"error": "Only POST allowed"}, status=405)