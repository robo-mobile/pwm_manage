Script for set up robot-platform
================================

This playbook installs and configures all necessary software:

- Update packages
- Installs base system packages
- Configures user profile settings (.bashrc, .tmux.conf, .bash_aliases)

## Installation

  1. [Install Ansible](http://docs.ansible.com/intro_installation.html) on the
     local machine.
  2. Clone this repository to your local drive.
  3. Add required servers to the inventory file **inventory.yml**.
  4. Add SSH public key to servers which will be used by Ansible (run on the
     remote server):
```$ su - root
ssh_public_key="content of the public SSH key"
mkdir /root/.ssh && chmod 700 /root/.ssh
echo "$ssh_public_key" >> /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
```
  5. Add/change specific variables in the **config.yml**.
  6. Be sure that pip3 or pip command is available on the local machine.
  7. Run `ansible-playbook main.yml -v` inside this directory to provison
     a server or group of servers.

## Deploy latest version of python packages

Run `ansible-playbook -i inventory.yml main.yml -v --tags upgrade`

> Note: fully tested on Raspbian OS distribution.