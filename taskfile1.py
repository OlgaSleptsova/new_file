import os

cook_book = {}

y = 0

with open('recipes.txt',encoding='utf8') as file:
    for ind, line in enumerate(file):
        line = line.strip()

        if not line:
            x =file.readline()
            y = int(file.readline())
            list1 = []
            for m in range(1,y+1):

                len1 =file.readline().split('|')
                ingridients = {'ingredient_name': len1[0], 'quantity': len1[1], 'measure': len1[2]}

                list1.append(ingridients)
                cook_book[x[0:-1]] = (list1)

    # print(cook_book)




#
with open('recipes_cleare.txt', 'w',encoding='utf8') as file:
    for x, line in cook_book.items():
        file.writelines(x+ os.linesep)
        for y in line:
            file.writelines(str(y) + os.linesep)



y = input('Веведите рецепты через запятую ').split(',')

w = input('Введите количество персон ')




def get_shop_list_by_dishes(dishes, person_count):
    z = []
    v =[]
    o =0
    for n in cook_book.keys():
        z.append(n)
    for g in z:
        if g in dishes:
            v.append(g)
            o += 1

    if o == 0:
        print('Такого рецепта нет в кулинарной книге')
    new_cook_book = {}
    for t in v:

        for l in cook_book.get(t):
            new_cook_book[l.get('ingredient_name')] = {'measure':l.get('measure')[0:-1],'quantity': int(l.get('quantity'))* int(person_count)}



    return new_cook_book

print(get_shop_list_by_dishes(y,w))




