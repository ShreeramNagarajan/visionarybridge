from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from .models import database
from django.urls import reverse_lazy

# CreateView to handle form submission
class LandingPageCreateView(CreateView):
    model = database
    template_name = 'landing_page.html'
    fields = ['Name', 'Email', 'Mobile_no', 'Resume']
    success_url = reverse_lazy('landing_page')  # Redirect after success

    def form_valid(self, form):
        # Add custom success message after form submission
        response = super().form_valid(form)
        messages.success(self.request, "Form submitted successfully!")
        return response

    def form_invalid(self, form):
        # Add custom error message if form is invalid
        messages.error(self.request, "Please fill in all fields!")
        return super().form_invalid(form)

# ListView to show all entries
class DatabaseListView(ListView):
    model = database
    template_name = 'database_list.html'
    context_object_name = 'entries'

# DetailView to show a single entry's details
class DatabaseDetailView(DetailView):
    model = database
    template_name = 'database_detail.html'
    context_object_name = 'entry'


