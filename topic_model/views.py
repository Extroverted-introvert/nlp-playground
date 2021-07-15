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

from topic_model.models import TopicModelQuery
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
    model = TopicModelQuery
    template_name = "topic_model/topic_model_detail.html"


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
        return redirect(self.success_url)

    def assign_prediction(self,prediction_score):
        pred_score=prediction_score*100
        sentiment = 'Negative'
        if(pred_score>=20 and pred_score<40):
            sentimentg = 'Poor'
        elif(pred_score>=40 and pred_score<60):
            sentiment = 'Average'
        elif(pred_score>=60 and pred_score<80):
            sentiment = 'Good'
        elif(pred_score>=80):
            sentiment = 'Positive' 
        return sentiment


class TopicModelUpdateView(LoginRequiredMixin, View):
    template_name = 'topic_model/topic_model_form.html'
    success_url = reverse_lazy('topic_model:all')

    def __init__(self):
        self._sentiment_model = TopicModelConfig.sentiment_model

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
        prepared_text=np.array([self.request.POST['text']])
        query.prediction_score = np.float64(self._sentiment_model.predict(prepared_text)[0][0]).item()
        query.prediction = self.assign_prediction(query.prediction_score)
        query.save()
        return redirect(self.success_url)

    def assign_prediction(self,prediction_score):
        pred_score=prediction_score*100
        sentiment = 'Negative'
        if(pred_score>=20 and pred_score<40):
            sentimentg = 'Poor'
        elif(pred_score>=40 and pred_score<60):
            sentiment = 'Average'
        elif(pred_score>=60 and pred_score<80):
            sentiment = 'Good'
        elif(pred_score>=80):
            sentiment = 'Positive' 
        return sentiment
    


class TopicModelDeleteView(OwnerDeleteView):
    model = TopicModelQuery
    fields = '__all__'
