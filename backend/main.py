from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
import numpy as np
import io

app = FastAPI()


@app.post("/analyze-image/")
async def analyze_image(file: UploadFile = File(...)):
    # 1️⃣ Validate file type
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(
            status_code=400,
            detail="Only JPG and PNG images are supported"
        )

    # 2️⃣ Read image bytes
    image_bytes = await file.read()

    # 3️⃣ Load image with Pillow
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # 4️⃣ Resize image (common ML input size)
    image = image.resize((224, 224))

    # 5️⃣ Convert to NumPy array
    image_array = np.array(image)

    # 6️⃣ Normalize pixel values (0–1)
    image_array = image_array.astype("float32") / 255.0

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "image_shape": image_array.shape,
        "dtype": str(image_array.dtype),
        "min_pixel": float(image_array.min()),
        "max_pixel": float(image_array.max())
    }

