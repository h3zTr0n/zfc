from __future__ import absolute_import

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Sponser, Post, History, Ticket
from django.views import generic
from django.utils import timezone

from .forms import TicketForm


# class BaseView(generic.ListView):
#     model = Post
#     object_list = Post.objects.all()
#     paginator = Paginator(object_list, 3)
#     template_name = 'pages/home.html'


# class BaseView(generic.ListView):
#     template_name = 'pages/home.html'
#     queryset = Sponser.objects.all()
#     # object_list = Sponser.objects.all()
#
# class SponserView(generic.ListView):
#     models = Sponser
#     object_list = Sponser.objects.all()
#     template_name =  'pages/home.html'
#
#     def get_context_data(self, **kwargs):
#        context = super(SponserView, self).get_context_data(**kwargs)
#        context['now'] = timezone.now()
#        return context
#

from .models import Sponser, Post, JuvenilePlayer, VeteranPlayer, SeniorPlayer

class BaseView(generic.ListView):
   context_object_name = 'home'
   template_name = 'pages/home.html'
   queryset = Post.objects.all()

   def get_context_data(self, **kwargs):
       context = super(BaseView, self).get_context_data(**kwargs)
       context['sponser_list'] = Sponser.objects.all()[:6]
       context['post_list'] = Post.objects.all()
    #    context['post_list'] = Post.objects.filter(published_date=timezone.now())
       context['juvenile_player'] = JuvenilePlayer.objects.all()
       context['veteran_player'] = VeteranPlayer.objects.all()
       context['senior_player'] = SeniorPlayer.objects.all()
       context['ticket'] = Ticket.objects.all()
       # And so on for more models
       return context

# def post_list(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'blog/post_list.html', {})
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def history_listing(request):
    contact_list = Contacts.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'contacts': contacts})

# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.shortcuts import render

class HistoryView(generic.TemplateView):
    context_object_name = "history"

    template_name = "pages/history.html"

    def get_context_data(self, **kwargs):
        context = super(HistoryView, self).get_context_data(**kwargs)
        context['history_list'] = History.objects.all()[:5]

        # paginator = Paginator('history_list', 25) # Show 25 contacts per page
        # page = request.GET.get('page')
        # try:
        #     history_list = paginator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     history_list = paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of results.
        #     history_list = paginator.page(paginator.num_pages)

        # return render(request, 'list.html', {'contacts': contacts})

        return context

from django.core.urlresolvers import reverse_lazy

class TicketView(generic.FormView):
    form_class = TicketForm
    template_name = "pages/ticket.html"

    def get_success_url(self, *args, **kwargs):
            return reverse_lazy('home')
