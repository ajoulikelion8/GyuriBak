
지금까지 배운 내용과 새로운 내용을 바탕으로 환율계산 페이지 실습을 하겠습니다. 실습의 전제는 Classlion의 wordcount를 들은 것입니다!

##### 배운내용 활용

1. html, css를 작성할 수 있다.
2. html,view,url의 관계를 이해한다.
3. return render를 사용한다.
4. html과 css를 연동한다.

##### 새로운 내용

1. request.GET과 request.POST 에 대해서 이해한다.
2. 템플릿 변수를 사용한다.
3. Bootstrap을 사용해본다.

##### 실습과 관련해서 더 멋지게 코딩하기 위해 나중에 배울 내용

1. Django form에 대해서 익힌다.
2. 모든 페이지에서 공통되는 html을 관리하는 html을 만든다.
3. 폰트를 바꿔본다.



우선 오늘의 목표 페이지에 대해서 설명하겠습니다.

![image](https://user-images.githubusercontent.com/42667951/79073340-f620ed80-7d20-11ea-8be1-72cbd2937605.png)



![image](https://user-images.githubusercontent.com/42667951/79073360-1650ac80-7d21-11ea-832c-45f958b2b569.png)

짜잔~ 기능설명부터!

1. home 페이지에 한국 돈을 입력받는 칸을 만든다. ( 그 칸은 숫자만 입력 가능 )
2. home 페이지에 각 나라별 버튼을 만든다.
3. 나라별 버튼을 누르면 result 페이지에서 내가 입력한 숫자와 버튼 누른 나라, 환전 결과가 나오게 한다.
4. 다시 home으로 돌아갈 수 있는 버튼을 result 페이지에 만든다.



### 1. 기본 환경 설정

이 부분은 저번 주에 한부분이니 간단하게 설명만 하고 넘어가겠습니다.

1. 가상환경, 프로젝트, 앱 만들기

   ```bash
   $ python -m venv myvenv
   $ source myvenv/Scripts/activate
   $ pip install django
   $ django-admin startproject exchangeproject
   $ cd exchangeproject
   $ python manage.py startapp exchangeapp
   ```

2. settings.py에 앱 만들었다고 알리기

   ```python
   'exchangeapp.apps.ExchangeappConfig',
   ```

3. 앱 안에 templates폴더/앱이름폴더/html 파일 만들기 - home.html, result.html, about.html

   

### # 난이도 하 버전

[난이도 하 버전!] :  

난이도 하버전은 wordcount와 난이도가 아주그냥 똑같습니다. 복습한다고 생각하면 돼요.

1. 나라별로 form 태그 만든다.
2. views.py에 함수도 따로 만든다.
3. 환율 정보도 실시간으로 가져오는거 아니다.

![image](https://user-images.githubusercontent.com/42667951/79127161-588af400-7ddc-11ea-91dd-d255d4f781d9.png)

![image](https://user-images.githubusercontent.com/42667951/79127337-b15a8c80-7ddc-11ea-8246-46c654401ff6.png)
![image](https://user-images.githubusercontent.com/42667951/79127370-bf101200-7ddc-11ea-9f70-9a6e16fcfdda.png)
![image](https://user-images.githubusercontent.com/42667951/79127410-ce8f5b00-7ddc-11ea-8d98-ae2aa13996e2.png) 

```html
<!-- home.html -->
<h1>환율페이지입니다.</h1>

<h3>달러 환전.</h3>
<form action = "{% url 'usd' %}" method=POST>
    {% csrf_token %}
    <input type=number placeholder="한국 돈을 입력하세요." name="korea">
    <br>
    <button type=submit >미국</button>
</form>

<br>

<h3>옌 환전.</h3>
<form action = "{% url 'jpy' %}" method=POST>
    {% csrf_token %}
    <input type=number placeholder="한국 돈을 입력하세요." name="korea">
    <br>
    <button type=submit >일본</button>
</form>

<br>

<h3>캐나다 돈 환전.</h3>
<form action = "{% url 'can' %}" method=POST>
    {% csrf_token %}
    <input type=number placeholder="한국 돈을 입력하세요." name="korea">
    <br>
    <button type=submit >캐나다</button>
</form>
```

```html
<!-- usd.html -->
<h1>미국 환전 결과페이지입니다.</h1>

<h3>입력한 한국 돈</h3>
{{korea}}

<h3>미국 환전 결과</h3>
{{usd}}

<br>
<a href="{% url 'home' %}">home</a>
```

```html
<!-- jpy.html -->
<h1>일본 환전 결과페이지입니다.</h1>

<h3>입력한 한국 돈</h3>
{{korea}}

<h3>일본 환전 결과</h3>
{{jpy}}

<br>
<a href="{% url 'home' %}">home</a>
```

```html
<!-- can.html -->
<h1>캐나다 환전 결과페이지입니다.</h1>

<h3>입력한 한국 돈</h3>
{{korea}}

<h3>캐나다 환전 결과</h3>
{{can}}

<br>
<a href="{% url 'home' %}">home</a>
```

```python
#views.py
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'exchangeapp/home.html')

def usd(request):
    korea = request.POST['korea']
    korea = int(korea)
    usd = korea/1217.50
    return render(request,'exchangeapp/usd.html',{'korea':korea,'usd':usd})

def jpy(request):
    korea = request.POST['korea']
    korea = int(korea)
    jpy = korea/1127.26*100
    return render(request,'exchangeapp/jpy.html',{'korea':korea,'jpy':jpy})

def can(request):
    korea = request.POST['korea']
    korea = int(korea)
    can = korea/871.70
    return render(request,'exchangeapp/can.html',{'korea':korea,'can':can})
```

```python
#urls.py
from django.contrib import admin
from django.urls import path
import exchangeapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',exchangeapp.views.home,name='home'),
    path('usd/',exchangeapp.views.usd,name='usd'),
    path('jpy/',exchangeapp.views.jpy,name='jpy'),
    path('can/',exchangeapp.views.can,name='can')
]
```



### #난이도 상 버전

### 2. urls.py

수업의 진행 흐름상 url을 먼저 채우고 갑시다. 이건 저번에 배운거니깐 넘어갑시다

```python
from django.contrib import admin
from django.urls import path
import exchangeapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',exchangeapp.views.home, name='home'),
    path('result/',exchangeapp.views.result,name='result'),
    path('about/',exchangeapp.views.about,name='about')
]


```



### 3. home.html 

우선 home.html에는 환율페이지 제목, 한국 돈을 입력할 칸, 나라별 결과를 보여줄 버튼을 만들어야 겠죠?  이쁜거 생각 안하고 필요한 것만 적어봅시다.

```html
<head>
    <meta charset="UTF-8">
</head>

<h1>환율페이지입니다.</h1>

<form action="{% url 'result' %}" method="post" >
    {% csrf_token %}
    <div class="form-group">
        원화 환전
        <input type="number" placeholder="숫자를 입력하시오" name='korea'>
        환전하고 싶은 한국 돈을 숫자로 입력하세요.
    </div>
    <br>
    <div class="buttoncollector">
        <button type="submit" name="USD">미국</button>
        <button type="submit" name="JPY">일본</button>
        <button type="submit" name="EUR">유럽연합</button>
        <button type="submit" name="CNY">중국</button>
        <button type="submit" name="GBP">영국</button>
        <button type="submit" name="AUD">호주</button>
        <button type="submit" name="CAD">캐나다</button>
        <button type="submit" name="NZD">뉴질랜드</button>
    </div>
</form>

```

1. 우선 form에 url 부분은 'result'로 설정했습니다.

2. form의 method는 post로 설정하였습니다.

   <details><summary>form태그란?</summary>
       form태그란 사용자가 입력한 정보를 서버로 한번에 전송하는 역할을 하는 태그입니다. 전송한 데이터는 웹 서버가 처리한 후 결과에 따른 또 다른 웹 페이지를 보여주게 됩니다.
   </details>

   여기서 잡고 가야 할 개념이 나옵니다. 바로 GET과 POST 개념이죠!

   GET과 POST의 가장 큰 차이점은 URL 끝에 데이터를 붙이느냐, 안붙이느냐 입니다.

   ![image](https://user-images.githubusercontent.com/42667951/79074619-67b06a00-7d28-11ea-9690-55f3292cd3a6.png)

   URL 끝에 데이터를 붙이는게 GET 방식, 데이터를 붙이지 않는 것이 POST 방식입니다.  

   GET방식은 뒤에 데이터를 붙이기 때문에 보안에 취약합니다. 그래서 GET 메소드는 데이터를 읽거나 검색할 때 사용하게 됩니다. 또한 GET 요청은 같은 요청을 여러 번 하더라도 변함없이 항상 같은 응답을 받을 수 있습니다. 따라서 해당 메소드는 데이터 변경이 자주일어나는 안전하지 않은 연산에 사용하면 안됩니다.

   

   POST방식은 GET과는 다르게 보안에 신경을 쓴 방식입니다. POST 메소드는 주로 새로운 리소스를 생성 및 수정을 할 때 사용됩니다. (사용자에게 값을 받을 때... 약간 뇌피셜)  POST 방식은 요청을 반복했을 때 항상 같은 결과물이 나오는 것을 보장하지 않아요. 그래서 두개의 같은 POST 요청을 보내도 같은 정보를 담은 두개의 다른 resource를 반환할 가능성이 있습니다.

   

   더 궁금하신 분들을 위해 GET과 POST의 차이를 좀 정리해둘게용.

   <details><summary>GET vs POST </summary>
   GET<br/>
       - 파라미터들의 URL의 일부분 : 브라우저 히스토리에 남는다.<br/>
       - 파라미터들의 URL로 인코딩 됨 : 즐겨찾기가 가능<br/>
       - 전송가능한 데이터 크기가 제한됨<br/>
       - URL 뒤에 데이터가 붙음 : 보안에 취약함 + 히스토리에 저장 + 로그<br/>
       - 같은 요청을 여러번 보내도 항상 같은 응답이 옴<br/>
       <p>
   POST<br/>
       - 브라우저 히스토리에 남지 않는다.<br/>
       - 파라미터들이 request URL에 나타나는 것이 아닌 request body에 포함 : 즐겨찾기가 불가능 <br/>
       - 전송가능한 크기 제한 없음<br/>
       - GET보다 보안에 강함<br/>
       - 같은 요청에 같은 응답을 보장하지 않음.
   </details>

   그런데 여기서 {% csrf_token %} 이라는게 있죠? 이건 POST 메소드라는 걸 쓸 때 반드시 붙여줘야 하는 겁니다.  파라미터가 넘어갈 때 사이트간 위조 요청 공격을 막기위한 거거든요. 자세한 내용은 출처에 태그를 달아놓겠습니다. 

   

3. submit은 form의 action을 찾아간다.

   아직 form의 action 부분을 채우진 않았지만, button type = 'submit'인 경우 해당 버튼을 누르면 form의 action url에 있는 곳으로 찾아가게 됩니다. 이를 기억해 주세요.

   

4. {% url 'result' %} 가 뭐예요?

   이거 wordcount에서 있었던 거죵? 템플릿 태그이고 안에 들어있는 것은 url.py에서 path에 설정한 이름 중 하나입니다.여기선 views.py의 result함수가 return한 것을 의미하겠군요. view의 result 함수는 아래에서 보여주겠습니다.

   

5. input의 이름을 'korea'로 설정한다. 또한 각 button들의 이름도 나라에 맞게 설정해 줍니다. 이부분들은 views.py에서 이용되니 기억해주세요.

### 3. result.html

결과 페이지에는 페이지 제목, 내가 입력한 숫자, 환전 결과, 다시 home으로 돌아갈 버튼을 만들어 줄겁니다. 이 것도 일단은 꾸미는 것없이 쭉 씁니다. div 태그 사이 빈칸은 나중에 채울 거니까 일단은 보류!

```html
<head>
    <meta charset="UTF-8">
</head>

<h1>환율 결과 페이지입니다.</h1>

<h4> 입력한 KOR 원</h4>
<div class = "card">
    <div class = "container">

    </div>
</div>

<h4> KOR -> 환전결과</h4>
<div class = "card">
    <div class = "container">
     
    </div>
</div>

<p>
    <a href=''>home으로</a>
</p>

```

### 4. views.py

이번 환율 실습의 핵심 중의 핵심! views.py입니다.   

[난이도 업업 버전!] : 

우선 네이버 환율정보 사이트에서 환율 정보를 가져오는 작업을 먼저 해봅시다.  Beatuifoulsoup을 이용해서 크롤링을 해오는 방법도 있지만 오늘은 간단하게 pandas를 이용해볼게요. 

![image](https://user-images.githubusercontent.com/42667951/79089579-9b6bae00-7d81-11ea-9176-23fbec22fa49.png)위 사진에 있는 네이버 환율정보 사이트에서 환율 정보  테이블을  가져와 이를 데이터 프레임으로 받은 후 나라별 매매기준율에 대한 정보만 리스트에 넣어주도록 하겠습니다.

```python
from django.shortcuts import render

import pandas as pd

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%ED%99%98%EC%9C%A8%EC%A1%B0%ED%9A%8C'
tables = pd.read_html(url)
df = tables[1]
df.columns
df=df[['매매기준율']]
exchange_list = df.values.tolist()
exchange_list = sum(exchange_list,[])
```

코드 한줄 한줄에 대한 설명은 수업 때 하겠습니다. 여기서 중요한건 python도 중요하지만 django의 구성이 더 중요하니까요! 코드를 짤 때 저는 터미널에 python이라고 친 후 확인하면서 코드를 짰습니다. 이거에 대한 방법은 자유롭게~!

위 코드를 실행시키기 위해서는 필요한 패키지가 있습니다. 아래 패키지를 설치해야 네이버 환율 페이지에서 환율정보를 가져올 수 있어요.  

```bash
$ pip install pandas
$ pip install lxml

```

이제 각 html을 처리해줄 함수들을 만들어보아요. 우선 요청이 들어오면 html을 보여주기만 하면 되는 home과 about 함수 먼저 만들어줍시다.

```python
def home(request):
    return render(request,'exchangeapp/home.html')

def about(request):
    return render(request,'exchangeapp/about.html')

```

result함수에서는 아까 리스트로 만들어준 매매기준율을 사용자가 입력한 한국돈에 나누어서 환전한 값을 만들어줄거고, 그 값을 render를 이용해서 넘겨줄거에요.

```python
def result(request):
	nation = list(['USD','JPY','EUR','CNY','GBP','AUD','CAD','NZD'])

    for i in range(8):
        if nation[i] in request.POST:
            name = nation[i]
            korea = request.POST['korea']
            tocountry = int(korea)
            tocountry = tocountry / exchange_list[i]
            return render(request,'exchangeapp/result.html',{'country':tocountry,'name':name,'korea':korea})

```

우선 함수를 하나로 만들기 위해서 for문을 써줄거에요. 사용자가 누른 버튼마다 각각 이름을 설정해줬죠??? USD, JPY, EUR 이런식으로요. if문은 해당 버튼을 구별해 주기 위한 코드입니다. POST방식으로 넘어온 요청중에서 USD가 있다면 name이란 변수에 USD를 넣어라. 라는 뜻입니다. 만약에 POST 방식으로 넘어온 요청중에 JPY가 있다면 name이란 변수에 JPY를 넣어라가 되겠죠?

그 이후 korea변수에 아까 html form에서 사용자가 입력한 한국 돈을 POST방식으로 받아와 저장합니다. 지금 이 변수는 int형이 아니라 계산을 위해서 int형으로 바꿔줘야해요. 이에 해당하는 코드가 tocountry = int(korea) 입니다.

이제 각 나라별로 환전을 해줘야겠죠? 아까 위해서 exchange_list라는 리스트에 매매기준율을 받아왔습니다. USD에 해당하는 매매기준율은 exchange_list[0]이고 JPY에 해당하는 매매기준율은 exchange_list[1] 입니다. nation리스트와 매매기준율 나라는 같은 순서로 설정을 해놓았습니다.  tocountry = tocountry / exchange_list[i]는 한국 돈을 각 나라별 매매기준율로 나누어준 값을 tocountry라는 변수에 저장하는 코드입니다.

마지막으로 우리는 result페이지에 에 한국돈, 선택한 나라, 환전한 돈 에 대한 값을 넘겨줄거에요. 3개의 변수를 view에서 넘기기위해서는 저번에 말한 render의 context에 넘길 변수를 입력해줘야해요.

```
render(request, template_name, context=None, content_type=None, status=None, using=None)

```

```python
 return render(request,'exchangeapp/result.html',{'country':tocountry,'name':name,'korea':korea})

```



### 5. result.html 마무리

```html
<head>
    <meta charset="UTF-8">
</head>

<h1>환율 결과 페이지입니다.</h1>

<h4> 입력한 KOR 원</h4>
<div class = "card">
    <div class = "container">
		{{korea}}
    </div>
</div>

<h4> KOR -> {{name}} 환전결과</h4>
<div class = "card">
    <div class = "container">
     	{{country}}
    </div>
</div>

<p>
    <a href=''>home으로</a>
</p>
```

### 6. BeautifulSoup


HTML 및 XML 문서를 구문 분석하기 위한 Python 패키지입니다.

웹문서의 구조를 찾아내는 파서를 이용하여서 찾고자 하는 데이터의 위치를 찾아 내어 값을 추출하게 됩니다.

```bash
$ pip install beautifulsoup4
$ pip install html5lib
```

```python
from django.shortcuts import render

from urllib.request import urlopen
from bs4 import BeautifulSoup
# Create your views here.

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8"
html = urlopen(url)
source = html.read()
#해당 URL에 있는 html 데이터를 바이트 문자열로 반환한다.
html.close()

soup = BeautifulSoup(source, "html5lib")
#html5lib = html문서를 트리구조로 분석해주는 라이브러리 - 원하는 내용 추출 위함 (html dom 참조)
country = soup.select('table > tbody > tr > th > a > span > em')
tables = soup.find("table",class_="rate_table_info")
rate = tables.find_all("td",{'class': ''})

list = []

for item in zip(country,rate):
    list.append(
        {
            'country' : item[0].text,
            'rate' : item[1].text
        }
    )

def home(request):
    return render(request,'exchangeapp/home.html')

def result(request):

    nation = [0 for i in range(8)]
    exchange_list = [0 for i in range(8)]
    for i in range(8):
        t = listup[i]
        nation[i] = t['country']
        te = t['rate']
        te = te.replace(',', '')
        exchange_list[i] = float(te)

    for i in range(8):
        if nation[i] in request.POST:
            name = nation[i]
            korea = request.POST['korea']
            tocountry = int(korea)
            tocountry = tocountry / exchange_list[i]
            return render(request,'exchangeapp/result.html',{'country':tocountry,'name':name,'korea':korea})
```

urllib.request = URL을 가져오기 위한 파이썬 모듈입니다. 



오늘 다룬 네이버 페이지는 로그인을 하지 않아도 정보를 가져올 수 있으며, 새로고침을 하기전까지는 데이터가 변하지 않는 정적인 페이지 입니다. 

다음에 함께 크롤링이 필요할 때가 오면 그땐 동적페이지, 사진을 불러오고 해당 내용을 model에 까지 저장하는 것을 해봅시다~!





### 7. Bootstrap 사용하여 html 꾸며주기

저번에 네이버 클론코딩해봤겠지만... 우리의 미적감각은 한계가 있고.. 꾸미는건 정말 어렵죠..? 이럴 때 여러분을 도와줄 부트스트랩이라는 멋진 프레임워크가 있습니다.

Bootstrap이란  웹사이트를 쉽게 만들 수 있게 도와주는 html,css,js프레임 워크입니다.

Google에 Bootstrap을 검색해서 들어가면 이런 멋진 꾸며놓은 것들이 있습니다.

![image](https://user-images.githubusercontent.com/42667951/79073624-94618300-7d22-11ea-9320-2eb4d27bad22.png)

놀랍게도 복사 붙여넣기 두번이면 이 멋진 페이지를 마치 내 것인것마냥 사용할 수 있어요.

# 출처

- [form 태그]('http://www.nextree.co.kr/p8428/')
- [GET vs POST]('https://im-developer.tistory.com/166')
- [CSRF Token]('https://jjinisystem.tistory.com/41')
