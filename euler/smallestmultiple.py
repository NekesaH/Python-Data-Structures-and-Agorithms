def smallest_multiple(number):
    for i in range(2, 21):
        if number % i != 0:
            return False

    return True
number = 20
while True:
    if smallest_multiple(number):
        break
    number += 20 #increment number

    

