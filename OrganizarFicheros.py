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
    _, ext = os.path.splitext(nombreArchivo)
    if not ext:
        return"sin_extension"
    return ext[1:].lower()
    """
    devuelve la extension de un archivo en minuscuulas y sin el punto.
    si no existe extension te dice 'sin_extension'
    """

def comprobar(rutaA, rutaB):
    asb_a =os.path.abspath(rutaA)+ os.sep
    asb_b =os.path.abspath(rutaB)+ os.sep

    return abs_a.startwith(abs_b) or asb_b.startwith(abs_a)
    """mira si una ruta esta dentro de otra o si son iguales"""

def nombreDisponible(rutaDestino, nombreArchivo):
    nombreBase, extension = os.path.splitext(nombreArchivo)
    candidato = nombreArchivo
    contador = 1

    while os.path.exists(os.path.join(rutaDestino, candidato)):
        candidato = f"{nombreBase}_{contador}{extension}"
        contador += 1
    return candidato
    """busca un nombre libre si el archivo ya exsiste"""

def clasificarArchivo (rutaOrigen, nombreArchivo, rutaDestino, historial):

    ext = obtenerExtension(nombreArchivo)
    subcarpeta = os.path.join(rutaDestino, ext)

    os.makedirs(subcarpeta, exist_ok=True)
    nombreLibre = nombreDisponible (subcarpeta, nombreArchivo)

    origenC= os.path.join(rutaOrigen, nombreDisponible)
    destinoC= os.path.join(subcarpeta, nombreLibre)
    #mover el archivo fisicamente
    shutil.move(origenC, destinoC)

    #modificacion del objeto original
    historial.append(f"{origenC} -> {subcarpeta}/ {nombreLibre}")
    """mueve un archivo a su subcarpeta y agrega un registro a una lista 'historial'"""

#funciones recursivas

def clasificarCarpetaR (rutaOrigen, rutaDestino, historial):

    for elemento in os.listdir(rutaOrigen):
        rutaElemento = os.path.join(rutaOrigen, elemento)

    #caso recursivo: si es una subcarpeta se vuelve a llamar
    if os.path.isdir(rutaElemento):
        clasificarCarpetaR(rutaElemento, rutaDestino, historial)

    #caso base: si es un archivo se clasifica
    elif os.path.isfile(rutaElemento): 
        clasificarArchivo(rutaOrigen, elemento, rutaDestino, historial)

    """recorre la carpeta origen y subcarpetas de manera recursiva

        elementos:
        cuando el bucle for recorre una carpeta que solo contiene archivos, los procesa y el bloque termina

        cuando encuentra una subcarpeta, la funcion se autollama y le pasa uuna nueva carpeta
    """
    
def contarArchivosrecursivos(ruta):
    if not os.path.exists(ruta) or not os.path.isdir(ruta):
        return 0

    totalArchivos = 0
    for elemento in os.listdir (ruta):
        rutaElemento = os.path.join(ruta, elemento)

        #caso recursivo
        if os.path.isdir(rutaElemento):
            totalArchivos += contarArchivosrecursivos (rutaElemento)
        
        #caso base
        elif os.path.isdir(rutaElemento):
            totalArchivos += 1

    return totalArchivos
    """
        cuenta recursivamente los archivos que hay en una ruta y sus subcarpetas
    """

#programa como tal

def main():
    consola = Console()
    mostrarCabecera (consola)

    origen = Prompt.ask("[bold blue]Introduce la carpeta de origen[/bold blue]")
    destino = Prompt.ask("[bold blue]Introduce la carpeta de destino[/bold blue]")
    #entrada de datos con rich

#control de errores

    if not os.path.exists(origen) or not os.path.isdir(origen):
        consola.print(Panel("la ruta de origen no existe o no es una carpeta", border_style = "red"))
        return

    if os.path.exists(destino) and not os.path.isdir(destino):
        consola.print(Panel("la ruta de destino no es una carpeta", border_style = "red"))
        return

    if comprobar(origen, destino):
        consola.print(Panel("la ruta de origen y destino no pueden ser iguales o estar dentro una de otra", border_style = "red"))
        return

    historial = [] #lista para almacenar los movimientos realizados

    clasificarCarpetaR(origen, destino, historial) #llamada a la funcion recursiva principal
    consola.print ("\n[bold green]clasificación completada[/bold green]")