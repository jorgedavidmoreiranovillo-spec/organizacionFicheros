import os
import shutil
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

#libreria rich para interfaz de usuario e importaciones

def mostrar_cabecera(consola):
    #titulo principal
    consola.print(Panel("[bold orange] ORGANIZADOR DE CARPETAS [/bold orange]"))

def mostrar_informe(consola, movidos, tamanoTotal, enOrigen, enDestino, historial):
    """construye dos tablas formateadas con un resumen de lo que esta pasando y una lista con los movimientos
        parametros:
            consola:instancia de Console
            motivos: total de archivos movidos
            tamanoTotal:tamaño que ocupan los archivos
            enOrigen: los archivos que quedan en el origen
            enDestino: archivos que estan en el destino
            historial: lista con las descripciones de cada movimiento
    """
    consola.print("\n[bold green]INFORME FINAL[/bold green]")