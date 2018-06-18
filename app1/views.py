from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def hello2(request):
   text = """<h1>view 2!</h1>"""
   return HttpResponse(text)