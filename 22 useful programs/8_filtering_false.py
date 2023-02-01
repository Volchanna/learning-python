def Filtering(lst):
    return list(filter(None,lst))
lst = [None,1,3,0,"",5,7,4,6,1]
print(Filtering(lst)) #[1, 3, 5, 7]
print(list(filter(None,lst)))
print((filter(None,lst)))
