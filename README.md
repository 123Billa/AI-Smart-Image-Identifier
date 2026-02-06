# AI-Smart-Image-Identifier
This project builds a simple web based  AI smart image identifier in a python environment incorporating TensorFlow  ML framework  for training the model, Pillow and Numpy python libraries for loading/saving images and  for multidimensional array processing respectively. The model receives an uploaded image and interpret it. FastAPI is employed.
Uvicorn - an ASGI web server implementation for Python is used to run the code versioned SMImgID Backend-Part One. Uvicorn is a minimal low-level server/application interface for async frameworks. To run the code cd into the backend directory where the main.py and model.py files reside.
Run it:
python -m uvicorn main:app --reload (or just) uvicorn main:app
The following output messages show that the backend server is running properly.  

Application startup complete. This means(=>) uvicorn successfully started your FastAPI app. No startup errors.

GET /docs → 200 OK => browser accessed the Swagger UI at /docs, and the server responded successfully.

GET /openapi.json → 200 OK => Swagger UI requested your OpenAPI schema, and FastAPI generated and returned it correctly.

Bottom line: your backend is running properly, the API is healthy, and the interactive docs are working exactly as expected


To test in browse, run:
http://127.0.0.1:8000/docs
