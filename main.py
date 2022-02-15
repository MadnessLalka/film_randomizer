import random

print('To enter the movie name use "space"\n'
      'To separate the movie name use symbols "_"')
array_film = [str(i) for i in input().split()]

print(random.choice(array_film))