FROM python:3.11.11-alpine

WORKDIR /app

ADD . /app

RUN apk add tesseract-ocr
RUN apk add tesseract-ocr-data-eng

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]