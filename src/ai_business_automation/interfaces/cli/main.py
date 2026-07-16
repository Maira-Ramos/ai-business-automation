import typer

from rich import print

app = typer.Typer(
    help="AI Business Automation"
)


@app.command()
def version():
    print("[green]AI Business Automation v2.0[/green]")


@app.command()
def hello():
    print("[cyan]Projeto iniciado com sucesso![/cyan]")


if __name__ == "__main__":
    app()