from django.shortcuts import render
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions


class ContactList(ListCreateAPIView):
    print("here")

    serializer_class=ContactSerializer
    print("-----",serializer_class)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        print("inside perform create")
        serializer.save(owner=self.request.user)


    def get_queryset(self):
        print("get_queryset")
        return Contact.objects.filter(owner=self.request.user)


class ContactDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class=ContactSerializer
    permission_classes=(permissions.IsAuthenticated,)
    lookup_field = "id"


    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)