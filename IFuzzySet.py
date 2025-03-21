from abc import ABC
from IDomain import IDomain
from DomainElement import DomainElement

class IFuzzySet(ABC):
    def __init__(self,domain:IDomain):
        if domain is not None:
            self.domain=domain
        else:
            print('Domena mora biti zadana!')
            exit(1)

    def getDomain(self):
        return self.domain

    def getValueAt(self,domainElement:DomainElement):
        return -1