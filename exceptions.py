# A way to handle erros created by users in a way that doesnt damage the code
#Errors it can catch are: zero division, file not found, value error, type error, index error
while True:
    try:
        num = int(input("Tell me a number: "))
        numTwo = int(input("Tell me another number: "))
    except TypeError:
        print("That wasnt a whole number stupid")
        continue
    else:
        print(f'{str(num)} plus {str(numTwo)} equals {num + numTwo}')
        again = input("Do you want to play this super fun game again(Y/N) ").strip().upper()
        if again == "Y":
            continue
        else:
            break