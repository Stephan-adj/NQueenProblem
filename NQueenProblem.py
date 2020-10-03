# -*- coding: utf-8 -*-
"""
ADJARIAN Stéphan
"""

import random
echec_dim=8

class individu: 
    def __init__(self, val=None):
        if val==None:
            self.val=random.sample(list(range(8)), 8)
        else:
            self.val=val
        self.nbconflict=self.fitness()
                      
    def __str__(self):
        return str(self.val)  
        
    def conflit(p1, p2):
        return p1[1]==p2[1] or p1[0]==p2[0] or abs(p1[0]-p2[0])==abs(p1[1]-p2[1])
    
    def fitness(self):
        """ evaluer l'individu c'est connaitre le nbr de conflit"""
        self.nbconflict=0
        for i in range(echec_dim):
            for j in range(i+1, echec_dim):
                if individu.conflit([i,self.val[i]], [j,self.val[j]]):
                    self.nbconflict+=1
        return self.nbconflict
        
def create_rand_pop(count):
    liste=[]
    for i in range(count+1):
         liste.append(individu())
    return liste
        
def evaluate(pop):
    return sorted(pop, key=lambda x : x.fitness())

def selection(pop,hcount,lcount):
    n=len(pop)
    popu=pop[0:hcount]+pop[n-lcount:]
    return popu

def croisement(ind1,ind2):
    return (individu(ind1.val[:4]+ind2.val[4:]), individu(ind2.val[:4]+ind1.val[4:]))

def Mutation(ind):
    ind.val[random.randint(0,7)]=random.randint(0,7)
    return ind

def algosimple():
    pop=create_rand_pop(25)
    solutiontrouvee=False
    nbiteration=0
    while not solutiontrouvee:
        print("iteration numero :",nbiteration)
        nbiteration+=1
        evaluation = evaluate(pop)
        if evaluation[0].fitness()==0:
            solutiontrouvee=True
        else:
            select=selection(evaluation,10,4)
            croises=[]
            for i in range(0,len(select),2):
                croises+=croisement(select[i],select[i+1])
            mutes=[]
            for i in select:
                mutes.append(Mutation(i))
            newalea=create_rand_pop(5)
            pop=select[:]+croises[:]+mutes[:]+newalea[:]
    print(evaluation[0])

algosimple()         