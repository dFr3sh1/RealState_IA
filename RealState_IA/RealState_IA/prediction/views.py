from django.shortcuts import render
import  pickle
from prediction.forms import PredictionForm
from django.shortcuts import render, redirect
from .models import PredictionModel


with open ('RealState_IA/data/model.pkl', 'rb') as prediction_model:
    model = pickle.load(prediction_model)

def price_prediction(request):
    form = PredictionForm(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            chambres = form.cleaned_data['chambres']
            salles_de_bain = form.cleaned_data['salles_de_bain']
            m2_habitable = form.cleaned_data['m2_habitable']
            m2_Lot = form.cleaned_data['m2_Lot']
            etages = form.cleaned_data['etages']
            vue_sur_leau = form.cleaned_data['vue_sur_leau']
            m2_cave = form.cleaned_data['m2_cave']
            etat = form.cleaned_data['etat']
            m2_above = form.cleaned_data['m2_above']
            lat = form.cleaned_data['lat']
            long = form.cleaned_data['long']
            prediction_house_price = model.predict([[chambres, salles_de_bain, m2_habitable, m2_Lot, etages, vue_sur_leau, m2_cave, etat, m2_above, lat, long]]).round(1)
            model_donnee = PredictionModel(
                chambres = chambres,
                salles_de_bain = salles_de_bain,
                m2_habitable = m2_habitable,
                m2_Lot = m2_Lot,
                etages = etages,
                vue_sur_leau = vue_sur_leau,
                m2_cave = m2_cave,
                etat = etat,
                m2_above = m2_above,
                lat = lat,
                long = long,
                prediction_house_price = prediction_house_price[0],
            
            )
            model_donnee.save()
            return render(request, 'result_prediction.html', {'prediction_house_price': prediction_house_price[0]})
    return render(request, 'price_prediction.html', {'form': form}) 
        

