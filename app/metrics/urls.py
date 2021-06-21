from django.urls import path
from .views import ChronicleView

urlpatterns = [
    path('<str:id>/', ChronicleView.as_view(), name="chronicle")
]
