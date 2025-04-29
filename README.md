# How to start the Application
Highly recomended to use virtual environment

### `pip install -r requirements.txt`
### To run the test you should use `pytest`
### To see the coverage, use pytest coverage plug-in,  `pytest -cov` 
### If you need to see the report in HTML `coverage html`
### To build  the docker image `docker build -t my-app:latest .`        
### To run the docker file  `docker run -d -p 8000:8000      my-app:latest`            
### To monitor the processes `docker ps`
### Port http://0.0.0.0:8000/docs to manipulate           
### To run locally, use `uvicorn main:app --reload`
