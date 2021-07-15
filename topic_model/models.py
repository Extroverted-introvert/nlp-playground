from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.conf import settings

# Create your models here.
class TopicModelQuery(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Input must be greater than 2 characters")])
    text = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Input must be greater than 2 characters"),
            MaxLengthValidator(250, "Input too long")]
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title

class DetectedTopics(models.Model):
        prediction_id = models.ForeignKey('TopicModelQuery', models.CASCADE)
        prediction_index = models.IntegerField()
        predicted_topic = models.CharField(max_length=50)
        prediction_accuracy = models.DecimalField(max_digits=5, decimal_places=3)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
                return self.predicted_topic
