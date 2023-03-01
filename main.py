#flask is used to make API route
from flask import Flask, request

#CORS is used so that we can send images through browers
from flask_cors import CORS, cross_origin

#tesseract our ML model
import pytesseract as tess


#to handel Image operations
from PIL import Image

#stores our image in local memory
import io

#app will be used to make our POST and GET request routes
app = Flask(__name__)

#CORS for image transfer
CORS(app)

#landing of the api
@app.route("/")
def home():
    return "API is working fine"


#Creating an route that handels our POST request from the frontend i.e image is received here {http://127.0.0.1:7777/upload-image} is our POST request path
@app.route('/upload-image', methods=['POST'])
#calling CORS
@cross_origin()

#function that handles our image operations
def upload_image():
    
    # Get the image data from the POST request
    image_data = request.files.get('image').read()

    
   # Use PIL to load the image from memory
    image = Image.open(io.BytesIO(image_data))

    # Use Tesseract to extract text from the image
    text=tess.image_to_string(image)

    # Send a response back to the client
    return text

#Assigning the port 7777 to the python api
if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=7777)


