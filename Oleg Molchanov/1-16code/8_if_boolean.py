'''a = False
if 2*2 == 4:
    print('ok')
else:
    print('Not ok')


password = '123'
user_input = ''


if user_input:
    if user_input == password:
        print('Welcome')
    else:
        print('Wrong password')
else:
    print('Input smth please')



s = '12345678'


if len(s) ==8:
    print('length 8')
elif len(s) == 6:
    print('length 6')
else:
    print ('asdf')

password = '123'
user_input = ''
print('Welcome') if user_input else print('Wrong password')
'''

# 1-100
#3 - Fizz
#5 - Buzz
# 3&5 - FizzBuzz
#i

def fizz_buzz(i):
    if not(i % 3) and not(i % 5):
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 ==0:
        print('Fizz')
    else:
        print(i)

fizz_buzz(1)
fizz_buzz(2)
fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(7)
fizz_buzz(10)
fizz_buzz(15)
fizz_buzz(17)
