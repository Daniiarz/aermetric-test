from django.urls import path
from .views import ChronicleView

urlpatterns = [
    path('/<uuid:id>/', ChronicleView.as_view(), name="chronicle")
]