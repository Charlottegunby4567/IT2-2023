# Oppgave 1

# 1.1
tall = (5*5)-4
tall = tall-1
# Verdien til tall er 20



# 1.2
ordbok = {"b": [4,3,5], "a":[0]}
# Verdien av ordboken ["a"][0] er 0



# 1.3
liste = [[5,4], [9,12,3]]
# a) Verdien av liste [1][0] er 9
# b) Verdien av liste [0] er [5,4]



# 1.4
def repeter(a): 
    a=a+a 
    return a
a="ab"
b = repeter(a) 

print(a + b)
# det skrives ut ababab


# 1.5
a = 10
b=1
while a > 0:
    b=b*2
    a=a-b
print("a = " + str(a)) 
print("b = " + str(b))
# det skrives ut a = -4 og b = 8


# 1.6
serie = "0"
for i in range(5,10):
    serie = serie + str(i) 
print("serie = " + serie)
# det rksives ut serie = 056789


# 1.7
a=[1,2,3] 
b=a
b[0] += 1
print(a)
# det skrives ut [2,2,3]



