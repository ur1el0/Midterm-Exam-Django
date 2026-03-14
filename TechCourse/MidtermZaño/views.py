from django.shortcuts import render
from .models import Assignment, Professor, Course

# Create your views here.

def index(request):
    professors = Professor.objects.all()
    return render(request, 'index.html', {'professors': professors})

def details(request, professor_id):
    professor = Professor.objects.get(profesorID=professor_id)
    courses = Course.objects.filter(professor=professor)
    assignments = Assignment.objects.filter(professor=professor)
    total = sum(a.totalAmount for a in assignments)
    return render(request, 'details.html', {
        'professor': professor, 
        'courses': courses, 
        'assignments': assignments, 
        'total': total
    })