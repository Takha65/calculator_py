# test_utils.py
from utils import add

def test_add():
    """
    Teste la fonction add avec quelques valeurs.
    """
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0