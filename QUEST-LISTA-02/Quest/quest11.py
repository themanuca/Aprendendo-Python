n = int(input('Digite o número: '))
d = 0

while (n > 0):
   d += n % 10
   n = n // 10
   
print(d)