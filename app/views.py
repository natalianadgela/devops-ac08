"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from app.models import Curso, Vestibular, Inscricao
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contato',
            'message':'Natalia Nadgela - 1700653 e Kaua Ramires - 1700652',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Natalia Nadgela - 1700653 e Kaua Ramires - 1700652',
            'year':datetime.now().year,
        })
    )

def cadastro_cursos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cadastro_cursos.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de cursos',
#            'cursos': ['ADS' , 'SI', 'CC'],
            'cursos': Curso.objects.all(),
            'year':datetime.now().year,
        })
    )

def cadastro_vestibulares(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cadastro_vestibulares.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de vestibulares',
            'vestibulares': Vestibular.objects.all(),
            'year':datetime.now().year,
        })
    )   

def Inscricao_vestibulares(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Inscricao_vestibulares.html',
        context_instance = RequestContext(request,
        {
            'title':'Inscrição de vestibulares',
            'inscricoes': Inscricao.objects.all(),
            'year':datetime.now().year,
       })
    )
