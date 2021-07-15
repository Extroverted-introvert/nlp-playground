from django.apps import AppConfig
import tensorflow as tf
from django.conf import settings as conf

class SentimentPredictorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sentiment_predictor'

    sentiment_model=tf.keras.models.load_model(conf.SENTIMENT_MODEL_DIR)
    print("Sentiment model loaded !!")
    