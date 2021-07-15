from django.contrib import admin
from topic_model.models import TopicModelQuery, DetectedTopics
# Register your models here.
admin.site.register(TopicModelQuery)
admin.site.register(DetectedTopics)