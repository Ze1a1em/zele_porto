from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import  reverse
from .forms import ContactForm
from .models import Contact
# Create your views here.

class HomeView(CreateView):
    form_class = ContactForm
    template_name = 'index.html'

    

    def submit_form(self, request):

        if self.request == "POST":
            form = ContactForm(request.POST)

            if form.is_valid():
                form.save(commit=True)
                return reverse('app:thanks')
            else:
                print("Erro")
        
        return render(request, 'index.html')



class FormIsSubmitedView(TemplateView):
    template_name = 'thanks.html'