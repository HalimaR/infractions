from django.shortcuts import render
import json
# Create your views here.


def zoeken(request, speed):
    infraction_speed = speed
    infraction_speed = []
    with open('data.json') as json_file:
        date = json.load(json_file)
        for p in date:
            if(speed <= p['infractions_speed']):
                infraction_speed.append(p)
                #print('speed: '+p['street'])
    return render(request, 'infraction/list.html', {'speedlijst': infraction_speed})
    
