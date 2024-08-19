# F1E - Crausio

first_input = input()
second_input = input()
third_input = input()

first_input = first_input.split()
second_input = second_input.split()

# upgrade of vars
house_info = [int(first_input[0]), int(first_input[1])]
battery = int(first_input[2])
initial_position = [int(second_input[0]), int(second_input[1])]

# verifications
if house_info[0] < 1 or house_info[0] > 100:
    exit()
elif house_info[1] < 1 or house_info[1] > 100:
    exit()
if battery < 0 or battery > 10000:
    exit()

if initial_position[0] < 1 or initial_position[0] > house_info[0]:
    exit()
elif initial_position[1] < 1 or initial_position[1] > house_info[1]:
    exit()

if len(third_input) < 1 or len(third_input) > 10000:
    exit()

# finally the exercise
directions = ['C','B','E','D'] ##
#directions = ["CBED"] ##
hits = 0

print('Teste: ', end='') ##
for i in directions: ##
    print(i, end='') ##
print('\n') ##

for i in third_input:
    if i.upper() not in directions:
        print('\n Not OK!!! ERROR!') ##
        exit()

    # bot moves
    if i.upper() == 'C':
        initial_position[1] += 1
    elif i.upper() == 'B':
        initial_position[1] -= 1
    elif i.upper() == 'E':
        initial_position[0] -= 1
    elif i.upper() == 'D':
        initial_position[0] += 1

    if initial_position[0] > house_info[0]:
        hits += 1
        initial_position[0] -= 1

    if initial_position[1] > house_info[1]:
        hits += 1
        initial_position[1] -= 1

print('{} {} {}'.format(initial_position[0], initial_position[1], hits))
