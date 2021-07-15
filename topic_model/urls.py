from django.urls import path, reverse_lazy
from . import views

app_name='topic_model'
urlpatterns = [
    path('', views.TopicModelListView.as_view(), name='all'),
    path('predictions/<int:pk>', views.TopicModelDetailView.as_view(), name='prediction_detail'),
    path('predictions/create',
        views.TopicModelCreateView.as_view(), name='prediction_create'),
    path('predictions/<int:pk>/update',
        views.TopicModelUpdateView.as_view(), name='prediction_update'),
    path('predictions/<int:pk>/delete',
        views.TopicModelDeleteView.as_view(success_url=reverse_lazy('topic_model:all')), name='prediction_delete'),
    ]