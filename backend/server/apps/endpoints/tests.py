from django.test import TestCase
from .algorithm import Logistic_Regression

# Create your tests here.
class TestModelPredictions(TestCase):

  def testPositive(self):
    input = 'I am very happy today :)'
    model = Logistic_Regression()
    pred  = model.predict_tweet(input)
    self.assertEqual('positive',pred)
  def testNegative(self):
    input = 'I am very sad today :('
    model = Logistic_Regression()
    pred  = model.predict_tweet(input)
    self.assertEqual('negative',pred)
