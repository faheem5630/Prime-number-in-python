def is_num(n):
    if n <= 1:
        return False
    elif n ==2:
        return 2
    if n%2 == 0:
        return False
    i = 3 
    while i * i <= n:
        if n % i == 0:
            return False
        i+=2
    return True


while True:
    start_value = eval(input("enter the starting number: "))
    end_value = eval(input("enter the end value: "))
    if start_value > end_value:
        print("end must greater than start")
    elif start_value == end_value or start_value <= 1:
        print("please select the valid range")
        continue
    else:
        print("prime number in the range from", start_value, "to", end_value)
    n = start_value
    while n <= end_value:
            
            if is_num(n):
                print(n, end=" ")
            n+=1
    break



