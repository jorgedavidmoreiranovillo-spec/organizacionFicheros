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
    
    #tabla de movimientos
    consola.print("\n[bold pink]MOVIMIENTOS REALIZADOS[/bold pink]")
    tabla_historial = Table(show_header = True, header_style = "bold blue")
    tabla_historial.add_column("Nº", justify= "right", style="cyan")
    tabla_historia.add_column("DETALLE DEL MOVIMIENTO", style="white")
    
    for i, movimiento in enumerate(historial, start=1):
        tabla_historial.add_row(str(i), movimiento)
    
    consola.print(tabla_historial)

    #funciones basicas de calculo y manejo de datos

def obtenerExtension (nombreArchivo):
    """
    devuelve la extension de un archivo en minuscuulas y sin el punto.
    si no existe extension te dice 'sin_extension'
    """
    _, ext = os.path.splitext(nombreArchivo)
    if not ext:
        return"sin_extension"
    return ext[1:].lower()

def comprobar(rutaA, rutaB):
    """mira si una ruta esta dentro de otra o si son iguales"""
    asb_a =os.path.abspath(rutaA)+ os.sep
    asb_b =os.path.abspath(rutaB)+ os.sep

    return abs_a.startwith(abs_b) or asb_b.startwith(abs_a)