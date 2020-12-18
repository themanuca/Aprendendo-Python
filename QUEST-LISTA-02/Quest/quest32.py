c = []

t = int(input('Quantos pedidos: '))

def pedido(t, c):
    for _ in range(0, t):
        log = str(input('Faça seu pedido: '))
        c.append(log)

        #print(c)

pedido(t, c)


p = ['100','101','102','103','104', '105', '106']
a = 0
b = 0
c1 = 0
d = 0
e = 0
f = 0
g = 0
soma = 0


#def part0(c, a, soma, p):
if c[0] == p[0] or c[0] == p[1] or c[0] == p[2] or c[0] == p[3] or c[0] == p[4] or c[0] == p[5] or c[0] == p[6]:
    if c[0] == p[0]:
        a += 1.2
    if c[0] == p[1]:
        a += 1.3

    if c[0] == p[2]:
        a += 1.5
                
    if c[0] == p[3]:
        a += 1.2
                
    if c[0] == p[4]:
        a += 1.7
                
    if c[0] == p[5]:
        a += 2.2

    if c[0] == p[6]:
        a += 1

        
soma = a
if t == 1:
    print(soma)

 

#def part(c, b, a, soma):
#if c[1] == p[0] or c[1] == p[1] or c[1] == p[2] or c[1] == p[3] or c[1] == p[4] or c[1] == p[5] or c[1] == p[6]:
if c[1] == p[0]:
    b += 1.2
if c[1] == p[1]:
    b += 1.3

if c[1] == p[2]:
    b += 1.5
            
if c[1] == p[3]:
    b += 1.2
            
if c[1] == p[4]:
    b += 1.7
            
if c[1] == p[5]:
    b += 2.2

if c[1] == p[6]:
    b += 1
        
soma = a + b
    
if t == 2:
    print(soma)




#def part2(c,c1,a ,b , soma, p, ):
#if c[2] == p[0] or c[2] == p[1] or c[2] == p[2] or c[2] == p[3] or c[2] == p[4] or c[2] == p[5] or c[2] == p[6]:    
if c[2] == p[0]:
    c1 += 1.2
        
if c[2] == p[1]:
    c1 += 1.3
        
if c[2] == p[2]:
    c1 += 1.5
        
if c[2] == p[3]:
    c1 += 1.2

if c[2] == p[4]:
    c1 += 1.7

if c[2] == p[5]:
    c1 += 2.2
        
if c[2] == p[6]:
    c1 += 1

soma = a + b + c1
if t == 3:
    print(soma)


if c[3] == p[0]:
    d += 1.2

if c[3] == p[1]:
    d += 1.3

if c[3] == p[2]:
    d+= 1.5

if c[3] == p[3]:
    d += 1.2

if c[3] == p[4]:
    d+= 1.7

if c[3] == p[5]:
    d += 2.2

if c[3] == p[6]:
    d += 1

soma = a + b + c1 + d
if t == 4:
    print(soma)


if c[4] == p[0]:
    e += 1.2

if c[4] == p[1]:
    e += 1.3

if c[4] == p[2]:
    e += 1.5

if c[4] == p[3]:
    e += 1.2

if c[4] == p[4]:
    e += 1.7

if c[4] == p[5]:
    e += 2.2

if c[4] == p[6]:
    e += 1

soma = a + b + c1 + d + e
if t == 5:
    print(soma)


if c[5] == p[0]:
    f += 1.2

if c[5] == p[1]:
    f += 1.3

if c[5] == p[2]:
    f += 1.5

if c[5] == p[3]:
    f += 1.2

if c[5] == p[4]:
    f += 1.7

if c[5] == p[5]:
    f += 2.2

if c[5] == p[6]:
    f += 1

soma = a + b + c1 + d + e + f
if t == 6:
    print(soma)


if c[6] == p[0]:
    g += 1.2

if c[6] == p[1]:
    g += 1.3

if c[6] == p[2]:
    g += 1.5

if c[6] == p[3]:
    g += 1.2

if c[6] == p[4]:
    g += 1.7

if c[6] == p[5]:
    g += 2.2

if c[6] == p[6]:
    g += 1

soma = a + b + c1 + d + e + g
if t == 7:
    print(soma)








    


