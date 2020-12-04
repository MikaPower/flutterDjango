import json
from builtins import print, list
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from apps.races.models import Race, Pilot


def index(request):
    races = [{'races': []}]
    for race in Race.objects.order_by("created").all():
        races[0]['races'].append(
            {'id': race.id, 'name': race.name, 'latitude': race.latitude, 'longitude': race.longitude,
             'image': 'http://'+request.get_host()+race.image.url})
    return JsonResponse(races, safe=False)


def get_pilots_race(request, id=''):
    pilots = Pilot.objects.filter(race_id=id).values('name', 'bike_name', 'engine_size', 'race_id')
    return JsonResponse(
        {"pilots": list(Pilot.objects.filter(race_id=id).values('name', 'bike_name', 'engine_size', 'race_id'))})


@csrf_exempt
def get_post_race(request, id=''):
    database_pilot = ""
    if request.method == 'POST':
        pilot = json.loads(request.body)

        try:
            database_pilot = Pilot.objects.filter(bike_name=pilot['bike_name'], race_id=id).get()
            return HttpResponse(status=409)
        except ObjectDoesNotExist:
            race = Race.objects.filter(id=id).first()
            pilot = Pilot(name=pilot['name'], bike_name=pilot['bike_name'],
                          engine_size=pilot['engine_size'],
                          race=race)
            pilot.save()
            race.pilot_set.add(pilot)
            #    str_data = serialize('json', race.pilot_set.all(), cls=DjangoJSONEncoder) # Or you don't need to provide the `cls` here because by default cls is DjangoJSONEncoder
            #   data = json.loads(str_data)
            # data = serializers.serialize("json", race.pilot_set.all())
            pilots = Pilot.objects.filter(id=pilot.id).values('name', 'bike_name', 'engine_size', 'race_id')
            return JsonResponse({"pilot": list(pilots)})


    else:
        return JsonResponse({"race": list(Race.objects.filter(id=id).values())})
