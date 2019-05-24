FROM jupyterhub/jupyterhub

WORKDIR /notebook

RUN pip install notebook

ADD adduser.sh /adduser.sh

RUN mkdir /data

RUN bash /adduser.sh