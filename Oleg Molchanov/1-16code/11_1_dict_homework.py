translit_dict = {'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'Yo','Ж':'Zh','З':'Z','И':'I','Й':'Y','К':'K','Л':'L','М':'M','Н':'N','О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'Kh','Ц':'Ts','Ч':'Ch','Ш':'Sh','Щ':'Sch','Ъ':'','Ь':'','Ы':'Y','Э':'E','Ю':'Yu','Я':'Ya',' ':' '}
slovo = 'Хуй_пизда джигурда!!'
slovo_string = ''

for bukva in slovo:
    if bukva in translit_dict:
        trans = translit_dict[bukva]
        #print(bukva+' '+trans)
    elif bukva.upper() in translit_dict:
        trans = translit_dict[bukva.upper()].lower()
        #print(bukva+' '+trans)
    else:
        trans = bukva 
        #print(bukva+' '+trans)
    slovo_string += trans

print(slovo_string)

#def translit(a):
#bukva = []   
#For bukva in a:
#    print(bukva)