from django.contrib import admin
from topic_model.models import TopicKeyword, TopicModelQuery, DetectedTopics
# Register your models here.
admin.site.register(TopicModelQuery)
admin.site.register(DetectedTopics)
admin.site.register(TopicKeyword)