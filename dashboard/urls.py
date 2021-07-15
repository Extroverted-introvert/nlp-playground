from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.static import serve
from django.views.generic import TemplateView

from . import views
app_name = 'dashboard'
urlpatterns = [
    path('', views.MainView.as_view(), name='dashboard'),
    # path('predictSentiment', views.Sentiment_Analyser.as_view(), name="predict_sentiment"),
    # path('topic_model', dashboard_views.topic_model, name="topic_model"),
    # path('sentiment', dashboard_views.sentiment, name="sentiment"),
    # path('predict_topic', dashboard_views.predict_topic, name="predict_topic"),
    # path('custom_topic', dashboard_views.custom_topic_model, name="custom_topic_model"),
    # path('predict_custom', dashboard_views.predict_custom_topic, name="predict_custom_topic"),
    # path('predict_reverse_translation', dashboard_views.predict_reverse_translation, name="predict_reverse_translation"),
    # path('reverse_translation', dashboard_views.reverse_translation, name="reverse_translation"),
    # path('predict_translation', dashboard_views.predict_translation, name="predict_translation"),
    # path('translation', dashboard_views.translation, name="translation"),
    # path('predict_answer', dashboard_views.predict_answer, name="predict_answer"),
    # path('question_answering', dashboard_views.question_answering, name="question_answering"),
    
]