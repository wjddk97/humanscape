FROM python:3

WORKDIR /usr/src/app 

COPY requirements.txt ./

RUN pip install -r requirements.txt
RUN python3 manage.py crontab add

COPY . . 

EXPOSE 8000   

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "humanscape.wsgi:application"]