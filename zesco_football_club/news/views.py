from __future__ import absolute_import

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
from django.views import generic
from django.utils import timezone
# class BaseView(generic.ListView):
#     model = Post
#     object_list = Post.objects.all()
#     paginator = Paginator(object_list, 3)
#     template_name = 'pages/home.html'
 

class BaseView(generic.ListView):
    model = Post
    template_name = 'pages/home.html'


class Homev2(generic.TemplateView):
    template_name = "home2.html"

class Homev3(generic.TemplateView):
    template_name = "home3.html"

class Homev4(generic.TemplateView):
    template_name = "home4.html"

class Homev5(generic.TemplateView):
    template_name = "home5.html"

class Homev7(generic.TemplateView):
    template_name = "home7.html"

class Homev8(generic.TemplateView):
    template_name = "home8.html"

class NewsDetailView(generic.DetailView):
    model = Post
    template_name = 'pages/home.html'
# class Sponsors(generic.DetailView):

#
# class OurSPonsors(generic.ListView):
#     model = Sponsers
#     template_name = 'pages/home.html'
