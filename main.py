import typer
from cfcli.commands import profile, contests ,mashup

app = typer.Typer()


@app.command()
def user(handle: str):
    """Show Codeforces profile"""
    profile(handle)


@app.command()
def history(handle: str):
    """Show contest history"""
    contests(handle)

@app.command()
def mashupQuestion(handle1:str,handle2:str,rating:int):
    mashup(handle1,handle2,rating)

if __name__ == "__main__":
    app()