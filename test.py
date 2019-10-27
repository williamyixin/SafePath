from __future__ import print_function
import json
import requests
import sys

import random #for testing only
from math import sqrt

def elevation(lat, lng):
    # return random.randint(200,500)
    apikey = "AIzaSyBKatwBAmFSYjefKc2a6QPPdvMPG57Pwbg"
    url = "https://maps.googleapis.com/maps/api/elevation/json"
    request = requests.get(url+"?locations="+str(lat)+","+str(lng)+"&key="+apikey)
    try:
        results = json.loads(request.text).get('results')
        if 0 < len(results):
            elevation = results[0].get('elevation')
            #resolution = results[0].get('resolution') # for RESOLUTION
            # ELEVATION
            return elevation
        else:
            print('HTTP GET Request failed.')
    except ValueError as e:
        print('JSON decode failed: '+str(request) + str(e))

def collectdata(start_lat, start_lon, tile_size, grid_x, grid_y): #start_lat and start_lon are the upper left (north west) coordinates
    #grid_x and #grid_y are how many measurements are being taken for each direction
    f = open("topography_testing1.txt","w+")
    num_data_points = grid_x * grid_y
    counter = 0
    previous = 0
    for i in range(grid_y):
        for j in range(grid_x):
            multiplier = (1-2*(i%2)) * (1-2*(j%2))
            curr_lat, curr_lon = start_lat - tile_size * i + (multiplier * (tile_size * sqrt(3) / 6)), start_lon + tile_size * 0.5 * j
            elev = elevation(curr_lat, curr_lon)

            progress = str(round(100*counter/num_data_points))
            if progress != previous:
                print('Progress: ', str(progress) + '%')
                previous = progress
            counter += 1

            f.write(str(j) + ' ' + str(i) + ' ' + str(elev) + '\n')
            #print(j, i, elev)
            #print(curr_lat, curr_lon, elev)

#collectdata(0, 0, 1, 50, 25)
command_args = sys.argv
collectdata(command_args[1], command_args[2], command_args[3], command_args[4], command_args[5])