from django.urls import path

from . import views

urlpatterns = [
    path('paper_league', views.solve_paper_league),
    path('chess', views.solve_chess),
    path('string_value', views.solve_string_value)
]
