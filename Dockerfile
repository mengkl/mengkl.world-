FROM python:3.10-slim

LABEL MAINTAINER = Mengkl 

#目录
RUN mkdir -p /mengklblog/
WORKDIR /mengklblog/

#python库
COPY requirements.txt /mengklblog/
RUN pip3 install --no-cache-dir -r requirements.txt

#博客源码
COPY mengkl /mengklblog/

WORKDIR /mengklblog/
#启动
CMD ["python3","manage.py","runserver","0.0.0.0:3000"]
