from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import ContactForm
from .models import Contact
# Create your views here.

class HomeView(CreateView):
    form_class = ContactForm
    template_name = 'index.html'

    def submit_form(self, request):
        if self.request:
            print(form)


class FormIsSubmitedView(TemplateView):
    template_name = 'thanks.html'