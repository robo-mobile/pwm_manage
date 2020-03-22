# pwm manage

Это кучка скриптов населена на управление двигателями через  RPI3B

## ROADMAP

- [x] Добавить добавить логирование в journalctl
- [x] Добавить возможность делать использования программного ШИМ
- [x] Добавить подключение по WI-FI
- [x] Добавить тестовый клиент который будет пулять json
- [x] Запилить сервер который будет парсить json
- [x] Сделать установщик скрипта

## Install

```shell script
./pwm.sh help
Usage: pwm.sh  [OPTION]
pwm manager (install|remove|update).
OPTION                   DESCRIPTION
install            install $PROJECT_NAME script
remove             stop and remove $PROJECT_NAME script from your system
update             update $PROJECT_NAME script on your system
help               show help message "
```


Посмотреть статус pwm_manage демона:

```shell script
sudo systemctl status pwm_manage
```


### Static ip to WIFI interface

add  to /etc/dhcpcd.conf
```
interface wlan1
static ip_address=192.168.99.20
static routers=192.168.99.1
static domain_name_servers=8.8.8.8
```
