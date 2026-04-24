import pytest

def cubo(x):
    return x * x * x

@pytest.mark.parametrize("entrada_x, resultado_esperado", [
    (0, 0),       
    (1, 1),       
    (2, 8),       
    (-2, -8),     
    (10, 1000)    
])
def test_cubo_parametrizado(entrada_x, resultado_esperado):
    assert cubo(entrada_x) == resultado_esperado
