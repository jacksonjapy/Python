import gmpy2


class ContinuedFraction():
    def __init__(self, numerator, denumerator):
        self.numberlist = []
        self.fractionlist = []
        self.GenerteteNumberList(numerator, denumerator)
        self.GenerteFractionList()
        pass

    def GenerteteNumberList(self, numerator, denumerator):
        while numerator != 1:
            quotinet = numerator // denumerator
            remainder = numerator % denumerator
            self.numberlist.append(quotinet)
            numerator = denumerator
            denumerator = remainder

    def GenerteFractionList(self):
        self.fractionlist.append([self.numberlist[0], 1])
        for i in range(1, len(self.numberlist)):
            numerator = self.numberlist[i]
            denumerator = 1
            for j in range(i):
                temp = numerator
                numerator = denumerator + numerator * self.numberlist[i - j - 1]
                denumerator = temp
            self.fractionlist.append([numerator, denumerator])


n = 107820827895585003318160075938897995007771726056433792260306646508197614885172767297860713228269372581388675047053081480259665212535577590049118106812907146179205072239202195537073770739125675017748544703407492971258729480561817875290145208304790655494183395710284259904924825216130329385053835448236320458029
e = 89522445598733261357901825227079909455833500144157754746488199484282356592752881911539250096606592386991876444930791131091191645729189063282738620740478951554538143425376616935272546647795666042057430492362510853442637374299569781152667997525016908056524464220471765404748627571107144931587704935347192130747
c = 78801382956240362099621219179273906545911347424992980739524362075033074146925440259224069602152252908929563712955805750439181009392136772144489054854771121558867343856732335266122392680114047445081029206150709456363766540038033883249133391765001168831795492173604819457970972375924518104751091565565160890627
a = ContinuedFraction(e, n)
for k, d in a.fractionlist:
    m = gmpy2.powmod(c, d, n)
    try:
        print(bytes.fromhex(hex(m)[2:]).decode())
    except Exception:
        pass
