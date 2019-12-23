from django.shortcuts import render, redirect
from . import forms, models
import os

# Create your views here.

def Home(request):
    return render(request,'home.html')

def Home_en(request):
    return render(request, 'home_en.html')

def finished(request):
    return render(request, 'finished.html')

def finished_en(request):
    return render(request, 'finished_en.html')

def Location_en(request):
    
    recieved_locations = []
    
    data={
        'locations' : ["kitchen","bedroom","living_room","bath_room","laundry_room","dressing_room","study_room"],
        'things' : []
    }
    
    if request.POST.getlist('things'):
        filename=''
        
        if os.listdir('./collected_data'):
            filename=str(len(os.listdir('./collected_data')))
            
        with open('./collected_data/'+str(filename)+".txt", 'w') as f:
            for location,thing in zip(data['locations'], request.POST.getlist('things')):
                f.write(location)
                f.write(":")
                f.write(thing)
                f.write('\n')
                
        return redirect('../finished/')
    
    return render(request, 'Location_en.html')

def Location(request):
    
    received_locations=[]

    data = {
        'locations' : ["kitchen","bedroom","living_room","bath_room","laundry_room","dressing_room","study_room"],
        'things' : []
    }

    # if (request.GET.get('locations')):
    #     received_locations = request.GET.get('locations')
    #     data['locations'] = received_locations.split()

    if request.POST.getlist('things'):
        filename = ''

        if os.listdir('./collected_data'):
            filename = str(len(os.listdir('./collected_data')))

        with open('./collected_data/'+str(filename)+".txt" , 'w') as f:

            for location,thing in zip(data['locations'],request.POST.getlist('things')):
                f.write(location)
                f.write(":")
                f.write(thing)
                f.write('\n')
            
        return redirect('../finished/')

    return render(request, 'Location.html', data)
