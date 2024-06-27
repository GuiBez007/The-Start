def read_int(prompt, min, max):
    try:
        prompt = int(input("Enter a number from -10 to 10: "))
        assert prompt >= min 
        assert prompt <= max
        return prompt
    except ValueError:
        print('Error: wrong input\n')
    except AssertionError:
        print("Error: the value is not within permitted range (min..max)\n")

v = read_int("Enter a number from -10 to 10: ", -10, 10)
while v == None:
    v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
