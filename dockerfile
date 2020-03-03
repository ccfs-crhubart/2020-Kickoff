# comments added more and more
FROM python:3

ADD main.py /
ADD diff.py /
# ADD ssh.py /

RUN pip install pystrich
CMD [ "python", "./main.py" ]
CMD [ "python", "./diff.py" ]
# CMD [ "python", "./ssh.py" ]