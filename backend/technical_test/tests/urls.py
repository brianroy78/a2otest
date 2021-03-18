from django.urls import path

from . import views

urlpatterns = [
    path('paper_league', views.solve_paper_league_controller),
    path('chess', views.solve_chess_controller),
    path('string_value', views.solve_string_value_controller)
]
