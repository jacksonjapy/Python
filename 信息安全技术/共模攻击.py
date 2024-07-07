import gmpy2

if __name__ == '__main__':
    e1 = 65537
    e2 = 123123
    n = 85999854958767959554784116688332018521455063421943587755368471383304578228792567660774571877905741286056067289890541571091855908678849916185854888968821607814818640208047279995507161148266054523381304011525647728747707818431001911666953029766636074021720647966519758884392967535424552761111268097116111462901
    c1 = 9433143107026358064391515635964202417308876133890005758988889931862218290781054744707379577326012522458662286597332929605122824536562485647300105455627793954094295846653031256284325264604759686045656307275756794396697873867363469305371738498084775601501173822178589694803568115145678280724873047855524442385
    c2 = 42446857502457030112230146270021298111025798717943720761082326671733270594681259539969045440718063967428503620991186621408906241321633523187251528315149722016740488445095537099063668916419127271324939716734085315365160642297644233070839887445518800006824122942167475395816587702204864436693519262350299925121
    s = gmpy2.gcdext(e1, e2)
    s1 = s[1]
    s2 = s[2]
    m = gmpy2.powmod(c1, s1, n) * gmpy2.powmod(c2, s2, n)%n
    print(bytes.fromhex(hex(m)[2:]))