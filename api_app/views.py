from django.views.generic import ListView
from .models import Songs


class HomePageView(ListView):
    template_name = 'home.html'
    model = Songs
