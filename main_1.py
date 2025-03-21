from Domain import Domain
from DomainElement import DomainElement
import Debug

d1=Domain.intRange(0,5)
Debug.ispis_1(d1,'Elementi domene d1:')
d2=Domain.intRange(0,3)
Debug.ispis_1(d2,'Elementi domene d2:')
d3=Domain.combine(d1,d2)
Debug.ispis_1(d3,'Elementi domene d3:')
print(d3.elementForIndex(0))
print(d3.elementForIndex(5))
print(d3.elementForIndex(14))
print(d3.indexOfElement(DomainElement.of([4,1])))


