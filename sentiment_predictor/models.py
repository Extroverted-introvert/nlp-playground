from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.conf import settings

# Create your models here.

class SentimentQuery(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Input must be greater than 2 characters")])
    text = models.TextField(
            max_length=200,
            validators=[MinLengthValidator(2, "Input must be greater than 2 characters"),
            MaxLengthValidator(250, "Input too long")]
    )
    prediction = models.CharField(max_length=128)
    prediction_score = models.DecimalField(max_digits=5, decimal_places=3)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title