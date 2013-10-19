# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
#from django.views.generic.list_detail import object_detail
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.template import Context
#from django.shortcuts import render
from django.shortcuts import render, render_to_response, get_object_or_404
from models import Page, Documento, Image, Allegato, Benefici, Caratteristiche, Galleria, Image

class HomeView(ListView):
    queryset = Page.objects.all()
    context_object_name = 'page_list'
    template_name = 'index.html'

class PaginaView(DetailView):
    queryset = Page.objects.all()
    context_object_name = 'page'
    template_name = 'pagina.html'

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super(PaginaView, self).get_context_data(**kwargs)
        context['caratteristiche_list'] = Caratteristiche.objects.filter(pagina=context['page'].id)[:1]
        context['galleria_list'] = Galleria.objects.filter(pagina=context['page'].id)[:3]
        context['benefici_list'] = Benefici.objects.filter(pagina=context['page'].id)[:1]
        return context
