from django.urls import path
from django.conf.urls import url
from .views import RegisterView,LoginView

urlpatterns = [
    url(r'^register', RegisterView.as_view()),
    url(r'^login', LoginView.as_view())
]