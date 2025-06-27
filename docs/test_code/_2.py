from fastapi import FastAPI
import json
import httpx
import requests
app = FastAPI()

# Asynchronous endpoint
@app.get("/fetch-todo")
async def get_url():
    url = "https://jsonplaceholder.typicode.com/todos/2"
    
    # Use httpx for asynchronous GET request
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        
        # Get the response body (text) as a string
        data_text = response.text
        print(type(data_text))  # <class 'str'>
        
        # Convert the JSON string into a Python object
        data = json.loads(data_text)
        print(data, type(data))  # <class 'dict'>

        print(f"this is title \"{data['title']}\"")
    return data


# Fetch data from an open-source public API (JSONPlaceholder for example)
@app.get("/fetch-todo/{todo_id}")
async def fetch_todo(todo_id: int) -> dict:
    # URL of the open-source API
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    
    # Fetch data using requests library
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse JSON response into a Python dictionary
        return data
    else:
        return {"error": "Unable to fetch data", "status_code": response.status_code}