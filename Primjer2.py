
from Domain import Domain
from DomainElement import DomainElement

from MutableFuzzySet import MutableFuzzySet
from Relations import Relations

u1=Domain.intRange(1,5)
u2=Domain.intRange(1,4)
u3=Domain.intRange(1,5)
r1=MutableFuzzySet(Domain.combine(u1,u2)).set(DomainElement.of([1,1]), 0.3)\
.set(DomainElement.of([1,2]), 1)\
.set(DomainElement.of([3,3]), 0.5)\
.set(DomainElement.of([4,3]), 0.5)

r2=MutableFuzzySet(Domain.combine(u2,u3)).set(DomainElement.of([1,1]), 1)\
.set(DomainElement.of([2,1]), 0.5)\
.set(DomainElement.of([2,2]), 0.7)\
.set(DomainElement.of([3,3]), 1)\
.set(DomainElement.of([3,4]), 0.4)

r1r2=Relations.compositionOfBinaryRelations(r1,r2)

for e in r1r2.getDomain():
    print('mu('+str(e)+')='+str(r1r2.getValueAt(e)))
