zoo = ('cheetah', 'monkey', 'octopus', 'python', 'chicken', 'shark', 'dolphin', 'honey badger', 'lion', 'bull')
zoo.index("cheetah")
animal_to_find = "leopard"
if animal_to_find in zoo:
  print('animal is in the zoo.')
(spots, tail, tentacles, snake, bird, fish, smart, ruthless, king, farm) = zoo
zoo = list(zoo)
zoo.extend(['black widow', 'cow', 'leopard'])
zoo = tuple(zoo)