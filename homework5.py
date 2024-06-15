tuple_ = 3, 8.0, "Word", True
print('Immutable tuple: ', tuple_)
print('Types of data')
print(type(tuple_[0]))
print(type(tuple_[1]))
print(type(tuple_[2]))
print(type(tuple_[3]))
# Изменить кортеж невозможно по своим своиствам,
# однако если кортеж содержит в себе список заключенный в квадратные скобки [],
# то возможно изменять элементы списка включенные в кортеж

tuple_1 = 3, 8, ["Word", True]
print(tuple_1)
tuple_1[2][1] = False
print(tuple_1)

list = [3, 5, 8, 4]
print(list)
print('Mutable list: ')
list[1] = 20
print(list)
list.append('Modified')
print(list)
list.extend('Whata')
print(list)
list.remove(8)
print(list)