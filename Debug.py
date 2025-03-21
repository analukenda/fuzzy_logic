import string
from IFuzzySet import IFuzzySet
from IDomain import IDomain

def ispis_1(domain:IDomain,headingText:string):
    if headingText is not None:
        print(headingText)
    for e in domain:
        print('Element domene: '+str(e))
    print('Kardinalitet domene je: '+str(domain.getCardinality()))
    print()

def ispis_2(iFuzzySet:IFuzzySet,headingText:string):
    if headingText is not None:
        print(headingText)
    for e in iFuzzySet.getDomain():
        print('d('+str(e)+')='+"{value:.6f}".format(value=iFuzzySet.getValueAt(e)))
    print()