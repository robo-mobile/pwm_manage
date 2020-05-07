"""
It's a simple script to set up ipmp server
"""
import typer

from . import *

app = typer.Typer(help="Awesome CLI IPMP universal tool.")


@app.command()
def addpanel(number: int,
             type: str = typer.Option("pmax", help="type of the panel", show_default=True),
             ip: str = typer.Option("192.168.99.100", help="ip address.", show_default=True)
             ):
    """
    Use for adding panels on you server

    Example of using:
    utool addpanel 100 --type=neo --ip=94.125.123.180

    Support VISONIC panels: PM10, PM30, PM360, PM360R
    Support DSC panels: HS2128, HS2064, HS2032, HS3248, HS3128, HS3064
    """
    creator = PanelsConstructor(ip)
    all_panels = {"pmax": ["PM30", "PM10", "PM360", "PM360R"],
                  "neo": ['HS2128', 'HS2064', 'HS2032', 'HS3248', 'HS3128', 'HS3064']}
    pmax_panels = all_panels.get("pmax")
    neo_panels = all_panels.get("neo")
    if type in all_panels:
        if type == "pmax":
            creator.pmaxPanels(number, model="PM360R")
        elif type == "neo":
            creator.neoPanels(number, model='HS2128')
    elif type in pmax_panels:
        creator.pmaxPanels(number, model=type)
    elif type in neo_panels:
        creator.neoPanels(number, model=type)
    # elif type == "all":
    #     for i in pmax_panels:
    #         creator.pmaxPanels(number, model=i)
    #     for e in neo_panels:
    #         creator.neoPanels(number, model=e)

    else:
        message = typer.style("something wrong", fg=typer.colors.RED, bold=True)
        typer.echo(message)
        typer.echo(f"number = {number}, type = {type}, ip = {ip}")


@app.command()
def addgroup(number: int,
             ip: str = typer.Option("192.168.99.100", help="Ip address.", show_default=True)
             ):
    """
    Use for adding groups on your server.

    Example of using:
    utool addgroup 10 --ip=94.125.123.180
    """
    creator = RestConstructor(ip)
    creator.addGroup(number)


@app.command()
def addcs(number: int,
          ip: str = typer.Option("192.168.99.100", help="Ip address.", show_default=True)
          ):
    """
    Use for adding Central Stations on your server.

    Example of using:
    utool addcs 10 --ip=94.125.123.180
    """
    creator = RestConstructor(ip)
    creator.addCS(number)


@app.command()
def addusers(number: int,
             ip: str = typer.Option("192.168.99.100", help="Ip address.", show_default=True)
             ):
    """
    Use for adding Central Stations on your server.

    Example of using:
    utool adduser 10 --ip=94.125.123.180
    """
    creator = RestConstructor(ip)
    creator.addUsers(number)


@app.command()
def addroles(number: int,
             ip: str = typer.Option("192.168.99.100", help="Ip address.", show_default=True)
             ):
    """
    Use for adding Central Stations on your server.

    Example of using:
    utool addroles 10 --ip=94.125.123.180
    """
    creator = RestConstructor(ip)
    creator.addRoles(number)


if __name__ == '__main__':
    app()
