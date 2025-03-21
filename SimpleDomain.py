from Domain import Domain

class SimpleDomain(Domain):
    def __init__(self,a:int,b:int):
        idomain=Domain.intRange(a,b)
        self.domainElements=idomain.domain


    def getComponent(self, index: int):
        return self.compositeElements[0]

    def getLast(self):
        return self.domain[-1]

    def getFirst(self):
        return self.domain[0]
