from django.shortcuts import render
from rest_framework import viewsets
from .serializer import StudentDataserializer
from .models import StudentData


class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentDataserializer
    queryset = StudentData.objects.all()


def home(request):
    return render(request,"index.html")