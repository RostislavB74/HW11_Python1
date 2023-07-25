from rich.console import Console
from rich.table import Table
from ab_classes_240723_w import AddressBook

table = Table(title="Address Book")

table.add_column("Name", justify="right", style="cyan", no_wrap=True)
table.add_column("Phone", style="magenta")
table.add_column("Birthday", justify="right", style="green")

table.add_row()

console = Console()
console.print(table)
