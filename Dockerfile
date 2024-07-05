# Use an official Python runtime as a parent image
FROM python:3.9-slim

ENV HOST 0.0.0.0

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY requirement.txt ./

# Install any dependencies specified in requirements.txt
RUN pip install -r requirement.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the Flask port
EXPOSE 5000

# Expose the Streamlit port
EXPOSE 8501

# Command to run both Flask and Streamlit
CMD ["sh", "-c", "flask --app app_api.py run & streamlit run mainpage.py"]