'''def a(name):
    print(locals())


a('Hello')'''

#name = 'Eroha'

def a():
    #name = 'in a()'
    
    def b():
        #name = 'Pupkin'
        print (name)
        print(locals())

    b()
a()