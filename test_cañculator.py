from main import string_calculator
import pytest

def test_string_calculator_vacio():
    assert string_calculator("") == 0

def test_string_calculator_un_numero():
    assert string_calculator("1") == 1

def test_string_calculator_dos_numeros():
    assert string_calculator("1,2") == 3

def test_string_calculator_tres_numeros():
    assert string_calculator("1,2,3") == 6

def test_string_calculator_con_salto_de_linea_1():
    assert string_calculator("1,2,4\n5,6") == 18

def test_string_calculator_con_salto_de_linea_2():
    assert string_calculator("1\n2,3") == 6

def test_string_calculator_delimitador_configurable_1():
    assert string_calculator("//;\n1;3;6;4") == 14

def test_string_calculator_delimitador_configurable_2():
    assert string_calculator("//|\n1|3|6|4") == 14

def test_string_calculator_con_negativos_1():
    with pytest.raises(ValueError) as excinfo:
        string_calculator("1,-3,-6,4")
    assert str(excinfo.value) == "No se permiten negativos: -3, -6"

def test_string_calculator_con_negativos_2():
    with pytest.raises(ValueError) as excinfo:
        string_calculator("1,2,-3,4")
    assert str(excinfo.value) == "No se permiten negativos: -3"
