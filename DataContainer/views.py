import requests 
from django.shortcuts import render, redirect
import urllib2, urllib
import json
from .forms import *
from .models import *

# Create your views here.
def get_data(request, slug):
	try:		
		req = urllib2.Request('http://hackathon.ttcloud.net:10026/v1/contextEntities/'+slug)
		req.add_header('Accept', 'application/json')
		req.add_header('fiware-service', 'todosincluidos')
		req.add_header('fiware-servicepath', '/iot')
		resp = urllib2.urlopen(req)
		content = resp.read()
		jsonContent = json.loads(content)
		temperature = jsonContent['contextElement']['attributes'][16]['value']
		humidity    = jsonContent['contextElement']['attributes'][6]['value']
		luminance   = jsonContent['contextElement']['attributes'][8]['value']
		cellid      = jsonContent['contextElement']['attributes'][0]['value']
		lac         = jsonContent['contextElement']['attributes'][7]['value']
		mcc         = jsonContent['contextElement']['attributes'][9]['value']
		mnc         = jsonContent['contextElement']['attributes'][11]['value']

		# get lat and long

		data = urllib.urlencode({
		  'homeMobileCountryCode': 412, # spain
		  'homeMobileNetworkCode': 7,
		  'radioType': 'gsm',
		  'carrier': 'Movistar',
		  'considerIp': 'true',
		  'cellTowers': {'cellId' : cellid, 'locationAreaCode': lac, 'mobileCountryCode': mcc, 'mobileNetworkCode': mnc}
		})
		cabeceras = {"Content-type": "application/json","Accept": "application/json"}
		payload = json.dumps(data)
		# cellid to long and lat
		url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCN_091Vz9Xyq0uEbLpGju8XnyXx_pusT4'

		response = requests.post(url, data=payload, headers=cabeceras)
		lat = response.json()['location']['lat']
		lng = response.json()['location']['lng']

		humidity = float(humidity)/1000000
		return render(request,'container.html', 
			{'temperature' : temperature,
			'humidity'     : humidity,
			'luminance'    : luminance,
			'lat'          : lat,
			'lng'          : lng,
			'slug'		   : slug,
			})
	except:
		return render(request,'container.html',{ 'slug': 'No encontrado'})

def add_data(request):
	form = ContainerForm(request.POST)
	if form.is_valid():
		pass
	pass
	return redirect('index')

def index(request):
	form = ContainerForm()
	