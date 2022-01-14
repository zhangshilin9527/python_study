import re


def find_item(hero):
    with open('sanguo.txt', encoding='utf-8') as f:
        data = f.read().replace('\n ', '')
        name_num = len(re.findall(hero, data))
        print('主角%s出现%s次' % (hero, name_num))
        return name_num


name_dict = {}
with open('name.txt') as f:
    for name in f:
        names = name.split('|')
        for n in names:
            name_dict[n] = find_item(n)
print(name_dict)
weapon_dict = {}
i = 1
with open('weapon.txt', encoding='utf-8') as f:
    for line in f.readlines():
        if i % 2 == 1:
            weapon = line.strip('\n')
            weapon_dict[weapon] = find_item(weapon)
        i += 1
print(weapon_dict)
