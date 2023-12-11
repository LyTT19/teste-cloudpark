from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Customer, Vehicle, Plan, CustomerPlan, Contract, ContractRule, ParkMovement

class homeView(ListView):
    model = ParkMovement
    template_name = "cloudPark/home.html"
    context_object_name = "parkmovements"


