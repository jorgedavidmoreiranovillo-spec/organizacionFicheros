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
    
    #tabla1 resumen del proceso
    tabla_resumen = Table( show_header = True, header_style = "bold blue")
    tabla.add_column("CONCEPTO", style="bold white")
    tabla.add_column("VALOR", justify="right")
    
    tabla.add_row("Archivos movidos", str(movidos))
    
    
    if en_origen ==0: 
        estilo_origen = "bold green"
    else:
        "bold red" 
    tabla.add_row("ARCHIVOS QUE QUEDAN EN ORIGEN", f"[{estilo_origen}]{en_origen}[/estilo_origen]")
    tabla.add_row("ARCHIVOS DE DESTINO", str(en_destino))
    
    consola.print(tabla)    