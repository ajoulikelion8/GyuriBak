from django.shortcuts import render

import pandas as pd

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%ED%99%98%EC%9C%A8%EC%A1%B0%ED%9A%8C'
tables = pd.read_html(url)
df = tables[1]
df.columns
df=df[['매매기준율']]
exchange_list = df.values.tolist()
exchange_list = sum(exchange_list,[])

# Create your views here.
def home(request):
    return render(request,'exchangeapp/home.html')

def result(request):

    nation = list(['USD','JPY','EUR','CNY','GBP','AUD','CAD','NZD'])

    for i in range(8):
        if nation[i] in request.POST:
            name = nation[i]
            korea = request.POST['korea']
            tocountry = int(korea)
            tocountry = tocountry / exchange_list[i]
            return render(request,'exchangeapp/result.html',{'country':tocountry,'name':name,'korea':korea})

def about(request):
    return render(request,'exchangeapp/about.html')



