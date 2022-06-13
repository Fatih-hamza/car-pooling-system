from django.shortcuts import render
from .models import Proposition
from core.models import MyUser

# Create your views here.

def homeCovoiturage(request):
    return render(request, 'homeCovoiturage.html')

def addProposition(request):

    if request.method == 'POST':
        proposition = Proposition()
        conducteur = MyUser.objects.get(is_logged=True)
        proposition.conducteur_id = conducteur.id
        proposition.depart = request.POST.get('depart')
        proposition.arrivee= request.POST.get('arrivee')
        proposition.date = request.POST.get('date')
        proposition.places_libres = request.POST.get('places_libres')
        proposition.cotisation = request.POST.get('cotisation')
        proposition.description = request.POST.get('description')
        proposition.save()
        return render(request, 'propositionAdded.html')

    return render(request, 'addProposition.html')

def wantProp(request):
    if request.method == 'GET':
        if request.GET.get('depart') and request.GET.get('arrivee'):
            dprt = request.GET.get('depart')
            arv = request.GET.get('arrivee')
            plcs = request.GET.get('places_libres')
            propositions = Proposition.objects.filter(depart=dprt, arrivee=arv).values()
            for prop in propositions:
                
                conduct = MyUser.objects.get(id=prop['conducteur_id'])
                
                prop['name'] = conduct.first_name + " " + conduct.last_name
                prop['image'] = conduct.profile_pic
                prop['rating'] = conduct.rating
                
                

            return render(request, 'findProposition.html', {'proposition':propositions})
    return render(request, 'wantProp.html')

def FAQ(request):
    return render(request, 'FAQ.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')



