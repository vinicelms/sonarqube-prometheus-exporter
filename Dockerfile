FROM python:3.8-alpine
ADD requirements.txt /
ADD core /core
RUN pip install -r requirements.txt
CMD ["python", "core/prometheus_exporter.py"]
