"""Punto de entrada: une configuración, lectura y cálculo."""

import sys

from demanda.calculo import estimar_demanda
from demanda.config import obtener_factor, obtener_ruta
from demanda.datos import leer_ventas


def main() -> int:
    try:
        ruta = obtener_ruta()
        factor = obtener_factor()
        ventas = leer_ventas(ruta)
        demanda = estimar_demanda(ventas, factor)
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Archivo: {ruta}")
    print(f"Registros: {len(ventas)} · Factor: {factor}")
    print(f"Demanda prevista: {demanda}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
