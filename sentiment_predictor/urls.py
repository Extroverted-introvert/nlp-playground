from django.urls import path, reverse_lazy
from . import views

app_name='sentiment_predictor'
urlpatterns = [
    path('', views.SentimentListView.as_view(), name='all'),
    path('predictions/<int:pk>', views.SentimentDetailView.as_view(), name='prediction_detail'),
    path('predictions/create',
        views.SentimentCreateView.as_view(), name='prediction_create'),
    path('predictions/<int:pk>/update',
        views.SentimentUpdateView.as_view(), name='prediction_update'),
    path('predictions/<int:pk>/delete',
        views.SentimentDeleteView.as_view(success_url=reverse_lazy('sentiment_predictor:all')), name='prediction_delete'),
    ]