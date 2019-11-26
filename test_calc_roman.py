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

def test_deux_symboles_identiques_to_valeur():
    assert c.deux_symboles_identiques_to_valeur("II") == 2
    assert c.deux_symboles_identiques_to_valeur("vv") == 10
    assert c.deux_symboles_identiques_to_valeur("XX") == 20
    assert c.deux_symboles_identiques_to_valeur("ll") == 100
    assert c.deux_symboles_identiques_to_valeur("CC") == 200
    assert c.deux_symboles_identiques_to_valeur("dd") == 1000
    assert c.deux_symboles_identiques_to_valeur("MM") == 2000
    assert c.deux_symboles_identiques_to_valeur("xd") == "error"
    assert c.deux_symboles_identiques_to_valeur("xcvb") == "error"

def test_n_symboles_identiques_to_valeur():
    assert c.n_symboles_identiques_to_valeur("III")==3
    assert c.n_symboles_identiques_to_valeur("VVVV")==20
    assert c.n_symboles_identiques_to_valeur("XXX")==30
    assert c.n_symboles_identiques_to_valeur("LLL")==150
    assert c.n_symboles_identiques_to_valeur("CCCCC")==500
    assert c.n_symboles_identiques_to_valeur("DDDDDD")==3000
    assert c.n_symboles_identiques_to_valeur("MMMMMMMMMM")==10000
    assert c.n_symboles_identiques_to_valeur("XCIV")=="error"
    assert c.n_symboles_identiques_to_valeur("absrt")=="error"