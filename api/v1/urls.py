from django.urls import path

from api.v1.auth import *
from api.v1.product import *

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('crud/', CRUDView.as_view()),
    path('crud/<int:pk>/', CRUDView.as_view()),

]