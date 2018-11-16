from django.shortcuts import render
from django.http import HttpResponse

INT_MIN = -32767

# Create your views here.
def index(request):
    price=request.POST.get('price')
    price=price.split(',')
    n=request.POST.get('length')
    res=solve(price,int(n))
    return render(request,'plot/ploted.html',{"result": res, "n":n})
    
    # HttpResponse(solve(price,n))
    #render(request, 'plot/ploted.html')
    #HttpResponse(request.POST.get('payment_id', '')+"   "+request.POST.get('payment_id', ''))

def solve(price, n): 
    val = [0 for x in range(n+1)] 
    val[0] = 0
  
    # Build the table val[] in bottom up manner and return 
    # the last entry from the table 
    for i in range(1, n+1): 
        max_val = INT_MIN 
        for j in range(i): 
             max_val = max(max_val, int(price[j]) + val[i-j-1]) 
        val[i] = max_val 
  
    return val[n]
