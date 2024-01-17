from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_scrape_facebook():
    id=2756460277826028  
    access_token="EAAM3HZBkiEskBO2p2bwesKhpzQxRvokrthi57dWXrKnWA44GhYociqkSaBne5rSQxfHSOrn9jpAQnE57p6VP6KmYwrumBNR1dO3kfknWtxz2zXPSaKkEKCIRZC63Y9HrkK1HCZBpSybpKW2M3IG1XSetG6O3100jXMYOxT1pZAwDncz1fBGcT1tp"
    # Replace 'id' with the actual Facebook page ID you want to test
    response = client.get(f"/scrape-facebook/{id}?access_token={access_token}")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains the expected message
    assert response.json()["message"] == "Scraping successful"

    # Add more assertions based on your specific requirements
    # For example, you can check if the returned data structure is as expected
    assert "data" in response.json()
    assert "email" in response.json()["data"]
    assert "name" in response.json()["data"]
    assert "short_name" in response.json()["data"]
    assert "name_format" in response.json()["data"]

