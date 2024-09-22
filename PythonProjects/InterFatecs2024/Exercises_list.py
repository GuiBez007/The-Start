# total_exercises == 24 (11+11+2) 72days
import random
import time

exercises_to_do = ['F1A', 'F1B', 'F1C', 'F1D', 'F1E', 'F1F', 'F1G', 'F1H', 'F1I', 'F1J', 'F1K', 'F2A', 'F2B', 'F2C',
                   'F2D', 'F2E', 'F2F', 'F2G', 'F2H', 'F2I', 'F2J', 'F2K', 'ExB', 'ExC']
exercises_ever_maked = ['ExB', 'ExC', 'F1C', 'F1E']
dont_want_to_do = ['F1A', 'F2A', 'F2B', 'F1F']
# maybe 'F1F'

while True:
    index = random.randint(0, len(exercises_to_do)-1)
    if exercises_to_do[index] not in exercises_ever_maked and exercises_to_do[index] not in dont_want_to_do:
        break

dots = '...'
print('\nO exercício sorteado foi', end='')

for i in dots:
    time.sleep(1)
    print(i, end='')

time.sleep(0.7)
print('\n    !!! -> {} <- !!!'.format(exercises_to_do[index]))
time.sleep(7)
