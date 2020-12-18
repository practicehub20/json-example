from django.shortcuts import render
from app1.utils import getRequest


# Create your views here.
def state_wise_beds_avail(request):
    data = getRequest('https://api.rootnet.in/covid19-in/hospitals/beds')
    if data['success']:
        return render(request,'hospital.html',{'result' : data})
    else:
        return render(request,'hospital.html',{'error' : 'Requested resource is not available.'})

def state_wise_colleges_avail(request):
    data = getRequest('https://api.rootnet.in/covid19-in/hospitals/medical-colleges')
    if data['success']:
        return render(request,'medical.html',{'result' : data})
    else:
        return render(request,'medical.html',{'error' : 'Requested resource is not available.'})

def state_wise_contacts(request):
    data = getRequest('https://api.rootnet.in/covid19-in/contacts')
    if data['success']:
        return render(request,'contact.html',{'result' : data})
    else:
        return render(request,'contact.html',{'error' : 'Requested resource is not available.'})