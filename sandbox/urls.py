from django.urls import path
from .views import (
    sandbox,
)

urlpatterns = [
    path('', sandbox, name="sandbox_home"),
    
]