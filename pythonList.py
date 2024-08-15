numbers = [10, 34, -5, 6, 98, 3]
names =['Rimzim' , 'Anuj', 'Saloni', 'Aryan', 'Khushi']
mixList = ['hii', 6, 20.9, True]
print(numbers, names)
print(mixList)
numbers.sort()
print(numbers)
print(numbers[0:7:2])
names.append('Anvi')
print(names)
numbers.insert(3,95) #3 is index and 95 is value
numbers[1:4]=[45,88,7]
mixList.remove('hii')
print(mixList)
print(numbers)
print(numbers.pop(5)) #display last if no position is defined