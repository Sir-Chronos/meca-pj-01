from django.urls import path
from api.views.Log import LogView

urlpatterns = [
    path('', LogView.as_view()),
]
