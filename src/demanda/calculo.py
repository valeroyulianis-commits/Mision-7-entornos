"""Lógica de negocio: cálculo de la demanda prevista (sin lectura de archivos)."""

FACTOR_POR_DEFECTO = 1.1


def estimar_demanda(ventas: list[float], factor: float = FACTOR_POR_DEFECTO) -> float:
    """Devuelve la media de las ventas multiplicada por el factor de crecimiento."""
    if not ventas:
        raise ValueError("No hay ventas para calcular la demanda")
    if any(valor < 0 for valor in ventas):
        raise ValueError("Las ventas no pueden ser negativas")
    if factor <= 0:
        raise ValueError("El factor debe ser mayor que 0")
    return round(sum(ventas) / len(ventas) * factor, 2)
