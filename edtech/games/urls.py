from django.urls import path

#Import views from current directory
from . import views

urlpatterns = [   
     path("",views.games,name="games"),
     path('signup',views.signup,name="signup"), 
     path('flashcards',views.flashcards,name="flashcards"),
     # urls.py (app) -> views.py(app)

     ]

