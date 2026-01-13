# ---------------------------------------------------------------
#    Dockerfile (v 2.1)
# ---------------------------------------------------------------


FROM python:3.11-slim


RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set WORKDIR to /code (parent of app) to ensure correct module resolution 
# and log aggregation in Azure Web Apps for Containers.
WORKDIR /code


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY ./app /code/app


EXPOSE 8000


HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]