from django.shortcuts import render
from course_app.models import Course

# Create your views here.
def home(request):
    c=Course.objects.all()
    print("""""""""""""""""")
    print(c)
    d=Course.objects.filter(title='python')
    print(d)
    return render(request, 'course_app/home.html')
