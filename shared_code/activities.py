import azure.functions as func
from function_app import app

@app.activity_trigger(input_name="city")
def hello(city: str):
    return f"Hello {city}"