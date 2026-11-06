import pytest

from demanda.calculo import estimar_demanda


def test_caso_normal():
    assert estimar_demanda([10, 20, 30]) == 22.0


def test_factor_personalizado():
    assert estimar_demanda([10, 20, 30], factor=2) == 40.0


def test_lista_vacia():
    with pytest.raises(ValueError, match="No hay ventas"):
        estimar_demanda([])


def test_ventas_negativas():
    with pytest.raises(ValueError, match="negativas"):
        estimar_demanda([10, -5, 20])


@pytest.mark.parametrize("factor", [0, -1])
def test_factor_invalido(factor):
    with pytest.raises(ValueError, match="factor"):
        estimar_demanda([10, 20], factor=factor)
