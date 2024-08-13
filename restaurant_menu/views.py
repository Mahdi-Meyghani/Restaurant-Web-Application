from django.shortcuts import render
from django.views import generic
from .models import Meal


class MenuList(generic.ListView):
    queryset = Meal.objects.order_by("date_created")
    template_name = "index.html"


class MenuDetail(generic.DetailView):
    model = Meal
    template_name = "menu_item_detail.html"
