from flask import Flask, render_template, request
import pickle
import numpy as np
import joblib



lr = joblib.load('ipl_cricket.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
        batting_team = request.form['batting_team']
        if batting_team == 'Sun Risers Hyderabad':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Rajastan Royals':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
            
        bowling_team = request.form['bowling_team']
        if bowling_team == 'Sun Risers Hyderabad':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Rajastan Royals':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            

        venue = int(request.form['venue'])    
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        
        temp_array = temp_array + [venue,overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        
        data = np.array([temp_array])
        predictions = int(lr.predict(data)[0])
              
        return render_template('index.html', prediction_text='The Score will be:{}'.format(predictions))


if __name__ == '__main__':
    app.run(debug=True)
