from django.shortcuts import render, redirect
from .models import Course
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required(login_url="/")
def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {"courses": courses})


@login_required(login_url="/")
def course_add(request):
    if request.method == 'POST':
        form = forms.AddCourse(request.POST, request.FILES)
        if form.is_valid():
            # save course to db
            instance = form.save(commit=False)
            instance.student = request.user
            instance.save()
            return redirect('courses:list')
    else:
        form = forms.AddCourse()
    return render(request, 'courses/course_add.html', {'form': form})