from django.urls import path
from django.conf.urls import url
from .views import ContactList,ContactDetailView

urlpatterns = [
    path('', ContactList.as_view()),
    path('<int:id>/', ContactDetailView.as_view())
]