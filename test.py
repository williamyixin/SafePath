from __future__ import print_function
import json
import requests

def elevation(lat, lng):
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

print(elevation(48.512315, 12.434518))