from django.http import HttpResponse
from django.shortcuts import render
from .functions import  next_song, neighbor_stations

def view_next_song(request, station_id):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    # code pour tester créer 
    n_sg = next_song(station_id=station_id)
    text = """ <h1> Test station """+station_id+""" next song is : """+ n_sg+"""</h1>"""
    return HttpResponse(text)


    view_neighbor_stations

def view_neighbor_stations(request, latitude, longitude):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    # code pour tester créer 
    stations = neighbor_stations(lat=latitude, longi=longitude)
    text = """ <h1> Test neigboor station :"""
    for station in stations:
        text+= """S """+station+""","""
    text += """</h1>"""
    return HttpResponse(text)