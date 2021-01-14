FROM python:3.8
RUN mkdir /app
WORKDIR /app
ADD . /app/
ENV MYSQL_HOST=dbmysql
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=0satellite0
ENV PATH_FOLDER=/home/daniele
ENV MYSQL_ROOT_PASSWORD=0satellite0
ENV MYSQL_URL=mysql+pymysql://root:0satellite0@dbmysql/
RUN pip install -r requirements.txt
CMD ["python", "build_database.py"]
CMD ["python", "app.py"]
