from django.shortcuts import render
# this gets the jobs from the database and turns them into objects:
from .models import Job


# the homepage is in the jobs app, because it shows all jobs
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
    
