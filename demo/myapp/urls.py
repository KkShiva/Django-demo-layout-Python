from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("DS/", views.DS, name="DS"),
    path("BC/", views.BC, name="BC"),
    path("Bleach/", views.Bleach, name="Bleach"),
    path("FT/", views.FT, name="FT"),
    path("JJK/", views.JJK, name="JJK"),
    path("MHA/", views.MHA, name="MHA"),
    path("Naruto/", views.Naruto, name="Naruto"),
    path("OP/", views.OP, name="OP"),
]