from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response
from django.views.generic import ListView
from .models import Proj_details, Person
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProjectSerializer
# Create your views here.

# BELOW IS FUNCTION BASED VIEW


def home(request):
  #  return HttpResponse("<h1>This is main page</h1>")
    Project = Proj_details.objects.all()
    context = {
        'project': Project,
    }
    return render(request, "home.html", context)


def details(request, id):
    obj = Proj_details.objects.get(id=id)
    people = obj.people.all()
    context = {
        'name': obj.name,
        'details': obj.details,
        'proposer': obj.proposer,
        'people': people
    }
    return render(request, "Details.html", context)


class projviewset(viewsets.ModelViewSet):
    queryset = Proj_details.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request):
        proj = Proj_details.objects.all()
        serializer = ProjectSerializer(proj, many=True)
        return Response(serializer.data)

    def retrieve(self, request, rollno):
        peeps = Person.objects.get(roll=rollno)
        proj = Proj_details.objects.filter(people=peeps)
        serializer = ProjectSerializer(proj, many=True)
        return Response(serializer.data)
