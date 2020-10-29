from .forms import PredictForm
from .algorithm import Logistic_Regression
from rest_framework.views import APIView
from django.http import JsonResponse

#Create your views here.
class PredictView(APIView):
  def get(self,request):
    if request.method == 'GET':
      #get the input data
      text = request.GET.get('text')
      #instantiate model
      model = Logistic_Regression()
      #get predictions
      result = model.predict_tweet(tweet=text)
      #return pred
      response = {'text_sentiment':result}
      return JsonResponse(response)