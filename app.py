from flask import Flask,request,render_template

from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            person_gender=request.form.get('person_gender'),
            person_education=request.form.get('person_education'),
            person_home_ownership=request.form.get('person_home_ownership'),
            loan_intent=request.form.get('loan_intent'),
            previous_loan_defaults_on_file=request.form.get('previous_loan_defaults_on_file'),
            person_age=float(request.form.get('person_age')),
            person_income=float(request.form.get('person_income')),
            loan_amnt=float(request.form.get('loan_amnt')),
            loan_int_rate=float(request.form.get('loan_int_rate')),
            loan_percent_income=float(request.form.get('loan_percent_income')),
            cb_person_cred_hist_length=float(request.form.get('cb_person_cred_hist_length')),
            person_emp_exp=int(request.form.get('person_emp_exp')),
            credit_score=int(request.form.get('person_income'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0")        


