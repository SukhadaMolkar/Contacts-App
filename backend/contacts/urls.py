from django.urls import path
from django.conf.urls import url
from .views import ContactList,ContactDetailView
from . import views

urlpatterns = [
    path('contact/', ContactList.as_view()),
    path('<int:id>/', ContactDetailView.as_view()),
    path('new/',views.new, name="new"),
    # path('ownercontacts/', OwnerContacts.as_view() )
]