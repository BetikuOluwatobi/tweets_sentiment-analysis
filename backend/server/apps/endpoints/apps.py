from django.apps import AppConfig
from django.conf import settings
import os
import pickle as pk
import codecs


class EndpointsConfig(AppConfig):
    path_freq = os.path.join(settings.ARTIFACTS,'dict.pk')
    path_model = os.path.join(settings.ARTIFACTS,'logistic_regression.pk')
    path_stem = os.path.join(settings.ARTIFACTS,'stemmer.pk')
    path_token = os.path.join(settings.ARTIFACTS,'tokenizer.pk')

    freq_file = open(path_freq,'rb')
    stem_file = open(path_stem,'rb')
    token_file = open(path_token,'rb')

    word_freq = pk.load(freq_file)
    stemmer = pk.load(stem_file)
    tokenizer = pk.load(token_file)
    with open(path_model,'rb') as file:
        model = pk.load(file,encoding='latin1')