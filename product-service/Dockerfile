# set base image (host OS)
FROM python

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt
RUN pip install Flask-SQLAlchemy

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "./app.py" ]
