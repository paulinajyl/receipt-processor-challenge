# following: https://fastapi.tiangolo.com/tutorial/testing/#fastapi-app-file
# and https://www.youtube.com/watch?v=yEYXF9XtbE0&list=PL8VzFQ8k4U1L5QpSapVEzoSfob-4CR8zM&index=58

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_example1():
    """
    test the examples from the repo
    """

    eg1 = {
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },{
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    },{
      "shortDescription": "Knorr Creamy Chicken",
      "price": "1.26"
    },{
      "shortDescription": "Doritos Nacho Cheese",
      "price": "3.35"
    },{
      "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
      "price": "12.00"
    }
  ],
  "total": "35.35"
}
    
    # test post response
    response = client.post("/receipts/process", json=eg1)
    assert response.status_code == 200
    assert "id" in response.json()
    receipt_id = response.json()["id"]

    # test get response
    response2 = client.get(f"/receipts/{receipt_id}/points")
    assert response2.status_code == 200
    points = response2.json()["points"]
    assert points == 28

def test_example2():
    """
    test the examples from the repo
    """

    eg2 = {
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}
    
    # test post response
    response = client.post("/receipts/process", json=eg2)
    assert response.status_code == 200
    assert "id" in response.json()
    receipt_id = response.json()["id"]

    # test get response
    response2 = client.get(f"/receipts/{receipt_id}/points")
    assert response2.status_code == 200
    points = response2.json()["points"]
    assert points == 109

def test_invalid_id():
    """
    test if id does not exist
    """
    # test get response
    response = client.get("/receipts/1234567890/points")
    assert response.status_code == 404
    print(response.json())
    assert response.json() == {"detail": "No receipt found for that ID."}


# class Tests:  
# could set up integration tests here?
#     def __init__(self):
#         self.client = TestClient(app)
        
#     def test_eg1(self):
#         return None
    
#     def test_eg2(self):
#         return None
    