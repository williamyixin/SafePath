from __future__ import print_function
import json
import requests

import random #for testing only

def elevation(lat, lng):
    return random.randint(200,500)
    # apikey = "AIzaSyBKatwBAmFSYjefKc2a6QPPdvMPG57Pwbg"
    # url = "https://maps.googleapis.com/maps/api/elevation/json"
    # request = requests.get(url+"?locations="+str(lat)+","+str(lng)+"&key="+apikey)
    # try:
    #     results = json.loads(request.text).get('results')
    #     if 0 < len(results):
    #         elevation = results[0].get('elevation')
    #         #resolution = results[0].get('resolution') # for RESOLUTION
    #         # ELEVATION
    #         return elevation
    #     else:
    #         print('HTTP GET Request failed.')
    # except ValueError as e:
    #     print('JSON decode failed: '+str(request) + str(e))

def collectdata(start_lat, start_lon, tile_size, grid_x, grid_y): #start_lat and start_lon are the upper left (north west) coordinates
    #grid_x and #grid_y are how many measurements are being taken for each direction
    f = open("topography_testing1.txt","w+")
    for i in range(grid_y):
        for j in range(grid_x):
            curr_lat, curr_lon = transformtotriangle(start_lat - tile_size * i, start_lon + tile_size * j, tile_size)
            elev = elevation(curr_lat, curr_lon)
            f.write(str(j) + ' ' + str(i) + ' ' + str(elev) + '\n')
            #print(j, i, elev)
            #print(curr_lat, curr_lon, elev)

def transformtotriangle(lat, lon, tile_size):
    return lat, lon

collectdata(37.88785, -122.24825, 0.00001, 50, 25)