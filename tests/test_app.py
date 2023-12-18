# tests/test_app.py
from modules.app import app

def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert b'Hello, Flask!' in response.data
