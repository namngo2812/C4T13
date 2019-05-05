district = ['st', 'bd', 'btl', 'cg', 'dd', 'hbt']
size = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
population = [150.300, 247.100, 333.300, 266.800, 420.900, 318.800]

for i in range(len(district)):
    print(district[i], size[i], population[i])

print('maximum element in the list: ', max(population), '\nMinimum element in the list: ', min(population))
    