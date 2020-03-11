FROM python:3
ADD facegenerated.py /


RUN pip3 install requests
CMD ["pyhton","./facegenerated.py"]