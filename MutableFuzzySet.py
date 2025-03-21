from DomainElement import DomainElement
from IFuzzySet import IFuzzySet
from IDomain import IDomain

class MutableFuzzySet(IFuzzySet):
    def __init__(self,domain:IDomain):
        super().__init__(domain)
        self.memberships=[0.0 for i in range(self.getDomain().getCardinality())]

    def getValueAt(self,domainElement:DomainElement):
        if domainElement is not None:
            index=self.getDomain().indexOfElement(domainElement)
            if index>-1:
                return self.memberships[index]
            print('Za zadani element nema vrijednosti!')
            return -1
        else:
            print('Element domene mora biti zadan!')
            exit(1)

    def set(self,e:DomainElement,mu:float):
        if e is not None:
            if mu>=0 and mu<=1:
                index=self.getDomain().indexOfElement(e)
                if index>-1:
                    self.memberships[index]=mu
                    return self
            else:
                print('Krivo zadan mu!')
                exit(1)
        else:
            print('Element domene mora biti zadan!')
            exit(1)


