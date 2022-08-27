s = ('*')
a  = ' '

def check():
    i = 0
    # for triangulo in s:
    while i <= 9:
        i+=1
        if (i % 2) == 0:
            continue

        else:
            ir = 11-(i+3)
            print(f'{(a * ir) + s * i}')

check()

# tengo que mejorar la postura del triangulo (hacerlo más recto) aunque ya puedo decir que lo hice