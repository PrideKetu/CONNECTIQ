from django.db import models

# Create your models here.
    
    # models.py at 8001
from django.db import models

from django.db import models

class Intern(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
age = models.IntegerField(null=True, blank=True)
def __str__(self):
        return f"{self.name} ({self.department}, {self.age})"
    
    
class Report(models.Model):
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE, related_name="reports")
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to="reports/")  # stores PDF
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.intern.name}"