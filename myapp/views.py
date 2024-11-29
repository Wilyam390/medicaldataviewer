from django.shortcuts import render
from .models import SafetyReport

def home(request):
    # Fetch all reports from the database
    reports = SafetyReport.objects.all()
    # Render the template with the data
    return render(request, 'myapp/data_table.html', {'reports': reports})
