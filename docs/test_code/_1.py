import requests
import os
from PIL import Image

BASE_URL='https://dog.ceo/'
ENDPOINT='api/breeds/image/random'

response = requests.get(BASE_URL+ENDPOINT)
print(f"Content-Type: {response.headers.get('Content-Type')}")

data=response.json()

print(data)

if data['status']=="success":
    filename = os.path.basename(data["message"])
    
    path = os.path.normpath(f"download_img/{filename}")
 
    image_url = data['message']
    print(f"Image URL extracted: {image_url}")
    
    image_response = requests.get(image_url)
    
    
    if image_response.status_code == 200:
        # Save the image
        with open(path, "wb") as file:
            file.write(image_response.content)
        print(f"Image downloaded successfully as {path}")
        
        # Try opening the image using PIL
        try:
            img = Image.open(path)
            img.show() 
        except Exception as e:
            print(f"Error opening image: {e}")
    else:
        print(f"Failed to download the image from {image_url}. Status code: {image_response.status_code}")
else:
    print(f"Failed to retrieve the API response. Status code: {response.status_code}")