# AI-Smart-Image-Identifier
This project builds a simple web based  AI smart image identifier in a python environment incorporating TensorFlow  ML framework  for training the model, Pillow and Numpy python libraries for loading/saving images and  for multidimensional array processing respectively. The model receives an uploaded image and interpret it. FastAPI is employed.
Uvicorn - an ASGI web server implementation for Python is used to run the code versioned SMImgID Backend-Part One. Uvicorn is a minimal low-level server/application interface for async frameworks. To run the code cd into the backend directory where the main.py and model.py files reside.
Run it:
python -m uvicorn main:app --reload (or just) uvicorn main:app

To test in browser where image uploading is now possible, run:
http://127.0.0.1:8000/docs
