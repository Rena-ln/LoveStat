print("enter the probability of person sympathised you")
A = float(input())
print("enter the probability of you sympathised the person")
I1 = float(input())
print("enter the probability of person is clueless in relationships")
P1t = float(input())

Fi = P1t*A*I1 + P1t*(1-A)*I1 + (1-P1t)*(1-A)*I1
F1 = (1-P1t)*A*(1-I1)
O1 = (1-P1t)*A*I1
N = 1 - Fi - F1 - O1
print("=============== Computation results ===============")
print(f"Relationships with person:     {round(O1*100, 1)}%")
print(f"Person is in frendzone:        {round(F1*100, 1)}%\n")
print(f"Frendzone of you by person:    {round(Fi*100, 1)}%")
print(f"Nothing happens:               {round(N*100, 1)}%\n")