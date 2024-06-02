nokta=[(2,6),(4,7),(6,3),(8,5)]

def mesafe(c1,c2):
    return pow(pow(c1[0]-c2[0],2)+pow(c1[1]-c2[1],2),0.5)

uzaklik=[]

for i in range(len(nokta)-1):
    for k in range(i+1,len(nokta)):
        uzaklik.append(mesafe(nokta[i],nokta[k]))


print(min(uzaklik))