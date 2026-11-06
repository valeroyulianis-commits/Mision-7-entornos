"""Configuración externa mediante variables de entorno."""

import os
from pathlib import Path

from demanda.calculo import FACTOR_POR_DEFECTO

RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
RUTA_POR_DEFECTO = RAIZ_PROYECTO / "data" / "ventas.csv"


def obtener_factor() -> float:
    """Lee FACTOR_DEMANDA; si no existe, usa el valor por defecto."""
    valor = os.getenv("FACTOR_DEMANDA", str(FACTOR_POR_DEFECTO))
    try:
        factor = float(valor)
    except ValueError:
        raise ValueError(f"FACTOR_DEMANDA debe ser un número, no '{valor}'") from None
    if factor <= 0:
        raise ValueError("FACTOR_DEMANDA debe ser mayor que 0")
    return factor


def obtener_ruta() -> Path:
    """Lee ARCHIVO_VENTAS; si no existe, usa data/ventas.csv del proyecto."""
    return Path(os.getenv("ARCHIVO_VENTAS", str(RUTA_POR_DEFECTO)))
