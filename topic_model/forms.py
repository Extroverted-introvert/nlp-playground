from topic_model.models import TopicModelQuery
from django.forms import ModelForm

class TopicForm(ModelForm):
    class Meta:
        model = TopicModelQuery
        fields = ['title','text']