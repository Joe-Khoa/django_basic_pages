from django.shortcuts import render
import json
from django.http import HttpResponse
# Create your views here.
import urllib.request

def index(request):
    data = {}
    if request.method == 'POST':
        city = request.POST['city']
        try :
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=b035d121ff439c272df931cfce3dbeec').read()
        except :
            data = {'error' : 'Not found '+"'"+city+"'"+' city!'}
            return render(request,'main_app/index.html',data)

        else:
            # print('\n'*3,url_open,'\n'*3)
            # source = url_open.read()
            # source = urllib.request.urlopen('https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22').read()
            # print('/n'+source+'/n')
            # byte object to string obj ( standard JSON)
            # print(type(source))
            list_of_data = source.decode('utf-8')
            # to normal obj (string obj to object)
            list_of_data = json.loads(list_of_data)
            # if list_of_data['cod'] != '404':
            data = {
                "city_name":str(list_of_data['name']),
                "country_code":(str(list_of_data['sys']['country']).lower()),
                "coordinate":str(list_of_data['coord']['lon'])+' | '+str(list_of_data['coord']['lat']),
                "temp":str(round(list_of_data['main']['temp'] - 273.15,2))+'°C',
                "pressure":str(list_of_data['main']['pressure'])+' hpa',
                "humidity":str(list_of_data['main']['humidity'])+'%',
                }
    return render(request,'main_app/index.html',data)




############################### ___draft___###############################

import os
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'city_list.json')
from pprint import pprint

def get_json():
    # with open(file_path) as f:
    #     print(type(f))
    data = ''
    with open(file_path,encoding='cp1252') as f:
        data = json.load(f)
        for line in f:
            # data = data + line
            pprint(type(line))
    # print(data)
    # print(data)
    # for a in f:
        # x = json.load(a)
        # print(a)
    # data = json.loads(f)
    # print(data)
    # data = []
    # with open(file_path) as f:
    #     for line in f:
    #         data.append(json.loads(line))
    # print(data)
