#!/bin/bash
base_python_interpreter=""
project_path=`pwd`

read -p "Python interpreter: " base_python_interpreter
`$base_python_interpreter -m venv env`
source env/bin/activate
pip install -U pip
pip install -r requirements.txt

sed -i "pwm_manage_path~$project_path~g" systemd/pwm_manage.service

sudo ln -s $project_path/systemd/pwm_manage.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl start pwm_manage
sudo systemctl enable pwm_manage
