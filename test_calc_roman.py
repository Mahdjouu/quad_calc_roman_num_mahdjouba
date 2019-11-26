import calc_roman as c

def test_un_symbole_to_valeur():
    assert c.un_symbole_to_valeur("I") == 1
    assert c.un_symbole_to_valeur("V") == 5
    assert c.un_symbole_to_valeur("x") == 10
    assert c.un_symbole_to_valeur("l") == 50
    assert c.un_symbole_to_valeur("C") == 100
    assert c.un_symbole_to_valeur("d") == 500
    assert c.un_symbole_to_valeur("M") == 1000
    assert c.un_symbole_to_valeur("a") == "error"
    assert c.un_symbole_to_valeur("XDGB") == "error"

def test_deux_symboles_to_valeur():
    assert c.deux_symboles_to_valeur("II")==2
    assert c.deux_symboles_to_valeur("vv") ==10
    assert c.deux_symboles_to_valeur("XX") ==20
    assert c.deux_symboles_to_valeur("ll") ==100
    assert c.deux_symboles_to_valeur("CC") ==200
    assert c.deux_symboles_to_valeur("dd") ==1000
    assert c.deux_symboles_to_valeur("MM") ==2000
    assert c.deux_symboles_to_valeur("xd") =="error"
    assert c.deux_symboles_to_valeur("xcvb") =="error"

