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
- `uvicorn app.main:app --reload`

Follow the link to the SwaggerUI
* `http://127.0.0.1:8000`

Run the program at
`http://127.0.0.1:8000/doc`
