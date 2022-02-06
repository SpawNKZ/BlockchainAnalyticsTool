from django.shortcuts import render
from .models import Blockchain
from etherscan import addres, balanc
# Create your views here.

def index(request):
    # data = 'Current Data'
    #
    # context = {
    #     'data': data
    # }
    #
    # return render(request, 'chartapp/index.html', context)
    for i in range(100):
        Blockchain.objects.create(address=addres[i], balance=balanc[i])
    query_results = Blockchain.objects.all()
    # query_results.delete()
    context = {'query_results': query_results}
    return render(request, 'chartapp/index.html', context)
