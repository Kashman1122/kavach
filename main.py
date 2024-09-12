from fastapi import FastAPI, File, UploadFile, Form
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

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")


# Function to get response from model
def get_data(question: str, image: Image.Image):
    if question and image is not None:
        # You may need to convert the image into a format that the model can accept,
        # if required (this depends on the generative model's API specs).
        response = model.generate_content([question, image])
        return response.text
    return "No response"


# API endpoint to accept image and question and Language choice
@app.post("/analyze-image/")
async def analyze_image(question: str = Form(...), file: UploadFile = File(...),language_choice: str = Form(...)):
    try:
        # Read the image file
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))

        # Get AI response
        response = get_data("which disease do you detect in the provided leaf or crop and provide solution to prevent it Please respond in {language_choice}.", image)

        # Return the AI response as JSON
        return JSONResponse(content={"response": response})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Define the main function to run the FastAPI app
if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8000))  # Render assigns a port via PORT environment variable
    uvicorn.run(app, host="0.0.0.0", port=port)
