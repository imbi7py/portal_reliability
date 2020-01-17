from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from .models import Word
from django.db.models import Q
from django.shortcuts import render
from django.forms.models import model_to_dict

from django.http import HttpResponse
from django.template import loader

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_app.views import LoginRequiredMixin

from collections import OrderedDict  # dictionary 객체를 render 로 전달하기 위함
import pdb  # 디버깅 용
import datetime
from dateutil.relativedelta import relativedelta

def index(request):    
    label_list = ['ab','cd','de','aaa']

    context = {'label_list': label_list}
    # context = {'latest_list': latest_list}
    return render(request, 'word/index.html', context)
