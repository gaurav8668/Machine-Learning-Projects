from flask import Flask, render_template, request
import sklearn
import pickle
import pandas as pd 

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        ## Date of Journey
        date_dep = request.form['Dep_Time']
        Journy_Day = int(pd.to_datetime(date_dep, format='%Y-%m-%dT%H:%M').day)
        Journy_month = int(pd.to_datetime(date_dep, format='%Y-%m-%dT%H:%M').month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format='%Y-%m-%dT%H:%M').hour)
        Dep_min = int(pd.to_datetime(date_dep, format='%Y-%m-%dT%H:%M').minute)

        ## Arrival
        date_arr = request.form['Arrival_Time']
        Arrival_hour = int(pd.to_datetime(date_arr, format='%Y-%m-%dT%H:%M').hour)
        Arrival_min = int(pd.to_datetime(date_arr, format='%Y-%m-%dT%H:%M').minute)

        ## Duration
        dur_hour = abs(Dep_hour - Arrival_hour)
        dur_min = abs(Dep_min - Arrival_min)

        ## Total stops
        Total_stops = int(request.form['stops'])

        ## Airline
        airline = request.form['airline']
        if airline == 'Jet Airways':
            Jet_Airways = 1
            # Jet Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Buisness = 0
            Vistara_Preminum_economy = 0
            Trujet = 0

        elif airline == 'IndiGo':
            Jet_Airways = 0
            IndiGo = 1
            Air_India= 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Buisness = 0
            Vistara_Preminum_economy = 0
            Trujet = 0

        elif airline == 'Air_India':
            Jet_Airways = 0
            IndiGo = 0
            Air_India= 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Buisness = 0
            Vistara_Preminum_economy = 0
            Trujet = 0

        elif airline == 'Multiple_carriers':
            Jet_Airways = 0
            IndiGo = 0
            Air_India= 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Buisness = 0
            Vistara_Preminum_economy = 0
            Trujet = 0
        
        elif airline == 'SpiceJet':
            Jet_Airways = 0
            IndiGo = 0
            Air_India= 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Buisness = 0
            Vistara_Preminum_economy = 0
            Trujet = 0
        
        elif airline == 'Vistara':
            Jet_Airways = 0
            IndiGo = 0
            Air_India= 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Buisness = 0
            Vistara_Preminum_economy = 0
            Trujet = 0
        
        if airline == 'GoAir':
            Jet_Airways = 0
            IndiGo = 0
            Air_India= 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Buisness = 0
            Vistara_Preminum_economy = 0
            Trujet = 0
        
        elif airline == 'Multiple_carriers_Premium_economy':
            Jet_Airways = 0
            IndiGo = 0
            Air_India= 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Buisness = 0
            Vistara_Preminum_economy = 0
            Trujet = 0
        
        elif airline == 'Jet_Ariways_Buisness':
            Jet_Airways = 0
            IndiGo = 0
            Air_India= 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Buisness = 1
            Vistara_Preminum_economy = 0
            Trujet = 0
        
        elif airline == 'Vistara_Premium_economy':
            Jet_Airways = 0
            IndiGo = 0
            Air_India= 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Buisness = 0
            Vistara_Preminum_economy = 1
            Trujet = 0
        
        elif airline == 'Turjet':
            Jet_Airways = 0
            IndiGo = 0
            Air_India= 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Buisness = 0
            Vistara_Preminum_economy = 0
            Trujet = 1
        
        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        
        ## Source
        source = request.form['Source']
        if source == 'Delhi':
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
        
        elif source == 'Kolkata':
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0
        
        elif source == 'Mumbai':
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0
        
        elif source == 'Chennai':
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1
        
        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
        
        ## Destination 
        destination = request.form['Destination']
        if destination == 'Cochin':
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
        elif destination == 'Delhi':
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
        elif destination == 'New_Delhi':
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0
        
        elif destination == 'Hyderabad':
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0
        
        elif destination == 'Kolkata':
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1
        
        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
        prediction = model.predict([[
            Total_stops,
            Journy_Day,
            Journy_month,
            Dep_hour,
            Dep_min, 
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Buisness,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet, 
            Trujet,
            Vistara, 
            Vistara_Preminum_economy,
            s_Chennai,
            s_Delhi, 
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_New_Delhi
        ]])
        output = round(prediction[0], 2)
        return render_template('home.html', prediction_text='Your Flightprice is Rs.{}'.format(output))


    else:
        return render_template('home.html')


        


if __name__ == '__main__':
    app.run(debug=True)
