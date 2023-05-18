from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.
def home(request):
    return render(request,'dashbord.html')




def predict(request):
    form = PredictForm()
    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():
            # Récupérer les données entrées par l'utilisateur
            Ram = form.cleaned_data['Ram']
            Poids = form.cleaned_data['Poids']
            Touchscreen = form.cleaned_data['Touchscreen']
            Pixels_par_pouce = form.cleaned_data['Pixels_par_pouce']
            HDD = form.cleaned_data['HDD']
            SDD = form.cleaned_data['SDD']
            algo = form.cleaned_data['algo']
            
            
            if algo == 'GD':
                prcie = Ram + Poids + Touchscreen + Pixels_par_pouce + HDD + SDD
            elif algo == 'GS':
                
                prcie = Ram*(4.46428902*10**2) + Poids*(1.07758781*10**2) + Touchscreen*(-9.07611679) + Pixels_par_pouce*(1.44702323*10) - HDD*0.172695991 + SDD*6.59394598 -27.91944797
            else:
                
                prcie = None
            
            context = {'prcie': prcie,
                       'Ram' : Ram,
                       'Poids' : Poids,
                       'Touchscreen' : Touchscreen,
                       'Pixels_par_pouce' : Pixels_par_pouce,
                       'HDD' : HDD,
                       'SDD' : SDD,
                       'algo' : algo,
                       }
            return render(request, 'predicted_price.html', context)
    context = {'form' : form}
    return render(request, 'predict_form.html', context)


def Gradient_Descent(request):
    return render(request, 'gd.html')


def Gradient_Stochaqtiue(request):
    return render(request, 'gs.html')