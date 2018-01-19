# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    index_html = "<html><body>Rango says hey there partner! <br/><br/><a href='/rango/about'><b>about rango</b></a></body></html>"
    
    return HttpResponse(index_html)

def about(request):
    about_html = "<html><body>Rango says here is the about page. <br/><br/><a href='/rango'><h1>Index</a></h1></body></html>"
    return HttpResponse(about_html)
    
