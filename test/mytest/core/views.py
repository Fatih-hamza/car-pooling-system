from django.shortcuts import render, redirect
# from numpy import _FlatIterSelf
from covoiturage.models import Voiture, Commentaire
from .models import User, MyUser
from .forms import UserForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')


def home_core(request):
    return render(request, 'home_core.html')



def login(request):
    if request.method == 'GET':
        if request.GET.get('email') and request.GET.get('password'):
            mail = request.GET.get('email')
            passwd = request.GET.get('password')
            authentified = MyUser.objects.filter(email=mail, password=passwd).values()
            if len(authentified) == 0:
                return render(request, 'failure.html')
            else:
                # here you should get the id of the user, and change its state to logged
                print('--------------------')
                the_logged_id = authentified[0]['id']
                the_logged_nature = authentified[0]['nature']

                the_logged = MyUser.objects.get(id=the_logged_id)
                MyUser.objects.filter().update(is_logged=0)
                the_logged.is_logged = True
                the_logged.save()
                print(type(the_logged))
                if the_logged_nature == 'c':
                    return render(request, 'logged_conducteur.html')
                else:
                    return render(request, 'logged_passenger.html')
            
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        if request.POST.get('password1') and request.POST.get('password2') and request.POST.get('password1') == request.POST.get('password2'):
            user = MyUser()
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.date_naissance = request.POST.get('date_naissance')
            if request.POST.get('nature') == 'passenger':
                user.nature = 'p'
            else:
                user.nature = 'c'
            user.email = request.POST.get('email')
            user.number = request.POST.get('phone')
            user.password = request.POST.get('password1')
            user.save()
            return redirect(login)
            
    return render(request, 'register.html')


def logout(request):
    the_logged = MyUser.objects.get(is_logged=True)
    the_logged.is_logged = 0
    the_logged.save()
    return redirect(index)


def profile(request):
    the_user = MyUser.objects.get(is_logged=True)
    context = {'info': the_user}
    return render(request, 'profile.html', context)

def conducteur_profile(request, id):
    conducteur = MyUser.objects.get(id=id)
    vtr = Voiture.objects.get(conducteur_id=id)
    
    comments = Commentaire.objects.filter(conducteur_id=id).values()
    for cmnt in comments:
        moul_lcmnt = MyUser.objects.get(id=cmnt['passanger_id'])
        cmnt['img'] = moul_lcmnt.profile_pic
        cmnt['name'] = moul_lcmnt.first_name + " " + moul_lcmnt.last_name
        
    context = {'info':conducteur, 'voiture':vtr, 'commnts':comments}

    return render(request, 'profile1.html', context)

def update_profile(request):
    active = MyUser.objects.get(is_logged=True)
    context = {'info': active}
    if request.method == 'POST':
        if request.POST.get('first_name'):
            MyUser.objects.filter(is_logged=True).update(first_name=request.POST.get('first_name'))
            active.refresh_from_db()

        if request.POST.get('last_name'):
            MyUser.objects.filter(is_logged=True).update(last_name=request.POST.get('last_name'))
            active.refresh_from_db()

        if request.POST.get('number'):
            MyUser.objects.filter(is_logged=True).update(number=request.POST.get('number'))
            active.refresh_from_db()
            
        if request.POST.get('email'):
            MyUser.objects.filter(is_logged=True).update(email=request.POST.get('email'))
            active.refresh_from_db()
        
        if request.POST.get('description'):
            MyUser.objects.filter(is_logged=True).update(description=request.POST.get('description'))
            active.refresh_from_db()

            
    return render(request, 'update_profile.html', context)


