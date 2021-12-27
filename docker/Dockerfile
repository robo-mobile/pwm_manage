FROM balenalib/i386-ubuntu-python
# RUN install_packages wget git
HEALTHCHECK CMD ["curl", "http://localhost:4500/health"]
COPY . /code/
WORKDIR /code/
# RUN pip3 install -r /code/requirements.txt
# RUN pip3 install  /code/
CMD ["python3" , "./pwm_manage/pwm_manage.py", "start"] 