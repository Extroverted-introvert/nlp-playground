import gensim
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import nltk
nltk.download('wordnet')
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
import spacy
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use'])

from topic_model.apps import TopicModelConfig


class Utils:

    def __init__(self):
        self._stemmer = SnowballStemmer("english")
        self._model_top=TopicModelConfig.topic_model
        self._bigram_mod=TopicModelConfig.bigram_model
        self._dictionary=TopicModelConfig.model_dict
    
    def lemmatize_stemming(self, text):
        return self._stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))
    # Tokenize and lemmatize

    def remove_stopwords(self, texts):
        return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]


    def make_bigrams(self, texts,bigram_mod):
        return [bigram_mod[doc] for doc in texts]


    def lemmatization(self, nlp, texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
        """https://spacy.io/api/annotation"""
        texts_out = []
        for sent in texts:
            doc = nlp(" ".join(sent))
            texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
        return texts_out


    def sent_to_words(self, sentences):
        #print(sentences)
        yield(gensim.utils.simple_preprocess(str(sentences), deacc=True))  # deacc=True removes punctuations
        #using yield to handle large data

    def preprocess(self, text):
        sent=text.strip().split()
        sent = list(self.sent_to_words(sent))
        # Remove Stop Words
        sent = self.remove_stopwords(sent)
        # Form Bigrams
        sent = self.make_bigrams(sent,self._bigram_mod)
        # Initialize spacy 'en' model, keeping only tagger component (for efficiency)
        # python3 -m spacy download en
        nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
        # Do lemmatization keeping only noun, adj, vb, adv
        sent = self.lemmatization(nlp,sent, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
        return sent[0]

    def topic_modeller(self, input_text):
        index_list=[]
        ot = self.preprocess(input_text,bigram_mod)
        #print(ot)
        bow_vector = self._dictionary.doc2bow(ot)
        #print(bow_vector)
        for index, score in sorted(self._model_top[bow_vector], key=lambda tup: -1*tup[1]):
            #print(index, score)
            temp = self._model_top.show_topic(index, 5)
            index_list.append((index,score,[i[0] for i in temp]))
        #print(index_list)
        return index_list    