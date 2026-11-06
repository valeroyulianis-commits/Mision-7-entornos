import pytest

from demanda.config import obtener_factor
from demanda.datos import leer_ventas


def test_leer_csv_valido(tmp_path):
    archivo = tmp_path / "ventas.csv"
    archivo.write_text("ventas\n10\n20\n30\n", encoding="utf-8")
    assert leer_ventas(archivo) == [10.0, 20.0, 30.0]


def test_csv_solo_cabecera(tmp_path):
    archivo = tmp_path / "vacio.csv"
    archivo.write_text("ventas\n", encoding="utf-8")
    assert leer_ventas(archivo) == []


def test_valor_no_numerico(tmp_path):
    archivo = tmp_path / "ventas.csv"
    archivo.write_text("ventas\n10\nabc\n", encoding="utf-8")
    with pytest.raises(ValueError, match="fila 3"):
        leer_ventas(archivo)


def test_archivo_inexistente(tmp_path):
    with pytest.raises(FileNotFoundError):
        leer_ventas(tmp_path / "no_existe.csv")


def test_factor_desde_variable_de_entorno(monkeypatch):
    monkeypatch.setenv("FACTOR_DEMANDA", "1.5")
    assert obtener_factor() == 1.5


def test_factor_de_entorno_invalido(monkeypatch):
    monkeypatch.setenv("FACTOR_DEMANDA", "abc")
    with pytest.raises(ValueError, match="FACTOR_DEMANDA"):
        obtener_factor()
