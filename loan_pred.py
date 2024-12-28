from flask import Flask, request
import pickle

app = Flask(__name__)

with open("classifier.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return '<h1>Welcome to the Loan Tap pred! UPDATEDDDD</h1>'

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return '<h1>This is get not post</h1>'
    else:
        loan_req = request.get_json()
        print(loan_req)

        if loan_req['Gender'] == "Male":
            Gender = 0
        else:
            Gender = 1

        if loan_req['Married'] == "Unmarried":
            Married = 0
        else:
            Married = 1

        # if loan_req['Credit_History'] == "Unclear Debts":
        #     Credit_History = 0
        # else:
        #     Credit_History = 1

        ApplicantIncome = loan_req['ApplicantIncome']
        LoanAmount = loan_req['LoanAmount']
        Credit_History = loan_req['Credit_History']
        
        input_data = [Gender, Married, ApplicantIncome, LoanAmount, Credit_History]
        pred = model.predict([input_data])
        
        result = "Approved" if pred == 1 else "Rejected"
        
        return {
            "loan_approval_status": result
        }
        
        
# docker tag local-image:tagname new-repo:tagname
# docker push new-repo:tagname

# my docker app -> docker pull aftab0409/ml-learnings-2024:flask_new_app