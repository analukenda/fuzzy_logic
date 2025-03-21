from Domain import Domain
from Relations import Relations
from DomainElement import DomainElement
from MutableFuzzySet import MutableFuzzySet

u=Domain.intRange(1,5)
r=MutableFuzzySet(Domain.combine(u,u)).set(DomainElement.of([1,1]), 1)\
.set(DomainElement.of([2,2]), 1)\
.set(DomainElement.of([3,3]), 1)\
.set(DomainElement.of([4,4]), 1)\
.set(DomainElement.of([1,2]), 0.3)\
.set(DomainElement.of([2,1]), 0.3)\
.set(DomainElement.of([2,3]), 0.5)\
.set(DomainElement.of([3,2]), 0.5)\
.set(DomainElement.of([3,4]), 0.2)\
.set(DomainElement.of([4,3]), 0.2)

r2=r

print('Početna relacija je neizrazita relacija ekvivalencije? '+str(Relations.isFuzzyEquivalence(r2)).lower())
print()
for i in range(1,4):
    r2=Relations.compositionOfBinaryRelations(r2,r)
    print('Broj odrađenih kompozicija: '+str(i)+'. Relacije je:')
    for e in r2.getDomain():
        print('mu('+str(e)+")={value:.1f}".format(value=r2.getValueAt(e)))
    print('Ova relacije je relacija ekvivalencije? '+str(Relations.isFuzzyEquivalence(r2)).lower())
    print()