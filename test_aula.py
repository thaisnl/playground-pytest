import pytest 

def soma_1(numero):
    return int(numero) + 1

def soma(n1, n2):
    return n1 + n2

def test_soma_1():
    assert soma_1(41) == 42

def test_soma_1_numero_como_string():
    assert soma_1("41") == 42

@pytest.mark.parametrize("a, b", [(0,1), (2,3)])
def test_soma_valida(a, b):
    assert soma(a,b) == a + b

@pytest.mark.parametrize("a, b", [("1",0)])
def test_soma_palavras(a, b):
    # dá erro se não levantar exceção
    with pytest.raises(TypeError):
        soma(a,b)

@pytest.fixture
def numero_impar():
     return 1

@pytest.fixture
def numero_par():
   return 2

def test_soma(numero_impar, numero_par):
    assert numero_impar + numero_par == 3