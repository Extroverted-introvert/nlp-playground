from django.apps import AppConfig
from django.conf import settings as conf
import os
import gensim
from gensim import corpora, models




class TopicModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'topic_model'

    topic_model_path=os.path.join(conf.TOPIC_MODELLING_DIR, './model_20/lda.model')
    topic_model=models.LdaModel.load(topic_model_path)
    
    bigram_model_path=os.path.join(conf.TOPIC_MODELLING_DIR, './model_20/bigram.pkl')
    bigram_model=gensim.models.phrases.Phraser.load(bigram_model_path)
    dict_path=os.path.join(conf.TOPIC_MODELLING_DIR, './model_20/dictionary.pkl')
    model_dict=corpora.Dictionary.load(dict_path)
    print("Topic model loaded !!")