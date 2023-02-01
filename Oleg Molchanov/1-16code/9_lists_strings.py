children=['abruzov_2000', 'ivanov_2011', 'petrov_2010', 'Bubnov_2015']

'''def by_year(name):
    splited_name= name.split('_')
    print(splited_name)

by_year(children[0])'''

def by_year(name):
    return name.split('_')[-1]
    

print(by_year(children[0]))


s_children = sorted(children,key=by_year)

print(s_children)

