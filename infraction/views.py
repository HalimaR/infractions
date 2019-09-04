from django.shortcuts import render
import json
# Create your views here.


def zoeken(request, speed):
    infraction_speed = speed
    with open('data.json') as json_file:
        date = json.load(json_file)
        for p in date:
            print('straat: '+p['street'])
    #meer of gelijk speed
    return render(request, 'infraction/list.html', {})
    
