from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from app.forms import *

class cbv_form(FormView):
    template_name='cbv_form.html'
    form_class=StudentForm

    def form_valid(self, form):
        form.save()
        return HttpResponse('Data is inserted Sucessfully')
