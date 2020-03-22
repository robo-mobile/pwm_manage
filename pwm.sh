#!/bin/bash

SCRIPT_PATH=/usr/bin/
PROJECT=https://github.com/eleutherius/pwm_manage.git
PROJECT_NAME=pwm_manage

function install() {


  cd $SCRIPT_PATH
  sudo git clone $PROJECT
  cd $SCRIPT_PATH$PROJECT_NAME
  sudo python3 -m venv venv
  source venv/bin/activate
  pip install -U pip
  pip install -r requirements.txt

  sudo cp systemd/$PROJECT_NAME.service /etc/systemd/system/

  sudo systemctl daemon-reload
  sudo systemctl start pwm_manage
  sudo systemctl enable pwm_manage
}

function remove() {

  sudo systemctl stop pwm_manage
  sudo systemctl disable pwm_manage
  sudo rm -rf $SCRIPT_PATH$PROJECT_NAME

  sudo systemctl daemon-reload
  sudo systemctl start pwm_manage
  sudo systemctl enable pwm_manage

}

function update() {

  sudo cd $SCRIPT_PATH$PROJECT_NAME
  sudo systemctl stop $PROJECT_NAME
  sleep 5
  git pull
  sudo systemctl start $PROJECT_NAME

}


function help() {

  echo "Usage: pwm.sh  [OPTION]
pwm manager (install|remove|update).
  OPTION                   DESCRIPTION
  install            install $PROJECT_NAME script
  remove             stop and remove $PROJECT_NAME script from your system
  update             update $PROJECT_NAME script on your system
  help               show help message "

}

if [[ "$1" == "install" ]]; then
echo "Installing $PROJECT_NAME ..."
install

elif [[ "$1" == "remove" ]]; then
echo "Removing $PROJECT_NAME ..."

elif [[ "$1" == "help" ]]; then
help

else
echo "Unexpected argument"
help
fi
