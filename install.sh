#!/bin/bash

SCRIPT_PATH=/usr/bin/
PROJECT=https://github.com/robo-mobile/pwm_manage
PROJECT_NAME=pwm_manage

set -xe

function service_end_point () {
    
cat > $SCRIPT_PATH/$PROJECT_NAME/run_app.sh <<END
#!/bin/bash

SCRIPT_PATH=$(dirname "$(realpath "$0")")
. "$SCRIPT_PATH/venv/bin/activate"
python3 "$SCRIPT_PATH/app.py"

END

}

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
  sudo rm /etc/systemd/system/$PROJECT_NAME.service
  sudo rm -rf $SCRIPT_PATH$PROJECT_NAME
  sudo systemctl daemon-reload
  echo "removing done!"

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
remove

elif [[ "$1" == "update" ]]; then
update

elif [[ "$1" == "help" ]]; then
help

else
echo "Unexpected argument"
help
fi
