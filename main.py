from cobra import Model, Reaction, Metabolite

model = Model('example_model')

r0 = Reaction('R0')
r0.name = 'R0'
r0.lower_bound = 1
r0.upper_bound = 1

r1 = Reaction('R1')
r1.name = 'R1'
r1.lower_bound = 0
r1.upper_bound = 1000

r2 = Reaction('R2')
r2.name = 'R2'
r2.lower_bound = 0
r2.upper_bound = 1000

X = Reaction('x')
X.name = 'x'
X.lower_bound = 0
X.upper_bound = 1000

Rec_ATP = Reaction('Rec_ATP')
Rec_ATP.name = 'Rec_ATP'
Rec_ATP.lower_bound = 0
Rec_ATP.upper_bound = 1000

r3 = Reaction('R3')
Rec_ATP.name = 'R3'
Rec_ATP.lower_bound = .9
Rec_ATP.upper_bound = .9

A = Metabolite(
    'A', compartment='c')
B = Metabolite(
    'B', compartment='c')
C = Metabolite(
    'C', compartment='c')

ATP = Metabolite(
    'ATP', compartment='c')

r0.add_metabolites({A:1})

r1.add_metabolites({A:-1,B:1})

r2.add_metabolites({B:-1,C:1})

r3.add_metabolites({ATP:-1})

X.add_metabolites({C:-1})

Rec_ATP.add_metabolites({A:-1,ATP:1})


model.add_reactions([r0,r1,Rec_ATP,r2,r3,X])

model.objective = 'x'

model.optimize()

model.summary()


