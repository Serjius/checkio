
def hex_dist(sp, ep):
    your_x = sp[0]
    your_y = int(sp[1])
    dist_dic = {}
    max_n = 30
    n = 1
    while n <= max_n:
        dist_dic[n] = set()
        n1 = your_x
        n2 = str(your_y - n)
        if n1 >= 'A' and n1 <= 'Z' and n2 >= '1' and n2 <= '9':
            dist_dic[n].add(n1 + n2)
            #print('0-1:', n,  n1 + n2)
        n1 = your_x
        n2 = str(your_y + n)
        if n1 >= 'A' and n1 <= 'Z' and n2 >= '1' and n2 <= '9':
            dist_dic[n].add(n1 + n2)
            #print('0-2:', n,  n1 + n2)

        # upper diagonal
        sh = n
        if n % 2 != 0 and (ord(your_x) - ord('A')) % 2 != 0:
            sh -= 1
        for i in range(1, n):
            n1 = chr(ord(your_x) - i)
            n2 = str(your_y - sh)
            if n1 >= 'A' and n1 <= 'Z' and n2 >= '1' and n2 <= '9':
                dist_dic[n].add(n1 + n2)
                #print('1-1:', n, (-i, -sh), n1 + n2)
            n1 = chr(ord(your_x) + i)
            n2 = str(your_y - sh)
            if n1 >= 'A' and n1 <= 'Z' and n2 >= '1' and n2 <= '9':
                dist_dic[n].add(n1 + n2)
                #print('1-2:', n, (i, -sh), n1 + n2)
            sh -= 1

        # bottom diagonal
        sh = n - 1
        if (ord(your_x) - ord('A')) % 2 != 0:
            sh += 1
        for i in range(-n + 1, 0, +1):
            n1 = chr(ord(your_x) - i)
            n2 = str(your_y + sh)
            if n1 >= 'A' and n1 <= 'Z' and n2 >= '1' and n2 <= '9':
                dist_dic[n].add(n1 + n2)
                #print('2-1:', n, (-i, -sh), n1 + n2)
            n1 = chr(ord(your_x) + i)
            n2 = str(your_y + sh)
            if n1 >= 'A' and n1 <= 'Z' and n2 >= '1' and n2 <= '9':
                dist_dic[n].add(n1 + n2)
                #print('2-1:', n, (i, -sh), n1 + n2)
            if i > 2:
                sh -= 1

        # legt and righ bars
        sh = -1 * int((n + 1) // 2)
        if n % 2 != 0 and (ord(your_x) - ord('A')) % 2 != 0:
            sh += 1
        for i in range(-n - 1, 0, +1):
            n1 = chr(ord(your_x) - n)
            n2 = str(your_y + sh)
            if n1 >= 'A' and n1 <= 'Z' and n2 >= '1' and n2 <= '9':
                dist_dic[n].add(n1 + n2)
                #print('3-1:', n, (-n, sh), n1 + n2)
            n1 = chr(ord(your_x) + n)
            n2 = str(your_y + sh)
            if n1 >= 'A' and n1 <= 'Z' and n2 >= '1' and n2 <= '9':
                dist_dic[n].add(n1 + n2)
                #print('3-1:', n, (n, sh), n1 + n2)
            sh += 1

        n += 1

    # D3
    # k1 = ['D2', 'C3', 'C4', 'D4', 'E3', 'E4']
    # k2 = ['D1', 'C2', 'B2', 'B3', 'B4', 'C5', 'D5', 'E5', 'F4', 'F3', 'F2', 'E2']
    # k2 = ['D1', 'C2', 'B2', 'B3', 'B4', 'C5', 'D5', 'E5', 'F4', 'F3', 'F2', 'E2']
    # r1 = [k for k in dist_dic[1]]
    # r2 = [k for k in dist_dic[2]]
    # if sorted(r1) != sorted(k1):
    #     print('Expc:', sorted(k1))
    #     print('Test:', sorted(r1))

    # if sorted(r2) != sorted(k2):
    #     print('Expc:', sorted(k2))
    #     print('Test:', sorted(r2))

    # for i in dist_dic.items():
    #     print(i)
    r = 0
    for i in dist_dic.keys():
        if ep in dist_dic[i]:
            r = i
            break
    return(r)


def find_enemy(you, dir, enemy):
    your_x = you[0]
    your_y = int(you[1])
    enmy_x = enemy[0]
    enmy_y = int(enemy[1])

    d = hex_dist(you, enemy)

    w = ''
    if your_y == enmy_y:
        if your_x > enmy_x:
            w = 'W'
        else:
            w = 'E'

    if your_y > enmy_y:
        if your_x > enmy_x:
            w = 'NW'
        elif your_x < enmy_x:
            w = 'NE'
        else:
            w = 'N'

    if your_y < enmy_y:
        if your_x > enmy_x:
            w = 'SW'
        elif your_x < enmy_x:
            w = 'SE'
        else:
            w = 'S'

    p = ''
    dir_lst = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    side_n_w_lst = ['F', 'R', 'R', 'R', 'B', 'L', 'L', 'L']
    side_s_e_lst = ['F', 'L', 'L', 'L', 'B', 'R', 'R', 'R']

    if dir in ['N', 'SW', 'NW', 'W', 'NE']:
        p = side_n_w_lst[abs(dir_lst.index(dir) - dir_lst.index(w))]
    else:
        p = side_s_e_lst[abs(dir_lst.index(dir) - dir_lst.index(w))]

    print(f'({you}, {dir}, {enemy}) dir:{dir} W:{w} P:{p} D:{d}')
    return ([p, d])


if __name__ == '__main__':
    assert find_enemy("A1", "SW", "Z9") == ['B', 25], "Ext3"
    assert find_enemy("C3", "SE", "A1") == ['B', 3], "T"
    assert find_enemy('B2', 'S', 'B4') == ['F', 2], "T"
    assert find_enemy('G5', 'N', 'G4') == ['F', 1], "N-1"
    assert find_enemy('G5', 'N', 'I4') == ['R', 2], "NE-2"
    assert find_enemy('G5', 'N', 'J6') == ['R', 3], "SE-3"
    assert find_enemy('G5', 'N', 'G9') == ['B', 4], "S-4"
    assert find_enemy('G5', 'N', 'B7') == ['L', 5], "SW-5"
    assert find_enemy('G5', 'N', 'A2') == ['L', 6], "NW-6"
    assert find_enemy('G3', 'NE', 'C5') == ['B', 4], "[watch your six!]"
    assert find_enemy('H3', 'SW', 'E2') == ['R', 3], "right"
    assert find_enemy('A4', 'S', 'M4') == ['L', 12], "true left"
    assert find_enemy("D3", "NE", "A1") == ['L', 4], "Ext2"

    print("You are good to go!")
