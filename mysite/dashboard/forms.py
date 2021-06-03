from django import forms
from mentor.models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses()
        fields = "__all__"


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer()
        fields = "__all__"



class StudentForm(forms.ModelForm):
    class Meta:
        model = Students()
        fields = "__all__"



class EventForm(forms.ModelForm):
    class Meta:
        model = Events()
        fields = "__all__"
