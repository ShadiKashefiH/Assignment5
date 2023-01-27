def square ():

    num1 = int(input("Please enter number1:"))
    num2 = int(input("Please enter number2:"))
    matrix = []

    for i in range (num1):
        a = []
        b = []

        for j in range (num2):
            a.append("#")
            a.append("*")
            b.append("#")
            b.append("*")

        matrix.append(a)
        matrix.append(b)

    for i in range(num1):
        for j in range(num2):
            print(matrix[i][j], end="")
        print()

square()



    

