#file = open('readme.txt')
#file.write('12')
#date = file.read()
#print(date)
#file.close()



pic = 'go.jpg'
file = open(pic, 'rb')

new_file = open('copy_'+pic, 'wb')
new_file.write(file.read())