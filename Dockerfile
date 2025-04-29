# ✅ Using Python 3.13-alpine (good!)
FROM python:3.13-alpine

# ✅ Set PYTHONUNBUFFERED for immediate output
ENV PYTHONUNBUFFERED=1

# ✅ Create a working directory
RUN mkdir /code


# ✅ Set the working directory
WORKDIR /code

# ✅ Copy requirements first (for caching)
COPY requirements.txt /code/

# ✅ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# ✅ Copy the rest of the application code
COPY . .

RUN chmod +x /code/start-django.sh

# ✅ Expose the port the app runs on
EXPOSE 8000

# ✅ Run the Django development server (or your production setup)
CMD ["/code/start-django.sh"]

