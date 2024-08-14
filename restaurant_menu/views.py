from django.shortcuts import render
from django.views import generic
from .models import Meal, MEAL_KINDS


class MenuList(generic.ListView):
    queryset = Meal.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["kinds"] = MEAL_KINDS
        return context


class MenuDetail(generic.DetailView):
    model = Meal
    template_name = "menu_item_detail.html"


class About(generic.ListView):
    queryset = Meal.objects.order_by("date_updated")
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
