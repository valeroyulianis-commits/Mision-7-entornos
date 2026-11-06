"""Entrada de datos: lectura y validación del CSV de ventas."""

import csv
from pathlib import Path

COLUMNA = "ventas"


def leer_ventas(ruta: str | Path) -> list[float]:
    """Lee la columna 'ventas' de un CSV y devuelve los valores como números."""
    ruta = Path(ruta)
    if not ruta.is_file():
        raise FileNotFoundError(f"No se encuentra el archivo de ventas: {ruta}")

    with ruta.open(encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if COLUMNA not in (lector.fieldnames or []):
            raise ValueError(f"El CSV debe tener una columna '{COLUMNA}'")

        ventas = []
        for numero_fila, fila in enumerate(lector, start=2):
            texto = (fila[COLUMNA] or "").strip()
            try:
                ventas.append(float(texto))
            except ValueError:
                raise ValueError(
                    f"Valor no numérico en la fila {numero_fila}: '{texto}'"
                ) from None
    return ventas
