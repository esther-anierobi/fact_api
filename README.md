# Welcome To FastAPI with an External Cat Fact API
This project is a simple fastapi python project that integrates an external cat fact api. 
It sends requests to factcat api returns at random.

#### Below is steps on how to run this project
In your terminal:
- Clone the project
  * `git clone https://github.com/esther-anierobi/me.git`
  * `cd me`
- Create a python virtual environment
  * `python -m venv py_venv`
- Activate the virtual environment <br>
  For macO/linux
  * `source .py_venv/bin/activate` <br>
  For windows 
  * `.venv\Scripts\activate.bat`

Once activated, Run the app using
- `uvicorn main:app --host 0.0.0.0 --port 8000`

Follow the link to the SwaggerUI
* `http://0.0.0.0:8000/docs`

Run the program at
`http://0.0.0.0:8000/docs`
