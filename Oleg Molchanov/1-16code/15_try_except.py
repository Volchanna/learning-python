def main():
    d = {'webdie':'google', 'url':'google.ru'}
    try:        
        data = d['url']
    except:
        
        data = 'https://'
    else:
        data = data.upper()
    print(data)
'''    finally:
        print('very important action')'''
main()


