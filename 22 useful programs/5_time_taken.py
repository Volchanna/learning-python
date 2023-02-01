import time
start_time= time.time()
def fun():
    a=2
    b=3
    c=a+b
    d=c+a+b
    return(d)
end_time= time.time()
fun()
print(fun())
timetaken = end_time - start_time
print("Your program takes: ", timetaken)
print(start_time, end_time)
print(end_time)