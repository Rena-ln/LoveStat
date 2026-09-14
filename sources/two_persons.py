print("enter the probability of person 1 sympathised you")
A = float(input())
print("enter the probability of person 2 sympathised you")
M = float(input())
print("enter the probability of you sympathised the person 1")
I1 = float(input())
print("enter the probability of you sympathised the person 2")
I2 = float(input())
print("enter the probability of person 1 is clueless in relationships")
P1t = float(input())
print("enter the probability of person 2 is clueless in relationships")
P2t = float(input())


TFI = P1t*P2t*M*(1-A)*I1*I2 + P1t*P2t*(1-M)*A*I1*I2 + P1t*P2t*(1-M)*(1-A)*I1*I2 + P1t*(1-P2t)*(1-M)*A*I1*I2 + (1-P1t)*P2t*M*(1-A)*I1*I2 + (1-P1t)*P2t*(1-M)*(1-A)*I1*I2 + (1-P1t)*(1-P2t)*(1-A)*(1-M)*I1*I2
FI2 = P1t*P2t*M*A*(1-I1)*I2 + P1t*P2t*M*(1-A)*(1-I1)*I2 + P1t*P2t*(1-M)*A*(1-I1)*I2 + P1t*P2t*(1-M)*(1-A)*(1-I1)*I2 + (1-P1t)*P2t*M*(1-A)*(1-I1)*I2 + (1-P1t)*P2t*(1-M)*(1-A)*(1-I1)*I2 + (1-P1t)*(1-P2t)*(1-A)*(1-M)*(1-I1)*I2
FI1 = P1t*P2t*M*A*I1*(1-I2) + P1t*P2t*M*(1-A)*I1*(1-I2) + P1t*P2t*(1-M)*A*I1*(1-I2) + P1t*P2t*(1-M)*(1-A)*I1*(1-I2) + (1-P1t)*P2t*M*(1-A)*I1*(1-I2) + (1-P1t)*P2t*(1-M)*(1-A)*I1*(1-I2) + (1-P1t)*(1-P2t)*(1-A)*(1-M)*I1*(1-I2)
HZ = (1-P1t)*(1-P2t)*M*A*I1*I2
O2 = P1t*(1-P2t)*M*A*(1-I1)*I2 + P1t*(1-P2t)*M*A*I1*I2 + P1t*(1-P2t)*M*(1-A)*(1-I1)*I2 + P1t*(1-P2t)*M*(1-A)*I1*I2 + (1-P1t)*(1-P2t)*M*A*(1-I1)*I2 + (1-P1t)*(1-P2t)*M*(1-A)*(1-I1)*I2 + (1-P1t)*(1-P2t)*M*(1-A)*I1*I2
O1 = (1-P1t)*P2t*M*A*I1*I2 + (1-P1t)*P2t*M*A*I1*(1-I2) + (1-P1t)*P2t*(1-M)*A*I1*I2 + (1-P1t)*P2t*(1-M)*A*I1*(1-I2) + (1-P1t)*(1-P2t)*M*A*I1*(1-I2) + (1-P1t)*(1-P2t)*(1-M)*A*I1*I2 + (1-P1t)*(1-P2t)*(1-M)*A*I1*(1-I2)
F2 = P1t*(1-P2t)*M*A*(1-I1)*(1-I2) + P1t*(1-P2t)*M*A*I1*(1-I2) + P1t*(1-P2t)*M*(1-A)*(1-I1)*(1-I2) + P1t*(1-P2t)*M*(1-A)*I1*(1-I2) + (1-P1t)*(1-P2t)*M*A*(1-I1)*(1-I2) + (1-P1t)*(1-P2t)*M*(1-A)*(1-I1)*(1-I2) + (1-P1t)*(1-P2t)*M*(1-A)*I1*(1-I2)
F1 = (1-P1t)*P2t*M*A*(1-I1)*I2 + (1-P1t)*P2t*M*A*(1-I1)*(1-I2) + (1-P1t)*P2t*(1-M)*A*(1-I1)*I2 + (1-P1t)*P2t*(1-M)*A*(1-I1)*(1-I2) + (1-P1t)*(1-P2t)*M*A*(1-I1)*(1-I2) + (1-P1t)*(1-P2t)*(1-M)*A*(1-I1)*I2 + (1-P1t)*(1-P2t)*(1-M)*A*(1-I1)*(1-I2)
N = 1-TFI-FI2-FI1-HZ-O2-O1-F2-F1

print("=============== Computation results ===============")
print(f"Relationships with person 1:   {round(O1*100, 1)}%")
print(f"Person 1 is in frendzone:      {round(F1*100, 1)}%\n")
print(f"Relationships with person 2:   {round(O2*100, 1)}%")
print(f"Person 2 is in frendzone:      {round(F2*100, 1)}%\n")
print(f"Nothing happens:               {round(N*100, 1)}%\n")
print(f"Total frendzone of you:        {round(TFI*100, 1)}%")
print(f"Frendzone of you by person 1:  {round(FI1*100, 1)}%")
print(f"Frendzone of you by person 2:  {round(FI2*100, 1)}%")
print("------------------")
print(f"Your being in any frendzone:   {round((TFI+FI1+FI2)*100, 1)}%")