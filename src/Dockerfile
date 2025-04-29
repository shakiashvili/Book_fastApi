FROM python:3.9
# Set working directory
WORKDIR /src
# Coping requirements
COPY requirements.txt requirements.txt
# Installing requirements
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py /src/
COPY model.py /src/  
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host","0.0.0.0","--port","8000"]