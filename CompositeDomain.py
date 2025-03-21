from Domain import Domain
from SimpleDomain import SimpleDomain
from IDomain import IDomain

class CompositeDomain(Domain):
    def __init__(self, compositeElements):
        try:
            if len(compositeElements)<2:
                print('Moraju bit zadane bar dvije domene za kompozitnu!')
                exit(1)
            for element in compositeElements:
                if isinstance(element,(IDomain,SimpleDomain)):
                    continue
                else:
                    print('Za kompozit moraju bit zadane jednostavne domene!')
                    exit(1)
            self.compositeElements=compositeElements
            idomain=Domain.combine(compositeElements[0],compositeElements[1])
            for i in range(2,self.getNumberOfComponenst()):
                idomain=Domain.combine(idomain,compositeElements[i])
            self.domainElements=idomain.domainElements
        except TypeError:
            print('Moraju bit zadane bar dvije domene za kompozitnu!')
            exit(1)



