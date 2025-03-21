from IDomain import IDomain
from DomainElement import DomainElement

class Domain(IDomain):
    def intRange(a:int,b:int):
        if a>=b:
            print('Granice domene neispravno postavljene!')
            exit(1)
        idomain=IDomain()
        idomain.domainElements=[DomainElement([i]) for i in range(a,b)]
        idomain.compositeElements=[idomain]

        return idomain

    def combine(domain_1:IDomain,domain_2:IDomain):
        if domain_1 is None or domain_2 is None:
            print('Nemoguce kombinirati praznu domenu!')
            exit(1)
        new_domain=[]
        for element_1 in domain_1:
            for element_2 in domain_2:
                new_domain.append(DomainElement(element_1.values+element_2.values))
        idomain=IDomain()
        idomain.domainElements=new_domain
        idomain.compositeElements=[domain_1,domain_2]

        return idomain





