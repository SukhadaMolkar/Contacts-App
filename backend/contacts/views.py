from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions


class ContactList(ListCreateAPIView):

    serializer_class=ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        print("self.request.user",self.request.user)
        serializer.save(owner=self.request.user)
        name_owner=self.get_queryset()
        print(name_owner)

    def get_queryset(self):
        print("queryset",self.request)
        return Contact.objects.filter(owner=self.request.user)


class ContactDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)


def new(request):
    mem = Contact.objects.all()
    return render(request,'ContactsListView.vue',{'mem': mem})

#
# class OwnerContacts(ContactList):
#     serializer_class = ContactSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#     val=ContactList.get_queryset()
#     print(val)