"""
It's a simple script to set up ipmp server
"""
import typer
from .default_config import *
import toml

from . import *

app = typer.Typer(help="Awesome CLI IPMP universal tool.")


conf="config.toml"

def init_config():
    """
    Create redundancy.toml config file

    Example of using:
    redundancy init
    """
   

    import os.path
    if os.path.isfile(conf):
        print ("Config file already exists")
        pass
    if not os.path.isfile(conf):
        print (f"Generate {conf} config file")
        with open(conf, 'w') as f:
            f.write(def_config)

try:   
    config = toml.load(conf)
except: 
    print (f"File {conf} not exist!")

app = typer.Typer(help="Awesome CLI redundancy universal tool.")

@app.command()
def init():
    """
    Create redundancy.toml config file

    Example of using:
    redundancy init
    """
    init_config()


@app.command()
def start(conf: str = typer.Option("/etc/pwm/config.toml", help="PWM config.", show_default=True)
             ):
    """
    Use for the start PWM manager 

    Example of using:
    pwm start --conf=/etc/pwm/config.toml
    """
    print ('hello') 


if __name__ == '__main__':
    app()
