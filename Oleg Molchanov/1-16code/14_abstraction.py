
'''#1000 : 15 = mass :x
#x = 15* mass / 1000

ingrtediets = {
    'salt': 15,
    'pepper': 5
}

def get_salt_mass(m):
    return m*15/1000

def get_pepper_mass(m):
    return m*5/1000


def get_ingredient_mass(m,ingr):
    return m*ingrtediets.get(ingr, 0) / 1000

#print(get_salt_mass(1500))
print(get_ingredient_mass(1500, 'cinnamon'))'''

def print_wrapper(text):
    with open('readme', 'a') as f:
        print(text, file=f)
        #автоматически подставляет знак переноса каретки \n
print_wrapper(2)  

