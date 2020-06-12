import os
import collections



def read (filename):
    cook_book = {}

    with open(filename,encoding='utf8') as file:

        for ind, line in enumerate(file):
            line = line.strip()
            if ind == 0:
                list1 = []
                cook_book[line] =list1
                y = int(file.readline())

                for m in range(1,y+1):
                    len1 =file.readline().split('|')
                    ingridients = {'ingredient_name': len1[0], 'quantity': int (len1[1]), 'measure': len1[2]}
                    list1.append(ingridients)

            if not line:
                x = file.readline()
                y = int(file.readline())
                list2 = []
                cook_book[x[0:-1]] = list2
                for m in range(1,y+1):
                    len1 =file.readline().split('|')
                    ingridients = {'ingredient_name': len1[0], 'quantity': int(len1[1]), 'measure': len1[2]}

                    list2.append(ingridients)

    return cook_book

def write (filename, cook_book):

    with open('recipes_cleare.txt', 'w',encoding='utf8') as file:
        for x, line in cook_book.items():
            file.writelines(x+ os.linesep)
            for y in line:
                file.writelines(str(y) + os.linesep)

def read_and_write(filename,new_filename):
    cook_book = read(filename)
    write(new_filename,cook_book)

read_and_write('recipes.txt','recipes_cleare.txt')


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read('recipes.txt')
    new_cook_book = {}
    zx = collections.Counter()
    for word in dishes:
        zx[word] += 1
    for a, z in zx.items():
        if z > 1:
            list_rec = []
            list_rec.append(a)
            recepes = []
            o = 0
            for n in cook_book.keys():
                recepes.append(n)
            for k in list_rec:
                if k in recepes:
                    o += 1
                    list3 = cook_book.get(k)
                    for l in list3:
                        new_cook_book[l.get('ingredient_name')] = {'measure': l.get('measure')[0:-1],
                                                                   'quantity': l.get('quantity') * int(
                                                                       person_count) * int(z)}

            if o == 0:
                print('Такого рецепта нет в кулинарной книге')

        else:
            recepes = []

            o = 0
            for n in cook_book.keys():
                recepes.append(n)
            for k in dishes:
                if k in recepes:
                    o += 1
                    list3 = cook_book.get(k)
                    for l in list3:
                        new_cook_book[l.get('ingredient_name')] = {'measure': l.get('measure')[0:-1],
                                                                   'quantity': l.get('quantity') * int(person_count)}

            if o == 0:
                print('Такого рецепта нет в кулинарной книге')

    return new_cook_book

print(get_shop_list_by_dishes(['Омлет','Омлет'],2))
