import pytest
import calc_roman as c

def test_symbole_to_valeur():
    assert c.symbole_to_valeur("I")==1
    assert c.symbole_to_valeur("V")==5
    assert c.symbole_to_valeur("x")==10
    assert c.symbole_to_valeur("l")==50
    assert c.symbole_to_valeur("C")==100
    assert c.symbole_to_valeur("d")==500
    assert c.symbole_to_valeur("M")==1000
    assert c.symbole_to_valeur("a")=="error"
    assert c.symbole_to_valeur("XDGB") == "error"