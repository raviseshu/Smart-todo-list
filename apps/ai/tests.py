# apps/ai/tests.py

from .services import example_ai_service

def test_example_ai_service():
    assert example_ai_service() == "AI service is running!"
