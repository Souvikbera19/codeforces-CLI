from rich.console import Console
from rich.table import Table
from .api import get_user_info, get_user_contest, mashup_ques ,solved_problem

console = Console()


def profile(handle: str):
    data = get_user_info(handle)

    table = Table(title="Codeforces Profile")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="magenta")

    table.add_row("Handle", data["handle"])
    table.add_row("Rank", data.get("rank", "Unrated"))
    table.add_row("Rating", str(data.get("rating", "Unrated")))
    table.add_row("Max Rating", str(data.get("maxRating", "-")))

    console.print(table)


def contests(handle: str):
    contests = get_user_contest(handle)

    table = Table(title="Recent Contests")

    table.add_column("Contest")
    table.add_column("Rank")
    table.add_column("Old Rating")
    table.add_column("New Rating")

    for c in contests[-10:]:
        table.add_row(
            c["contestName"],
            str(c["rank"]),
            str(c["oldRating"]),
            str(c["newRating"]),
        )

    console.print(table)


def mashup(handle1:str,handle2:str,rating:int):
    mashupQuestion = mashup_ques(handle1,handle2,rating)
    if mashupQuestion:
        console.print(f"[bold green]Mashup Problem:[/bold green] {mashupQuestion}")
    else:
        console.print("[red]No problem found[/red]")
