#./python/Dockerfile 
FROM python:3.9      

WORKDIR /usr/src/app  

## Install packages 
COPY requirements.txt .        

RUN pip install -r requirements.txt 

## Copy all src files 
COPY . .                       

## Run the application on the port 8000 
EXPOSE 8000

VOLUME . .

## run command
CMD ["python", "./manage.py", "runserver", "--host=0.0.0.0", "-p 8000"]