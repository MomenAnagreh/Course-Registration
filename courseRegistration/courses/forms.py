from django import forms
from . import models

class AddCourse(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ["title", "time", "day", "instructor"]