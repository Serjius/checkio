users = [{"id": 0, "name": "Zerro"},
         {"id": 1, "name": "One"},
         {"id": 2, "name": "Two"},
         {"id": 3, "name": "Three"},
         {"id": 4, "name": "Four"},
         {"id": 5, "name": "Five"},
         {"id": 6, "name": "Six"},
         {"id": 7, "name": "Seven"},
         {"id": 8, "name": "Eight"},
         {"id": 9, "name": "Nine"},
         ]
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9),
               ]

for u in users:
    u["friends"] = []

# print(users)

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

print(users[0]['friends'])
