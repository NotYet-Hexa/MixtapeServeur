from MixtapeServeur.apps.station.models import Station

from django.shortcuts import render_to_response


def monitor(request):
    stations = Station.objects.all()
    return render_to_response("hello.html", locals())