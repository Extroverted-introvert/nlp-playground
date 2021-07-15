from sentiment_predictor.models import SentimentQuery
from django.forms import ModelForm

class SentimentForm(ModelForm):
    class Meta:
        model = SentimentQuery
        fields = ['title','text']