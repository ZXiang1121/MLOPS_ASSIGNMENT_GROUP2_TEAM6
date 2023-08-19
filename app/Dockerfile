FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
WORKDIR /app
COPY . /app
RUN pip3 install Flask
RUN pip install --upgrade pip
RUN apk update && apk add build-base
RUN pip install numpy
RUN pip install --upgrade pip setuptools wheel
RUN pip install pycaret
# RUN conda install bottleneck
# RUN pip install -r requirements.txt
EXPOSE 3000
CMD python ./main.py


