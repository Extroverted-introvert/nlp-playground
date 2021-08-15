from topic_model.models import TopicModelQuery, DetectedTopics, TopicKeyword
from django.forms import ModelForm

class TopicForm(ModelForm):
    class Meta:
        model = TopicModelQuery
        fields = ['title','text']