from django.shortcuts import render

def home(request):
    return render(request, 'jobs/home.html') # the homepage is in the jobs
                                            # app, because it shows all jobs
