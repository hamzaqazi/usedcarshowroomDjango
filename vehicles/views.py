from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from django.core.paginator import Paginator
from django.core import serializers

# Create your views here.
def homePage(request):
	vehicles = Vehicle.objects.all().order_by('-id')

	context = {
		'vehicles': vehicles,
	}
	return render(request, 'vehicles/Homepage.html',context)



def usedCarsPage(request):
	if 'q' in request.GET:
		q=request.GET['q']
		vehicles = Vehicle.objects.filter(name__icontains=q).order_by('-id')
	else:
		vehicles = Vehicle.objects.all().order_by('-id')
	paginator = Paginator(vehicles,4)
	page_num = request.GET.get('page',1)
	vehicles = paginator.page(page_num)


	context = {
		'vehicles': vehicles,
	}
	return render(request, 'vehicles/UsedCars.html', context)

def usedCarDetailPage(request,veh_id):
	veh = Vehicle.objects.get(id=veh_id)
	context = {
		'veh':veh,
	}
	return render(request,'vehicles/UsedCarDetails.html',context)


def usedVansPage(request):
	return render(request, 'vehicles/UsedVans.html')

def valetingPage(request):
	return render(request, 'vehicles/Valeting.html')

def autoShinePage(request):
	return render(request, 'vehicles/AutoShine.html')

def contactUsPage(request):
	return render("Contact Us Page")

def sendMessage(request):
	if request.is_ajax():
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')

		new_message = Message(name=name, email=email, phone=phone, message=message)
		new_message.save()
		
		response ={
			'name': name,
			'email': email,
			'phone': phone,
		}

		return JsonResponse(response)
