try:
    a = int(input('1 число '))
    b = int(input('2 число '))

    i = input(': ')
except:
    print('шо ты пишешь дурачёк')

if i == '/':
    c = a / b
    print('результат '+str(c))

elif i == '-':
    c = a - b
    print('результат '+str(c))

elif i == '+':
    c = a + b
    print('результат '+str(c))

elif i == '*':
    c = a * b
    print('результат '+str(c))

else:
    print('хахаха сам считать не умеешь')
