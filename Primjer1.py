from Relations import Relations
from Domain import Domain
from MutableFuzzySet import MutableFuzzySet
from DomainElement import DomainElement

u=Domain.intRange(1,6)
u2=Domain.combine(u,u)
r1=MutableFuzzySet(u2).set(DomainElement.of([1,1]), 1)\
.set(DomainElement.of([2,2]), 1)\
.set(DomainElement.of([3,3]), 1)\
.set(DomainElement.of([4,4]), 1)\
.set(DomainElement.of([5,5]), 1)\
.set(DomainElement.of([3,1]), 0.5)\
.set(DomainElement.of([1,3]), 0.5)

r2=MutableFuzzySet(u2).set(DomainElement.of([1,1]), 1)\
.set(DomainElement.of([2,2]), 1)\
.set(DomainElement.of([3,3]), 1)\
.set(DomainElement.of([4,4]), 1)\
.set(DomainElement.of([5,5]), 1)\
.set(DomainElement.of([3,1]), 0.5)\
.set(DomainElement.of([1,3]), 0.1)

r3=MutableFuzzySet(u2).set(DomainElement.of([1,1]), 1)\
.set(DomainElement.of([2,2]), 1)\
.set(DomainElement.of([3,3]), 0.3)\
.set(DomainElement.of([4,4]), 1)\
.set(DomainElement.of([5,5]), 1)\
.set(DomainElement.of([1,2]), 0.6)\
.set(DomainElement.of([2,1]), 0.6)\
.set(DomainElement.of([2,3]), 0.7)\
.set(DomainElement.of([3,2]), 0.7)\
.set(DomainElement.of([3,1]), 0.5)\
.set(DomainElement.of([1,3]), 0.5)

r4=MutableFuzzySet(u2).set(DomainElement.of([1,1]), 1)\
.set(DomainElement.of([2,2]), 1)\
.set(DomainElement.of([3,3]), 1)\
.set(DomainElement.of([4,4]), 1)\
.set(DomainElement.of([5,5]), 1)\
.set(DomainElement.of([1,2]), 0.4)\
.set(DomainElement.of([2,1]), 0.4)\
.set(DomainElement.of([2,3]), 0.5)\
.set(DomainElement.of([3,2]), 0.5)\
.set(DomainElement.of([1,3]), 0.4)\
.set(DomainElement.of([3,1]), 0.4)

test1=Relations.isUTimesURelation(r1)
print('r1 je definiran nad UxU? '+str(test1).lower())

test2=Relations.isSymmetric(r1)
print('r1 je simetrična? '+str(test2).lower())

test3=Relations.isSymmetric(r2)
print('r2 je simetrična? '+str(test3).lower())

test4=Relations.isReflexive(r1)
print('r1 je refleksivna? '+str(test4).lower())

test5=Relations.isReflexive(r3)
print('r3 je refleksivna? '+str(test5).lower())

test6=Relations.isMaxMinTransitive(r3)
print('r3 je max-min tranzitivna? '+str(test6).lower())

test7=Relations.isMaxMinTransitive(r4)
print('r4 je max-min tranzitivna? '+str(test7).lower())