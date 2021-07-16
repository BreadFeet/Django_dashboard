import json
import time

from django.http import HttpResponse
from django.shortcuts import render

from myanalysis.population import Population
from myanalysis.weatherdata import WeatherData

# Create your views here.

def index(request):
    data = []
    for i in range(1, 100):
        person = {}                # 사원 한명 당 dictionary 하나를 만들어서 리스트에 추가
        person['name'] = 'James' + str(i)
        person['position'] = 'Position' + str(i)
        person['office'] = 'Office' + str(i)
        person['age'] = i
        d = time.time()
        person['start_date'] = time.ctime(d)
        person['salary'] = i * 1000
        print(person)
        data.append(person)

    context = {
        'section': 'main_section.html',            # section 변수를 주든지, section 없이 페이지를 바로 include 하든지 결과는 같음!
        'person': data                             # 보낸 변수가 main_section 페이지에서 사용됨!!
    }
    return render(request, 'index.html', context)

def dashboard1(request):
    context = {
        'section': 'dashboard1.html'
    }
    return render(request, 'index.html', context)

def dashboard2(request):
    context = {
        'section': 'dashboard2.html'
    }
    return render(request, 'index.html', context)

def dashboard3(request):
    context = {
        'section': 'dashboard3.html'
    }
    return render(request, 'index.html', context)

def dashboard4(request):
    result = Population().age5()
    context = {
        'section': 'dashboard4.html',
        'data': result
    }
    return render(request, 'index.html', context)


def charts(reqeust):
    return render(reqeust, 'charts.html')


def chart1(request):
    data = [{
                'name': 'Tokyo',
                'data': [7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
            }, {
                'name': 'London',
                'data': [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
            }]

    return HttpResponse(json.dumps(data), content_type='application/json')
    # 127.0.0.1/chart1으로 데이터가 확인됨 -> open API와 같음


def chart2(request):
    cmd = request.GET['cmd']
    if cmd == 'a':
        result = Population().age5()
    elif cmd == 'b':
        result = Population().diff3()
    elif cmd == 'c':
        result = Population().diff5()
    else:
        result = Population().P248(cmd)
    return HttpResponse(json.dumps(result), content_type='application/json')


def chart3(request):
    loc = request.GET['loc']
    data = WeatherData().chart3(loc)
    return HttpResponse(json.dumps(data), content_type='application/json')


