
def hex_dist(sp, ep):
    your_x = sp[0]
    your_y = int(sp[1])
    dist_dic = {}
    max_n = 2
    n = 1
    while n <= max_n:
        dist_dic[n] = set()
        if your_x >= 'A' and your_x <= 'Z'\
                and (your_y - n) >= 1 and (your_y - n) <= 9:
            dist_dic[n].add(your_x + str(your_y - n))
        if your_x >= 'A' and your_x <= 'Z'\
                and (your_y + n) >= 1 and (your_y + n) <= 9:
            dist_dic[n].add(your_x + str(your_y + n))
        if n % 2 == 0:
            if chr(ord(your_x) - 2 * n) >= 'A' and \
                chr(ord(your_x) - 2 * n) <= 'Z'\
                    and (your_y) >= 0 and (your_y) <= 9:
                dist_dic[n].add(chr(ord(your_x) - 2) + str(your_y))
            if chr(ord(your_x) + 2 * n) >= 'A' and \
                chr(ord(your_x) + 2 * n) <= 'Z'\
                    and (your_y) >= 0 and (your_y) <= 9:
                dist_dic[n].add(chr(ord(your_x) + 2) + str(your_y))
        n_odd = -n
        if (ord(your_x) - ord('A') + 1) % 2 == 0:
            n_odd += 1
        n_even = -n + 1
        new_elm = n * 2 if n % 2 != 0 else n * 2 - 1
        for i in range(1, new_elm, 1):
            k = 0
            if i % 2 == 0:
                k = n_even
                n_even += 1
            else:
                k = n_odd
                n_odd += 1
            if chr(ord(your_x) - i) >= 'A' and chr(ord(your_x) - i) <= 'Z'\
                    and (your_y + k) >= 1 and (your_y + k) <= 9:
                dist_dic[n].add(chr(ord(your_x) - i) + str(your_y + k))
                print('1-1:', n, (i, k), chr(ord(your_x) - i) + str(your_y + k))
            if chr(ord(your_x) + i) >= 'A' and chr(ord(your_x) + i) <= 'Z' \
                    and (your_y + k) >= 1 and (your_y + k) <= 9:
                dist_dic[n].add(chr(ord(your_x) + i) + str(your_y + k))
                print('1-2:', n, (i, k), chr(ord(your_x) + i) + str(your_y + k))
            #print(n, (-i, k), (i, k))
        n_odd = 0
        if (ord(your_x) - ord('A') + 1) % 2 == 0:
            n_odd += 1
        n_even = 1
        new_elm = (n * 2 - 1) if n % 2 != 0 else (n * 2 - 2)
        for i in range(new_elm, 0, -1):
            k = 0
            if i % 2 == 0:
                k = n_even
                n_even += 1
            else:
                k = n_odd
                n_odd += 1
            if chr(ord(your_x) - i) >= 'A' and chr(ord(your_x) - i) <= 'Z'\
                    and (your_y + k) >= 1 and (your_y + k) <= 9:
                dist_dic[n].add(chr(ord(your_x) - i) + str(your_y + k))
                print('2-1:', n, i, (-i, k), chr(ord(your_x) - i) + str(your_y + k))
            if chr(ord(your_x) + i) >= 'A' and chr(ord(your_x) + i) <= 'Z'\
                    and (your_y + k) >= 1 and (your_y + k) <= 9:
                dist_dic[n].add(chr(ord(your_x) + i) + str(your_y + k))
                print('2-1:', n, i, (i, k), chr(ord(your_x) + i) + str(your_y + k))
            #print(n, (-i, k), (i, k))
        n += 1

    for i in dist_dic.items():
        print(i)
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

    if dir in ['N', 'SW', 'NW', 'W']:
        p = side_n_w_lst[abs(dir_lst.index(dir) - dir_lst.index(w))]
    else:
        p = side_s_e_lst[abs(dir_lst.index(dir) - dir_lst.index(w))]

    print(f'({you}, {dir}, {enemy}) W:{w} P:{p} D:{d}')
    return ([p, d])


if __name__ == '__main__':
    print(hex_dist('A1', 'M4'))
    # assert find_enemy("C3", "SE", "A1") == ['B', 3], "T"
    # assert find_enemy('B2', 'S', 'B4') == ['F', 2], "T"
    # assert find_enemy('G5', 'N', 'G4') == ['F', 1], "N-1"
    # assert find_enemy('G5', 'N', 'I4') == ['R', 2], "NE-2"
    # assert find_enemy('G5', 'N', 'J6') == ['R', 3], "SE-3"
    # assert find_enemy('G5', 'N', 'G9') == ['B', 4], "S-4"
    # assert find_enemy('G5', 'N', 'B7') == ['L', 5], "SW-5"
    # assert find_enemy('G5', 'N', 'A2') == ['L', 6], "NW-6"
    # assert find_enemy('G3', 'NE', 'C5') == ['B', 4], "[watch your six!]"
    # assert find_enemy('H3', 'SW', 'E2') == ['R', 3], "right"
    # assert find_enemy('A4', 'S', 'M4') == ['L', 12], "true left"
    print("You are good to go!")
