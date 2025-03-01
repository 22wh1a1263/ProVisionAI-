from PIL import Image
import io

@app.post("/analyze-image/")
async def analyze_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))  # Convert bytes to an image
        result = process_image(image)  # Ensure process_image() supports PIL images
        return {"description": result}
    except Exception as e:
        return {"error": str(e)}
