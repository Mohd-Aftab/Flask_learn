import pytest 

from loan_pred import app

# Proxy to live server
@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.text == '<h1>Welcome to the Loan Tap pred!</h1>'
    
def test_predict_post(client):
    response = client.post('/predict', json={
        "ApplicantIncome" : 1000,
        "Credit_History" : 1.0,
        "Gender" : "Male",
        "LoanAmount" : 10,
        "Married" : "No"
    })
    assert response.status_code == 200
    assert response.json == {"loan_approval_status" : "Approved"}