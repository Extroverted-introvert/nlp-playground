from django.shortcuts import render

# Create your views here.
from django.db.models import query
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

from topic_model.models import TopicModelQuery, DetectedTopics, TopicKeyword
from topic_model.owner import OwnerListView, OwnerDetailView, OwnerDeleteView
from topic_model.forms import TopicForm

from topic_model.apps import TopicModelConfig
from topic_model.utils import Utils

import numpy as np


# Create your views here.

class TopicModelListView(OwnerListView):
    def get(self, request):
        ml = TopicModelQuery.objects.all()
        ctx = {'prediction_list': ml}
        return render(request, 'topic_model/topic_model_list.html', ctx)


class TopicModelDetailView(OwnerDetailView):
    def get(self, request, pk):
        print(request)
        qr = TopicModelQuery.objects.get(id = pk)
        tr = DetectedTopics.objects.filter(query_id = pk)

        topic_detail_list =[]
        for topic in tr:
            kr = TopicKeyword.objects.filter(topic_id = topic.id)
            topic_detail ={}
            topic_detail['topic'] = topic
            topic_detail['keywords'] = '\t'.join([ele.topic_keyword for ele in kr]) 
            topic_detail_list.append(topic_detail)
        ctx = {'qr': qr, 'tr': tr, 'topic_detail_list': topic_detail_list} 
        return render(request, 'topic_model/topic_model_detail.html', ctx)
  
            
class TopicModelCreateView(LoginRequiredMixin, View):
    template_name = 'topic_model/topic_model_form.html'
    success_url = reverse_lazy('topic_model:all')
    
    def __init__(self):
        self._utils = Utils()
        

    def get(self, request, pk=None):
        form = TopicForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = TopicForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        
        # Add owner to the model before saving
        query = form.save(commit=False)
        query.owner = self.request.user
        query.save()
        query_id = (query.id)

        index_list = self._utils.topic_modeller([self.request.POST['text']])
        print(index_list)
        status = self._utils.save_predictions(query_id, index_list)
        return redirect(self.success_url)


class TopicModelUpdateView(LoginRequiredMixin, View):
    template_name = 'topic_model/topic_model_form.html'
    success_url = reverse_lazy('topic_model:all')

    def __init__(self):
        self._utils = Utils()

    def get(self, request, pk):
        query = get_object_or_404(TopicModelQuery, id=pk, owner=self.request.user)
        form = TopicForm(instance=query)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        query = get_object_or_404(TopicModelQuery, id=pk, owner=self.request.user)
        form = TopicForm(request.POST, request.FILES or None, instance=query)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        query = form.save(commit=False)
        query.owner = self.request.user
        query.save()
        query_id = (query.id)

        index_list = self._utils.topic_modeller([self.request.POST['text']])
        print(index_list)
        status = self._utils.save_predictions(query_id, index_list)
        return redirect(self.success_url)


class TopicModelDeleteView(OwnerDeleteView):
    model = TopicModelQuery
    fields = '__all__'
