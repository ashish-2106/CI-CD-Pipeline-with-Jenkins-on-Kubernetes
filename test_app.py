# tests/test_app.py

from app import greet

def test_greet():
    assert greet("Jenkins") == "Hello, Jenkins!"
