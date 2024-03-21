import pickle
from flask import Flask,render_template,request
import numpy as np


#app = Flask(__name__)
app = Flask(__name__, template_folder='Template')
model = pickle.load(open('D:\Personal_projects\machine Learinig model deployment using Flask\model.pkl','rb'))

#url
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods = ['GET','POST'])
def prediction():
    #Result =  model.predict([[request.form.get('temperature')]])
    temperature = request.form.get('temperature')
    # Try converting the input to a float
    temperature_numeric = float(temperature)
    # Now you can use temperature_numeric in your prediction
    result = model.predict([[temperature_numeric]])
    output = result[0][0]
    #print(output)
    return render_template('index.html',predict_result =f"Total  Revenue generated is {output}/-")

if __name__ == '__main__':
    app.run(debug=True)