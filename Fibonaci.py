limit = int(input(" Enter the limit  : "))
first_number  = 0
second_number = 1
for i in range(limit):
    print(first_number, end=" ")
    temp = first_number 
    first_number = first_number + second_number
    second_number = temp
    if first_number > limit:
        break
