people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'}
        }

for key in people:
    print()
    print('Key :', key)
    for key2 in people[key]:
        print(key2.capitalize(), ':', people[key][key2])

# ------------------------------------------------------------------------------
people2 = [
        ('IcFDG2bO9AYDF651DoyH', {'name': 'John', 'age': 27, 'sex': 'Male'}),
        ('KcD9ntE6IRM59vkVta1k', {'name': 'Marie', 'age': 22, 'sex': 'Female'}),
        ('yDlgcn99xPc19mYXcRmy', {'name': 'Agness', 'age': 25, 'sex': 'Female'}),
        ('cpQh6GiAbBdGv35NDoTk', {'name': 'Nabeel', 'age': 17, 'sex': 'Male'}),
        ('12BifzWxCQySKgLhgahC', {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'}),
        ('QLnmg0pzlLj9x7c7DlLv', {'name': 'Ruby', 'age': 55, 'sex': 'Female'}),
        ('To47urX0DUznWmOxGZ6H', {'name': 'Lori', 'age': 27, 'sex': 'Male'}),
        ('KQ4bir3y4tlkbG69I7zq', {'name': 'Marie', 'age': 42, 'sex': 'Female'}),
        ('94cp4hsyZP2BnCh4D34z', {'name': 'Agness', 'age': 25, 'sex': 'Female'}),
        ('Vr4wRdkljeEs46Czxo54', {'name': 'Chiara', 'age': 17, 'sex': 'Male'})
        ]

'''
for Id, data in people2:
    print()
    print('Id :', Id)
    for key in data:
        print(key.capitalize(), ':', data[key])
''' 

# ------------------------------------------------------------------------------
people3 = [
        {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
        {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
        {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}
        ]

'''
for record in people3:
    print()
    for key in record:
        print(key.capitalize(), ':', record[key])
'''

# ------------------------------------------------------------------------------
people4 = [
            "Arkadiusz",
            "Wiola",
            "Kuba"
        ]

'''
for name in people4:
        print('Name :', name)
'''

# ------------------------------------------------------------------------------
ratings1 = {
            "Arkadiusz": (2, 1, 2, 3, 2, 3),
            "Agness": (4, 2, 1, 3, 4)
        }

'''
for key in ratings1:
        print(key.capitalize(), ':', ratings1[key])
'''

# ------------------------------------------------------------------------------
ratings2 = [
            {'name': "Arkadiusz", 'ratings': (2, 1, 2, 3, 2, 3), 'behaviour': 4},
            {'name': "Agness", 'ratings': (4, 2, 1, 3, 4), 'behaviour': 2}
        ]

'''
for key in ratings2:
        print()
        for key2 in key:
                print(key2.capitalize(), ':', key[key2])
'''

# ------------------------------------------------------------------------------
ratings3 = {
            "Arkadiusz": {'ratings': (2, 1, 2, 3, 2, 3), 'behaviour': 4},
            "Agness": {'ratings': (4, 2, 1, 3, 4), 'behaviour': 2}
        }

'''
for key in ratings3:
        print()
        print('Key :', key)
        for key2 in ratings3[key]:
                print(key2.capitalize(), ':', ratings3[key][key2])
'''

# ------------------------------------------------------------------------------
ppllist2 = [
            ('John', 27, 'Male'),
            ('John3', 22, 'Male'),
            ('John2', 11, 'Male')
        ]

'''
for name, age, sex in ppllist2:
        print('Name :', name)
        print('Age :', age)
        print('Sex :', sex)
        print()
'''
