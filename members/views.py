from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from members.models import Member

# Create your views here.
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def members(request):
    members = Member.objects.all().values()
    template = loader.get_template('members.html')
    context = {
        'members': members
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'member': member
    }
    return HttpResponse(template.render(context, request))

# For testing purposes
def testing(request):
  template = loader.get_template('test_template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))