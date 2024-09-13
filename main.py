# from fastapi import FastAPI, File, UploadFile, Form
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse
# from PIL import Image
# import io
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai
# import uvicorn

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Initialize the FastAPI app
# app = FastAPI()
# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:52436/","http://localhost:55425/"],  # Adjust this to specify which domains are allowed
#     allow_credentials=True,
#     allow_methods=["GET","POST"],  # Adjust this to specify allowed methods
#     allow_headers=["Content-Type","Authorization"],  # Adjust this to specify allowed headers
# )
# # Initialize the model
# model = genai.GenerativeModel("gemini-1.5-flash")


# # Function to get response from model
# def get_data(question: str, image: Image.Image):
#     if question and image is not None:
#         try:
#             buffered=io.BytesIO()
#             image.save(buffered,format="PNG")
#             image_bytes=buffered.getvalue()
#             # You may need to convert the image into a format that the model can accept,
#             # if required (this depends on the generative model's API specs).
#             response = model.generate_content([question, image])
#             return response.text
#         except Exception as e:
#             return f"Error in get_data: {str(e)}"
#     return "No response"


# # API endpoint to accept image, question, and language choice
# @app.post("/analyze-image/")
# async def analyze_image(question: str = Form(...), language_choice: str = Form(...), file: UploadFile = File(...)):
#     try:
#         # Read the image file
#         image_data = await file.read()
#         image = Image.open(io.BytesIO(image_data))

#         # Format the question with the language choice using f-string
#         formatted_question = f"Which disease do you detect in the provided leaf or crop and provide a solution to prevent it? Please respond in {language_choice}."

#         # Get AI response
#         response = get_data(formatted_question, image)

#         # Return the AI response as JSON
#         return JSONResponse(content={"response": response})

#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)


# # Define the main function to run the FastAPI app
# if __name__ == "__main__":
#     import os
#     port = int(os.getenv("PORT", 8000))  # Render assigns a port via PORT environment variable
#     uvicorn.run(app, host="0.0.0.0", port=port)

















from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image
import io
import os
from dotenv import load_dotenv
import google.generativeai as genai
import uvicorn

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:52981","http://34.82.30.12:0","http://106.221.85.7:0","http://localhost:52436", "http://localhost:55425","http://localhost:65019","http://localhost:49366","http://35.233.246.44:0","http://42.105.73.61:0","http://42.105.73.74:0","http://106.221.85.7:0","http://35.203.181.120:0","http://127.0.0.1:39730"],  # Allowed origins
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Allow only GET and POST methods
    allow_headers=["Content-Type", "Authorization"],  # Allow specific headers
)

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get response from model
def get_data(question: str, image: Image.Image):
    if question and image is not None:
        try:
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            image_bytes = buffered.getvalue()
            # Generate response using the model
            response = model.generate_content([question, image])
            return response.text
        except Exception as e:
            return f"Error in get_data: {str(e)}"
    return "No response"

# API endpoint to accept image, question, and language choice
@app.post("/analyze-image/")
async def analyze_image(question: str = Form(...), language_choice: str = Form(...), file: UploadFile = File(...)):
    try:
        # Read the image file
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))

        # Format the question with the language choice using f-string
        formatted_question = f"Which disease do you detect in the provided leaf or crop and provide a solution to prevent it? Please respond in {language_choice}."

        # Get AI response
        response = get_data(formatted_question, image)

        # Return the AI response as JSON
        return JSONResponse(content={"response": response})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


# Define the main function to run the FastAPI app
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Render assigns a port via PORT environment variable
    uvicorn.run(app, host="0.0.0.0", port=port)




























# from fastapi import FastAPI, File, UploadFile, Form
# from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware
# from PIL import Image
# import io
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai
# import uvicorn

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Initialize the FastAPI app
# app = FastAPI()

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust this to specify which domains are allowed
#     allow_credentials=True,
#     allow_methods=["*"],  # Adjust this to specify allowed methods
#     allow_headers=["*"],  # Adjust this to specify allowed headers
# )

# # Initialize the model
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Function to get response from model
# def get_data(question: str, image: Image.Image):
#     try:
#         # Convert image to bytes if required
#         buffered = io.BytesIO()
#         image.save(buffered, format="PNG")
#         image_bytes = buffered.getvalue()
        
#         # Generate response using the model
#         response = model.generate_content([question, image_bytes])
#         return response.text
#     except Exception as e:
#         return f"Error in get_data: {str(e)}"

# # API endpoint to accept image, question, and language choice
# @app.post("/analyze-image/")
# async def analyze_image(question: str = Form(...), file: UploadFile = File(...), language_choice: str = Form(...)):
#     try:
#         # Read and process the image file
#         image_data = await file.read()
#         image = Image.open(io.BytesIO(image_data))

#         # Format the question with the language choice
#         formatted_question = f"{question} Please respond in {language_choice}."

#         # Get AI response
#         response = get_data(formatted_question, image)

#         # Return the AI response as JSON
#         return JSONResponse(content={"response": response})

#     except Exception as e:
#         # Return a JSON response with error details
#         return JSONResponse(content={"error": str(e)}, status_code=500)

# # Define the main function to run the FastAPI app
# if __name__ == "__main__":
#     port = int(os.getenv("PORT", 8000))  # Render assigns a port via PORT environment variable
#     uvicorn.run(app, host="0.0.0.0", port=port)

