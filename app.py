import numpy as np
from flask import Flask,render_template, request, jsonify, url_for, redirect
import pickle
import joblib
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

app = Flask(__name__)
model = joblib.load(open('model.pkl', 'rb'))

def budgetRace(inputArray):
    if inputArray[-2]==0:
        inputArray[-2]=500
    elif inputArray[-2] ==1:
        inputArray[-2] = 3000
    elif inputArray[-2] ==2:
        inputArray[-2] =7500
    elif inputArray[-2] ==3:
        inputArray[-2] =15000      
    elif inputArray[-2] ==4:
        inputArray[-2] =35000
    elif inputArray[-2] ==5:
        inputArray[-2] =90000
    else:
        int_features[-2] = 3

def IncomeRace(inputArray):
    if inputArray[-1]==0:
        inputArray[-1]=10000
    elif inputArray[-1] ==1:
        inputArray[-1] = 25000
    elif inputArray[-1] ==2:
        inputArray[-1] =40000
    elif inputArray[-1] ==3:
        inputArray[-1] =60000    
    elif inputArray[-1] ==4:
        inputArray[-1] =85000
    elif inputArray[-1] ==5:
        inputArray[-1] =130000
    else:
        inputArray[-1] = 3     

def predResult(probInput):
        basetext = "Change to get elected is "
        if probInput < 30:
            return basetext + "very low (score 1/5)"
        elif probInput < 45:
            return basetext + "quite low (score 2/5)"  
        elif probInput < 55:
            return basetext + "modest (score 3/5)"   
        elif probInput < 65:
            return basetext + "quite high (score 4/5)"
        else:
            return basetext + "high (score 5/5)" 

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/form")
def form():
    return render_template('form.html') 

@app.route('/form-handler', methods=['POST'])
def handle_data():
    return jsonify(request.form)   

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]

    budgetRace(int_features)
    IncomeRace(int_features)
       
    mylist0 = [32,0,0,0,0,0,0,0,0,0,0,0,0,500,10000]
    mylist1 = [32,1,1,1,1,1,1,1,1,1,1,1,1,500,10000]
    mylist2 = [32,1,1,1,2,2,1,1,2,2,2,1,1,500,10000]
    mylist3 = [32,1,1,1,3,0,1,1,3,3,0,1,1,500,10000]
    mylist4 = [32,1,1,1,1,0,1,1,2,4,0,1,1,500,10000]
    mylist5 = [32,1,1,1,1,0,1,1,0,5,0,1,1,500,10000]
    mylist6 = [32,1,1,1,1,0,1,1,1,6,0,1,1,500,10000]
    mylist7 = [32,1,1,1,1,0,1,1,1,7,0,1,1,500,10000]
    mylist8 = [32,1,1,1,1,0,1,1,1,8,0,1,1,500,10000]

    mydataf = pd.DataFrame([int_features,mylist0, mylist1,mylist2,mylist3,mylist4,mylist5,mylist6,mylist7,mylist8],columns =['age',
            'sex', 'celebrity', 'currently_in_parliament', 'education',
        'mother_tongue', 'twitter_account', 'children', 'employer',
        'work_status', 'languages_known', 'PM_party',
        'external_election_funding', 'elect_budget_new ', 'yearly_income_new'])
    crit1 = mydataf.dtypes!=object
    cat2 = mydataf.columns[crit1].tolist()
    cat3 = cat2[4:10]
    cat3.remove('children')
    cat3.remove('twitter_account')
    
    OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
    OH_cols_train_user = pd.DataFrame(OH_encoder.fit_transform(mydataf[cat3]))

    OH_cols_train_user.index = mydataf.index
    num_X_train2 = mydataf.drop(cat3, axis=1)

    OH_X_user = pd.concat([num_X_train2, OH_cols_train_user], axis=1)    
    userd_newformat= pd.DataFrame(model.predict_proba(OH_X_user.values))
    probability = np.around((userd_newformat.iloc[0,1])*100,decimals = 2)

    return predResult(probability)
    #return jsonify(output) 
    #return render_template('index.html', prediction_text='Chance to get elected is {} %'.format(output))


if __name__ == "__main__":
    app.run(debug=True)