# Get python 3.7 image
FROM python:3.7.9

# Copy web app foler
COPY . /app
WORKDIR app

# Upgrade pip
RUN pip install -U pip

# Install requirements and dependencies
COPY requirements.txt app/requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -r requirements.txt


# Expose port 8080
EXPOSE 8051

# Run
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8051", "--server.address=0.0.0.0"]