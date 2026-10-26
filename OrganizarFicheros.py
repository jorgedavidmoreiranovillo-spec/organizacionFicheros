import os
import shutil
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

#libreria rich para interfaz de usuario e importaciones

def mostrar_cabecera(consola):
    #titulo principal
    consola.print(Panel("[bold orange] ORGANIZADOR DE CARPETAS[/bold orange]"))

    