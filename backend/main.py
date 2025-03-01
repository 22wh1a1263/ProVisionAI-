from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from PIL import Image
import numpy as np

app = FastAPI()

# Allow CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze-image/")
async def analyze_image(file: UploadFile = File(...)):
    try:
        # Read image
        contents = await file.read()
        image = Image.open(BytesIO(contents))
        
        # Convert to NumPy array for processing
        image_array = np.array(image)
        height, width, channels = image_array.shape
        
        # Example analysis: Return image dimensions and format
        return {
            "filename": file.filename,
            "format": image.format,
            "size": {"width": width, "height": height},
            "channels": channels,
        }
    except Exception as e:
        return {"error": str(e)}
