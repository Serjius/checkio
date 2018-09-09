
def hex_dist(sp, ep):
    your_x = sp[0]
    your_y = int(sp[1])
    dist_dic = {}
    max_n = 3
    n = 1
    while n <= max_n:
        dist_dic[n] = set()
        n1 = your_x
        n2 = str(your_y - n)
        if n1 >= 'A' and n1 <= 'Z' and n2 >= '1' and n2 <= '9':
            dist_dic[n].add(n1 + n2)
            print('0-1:', n,  n1 + n2)
        n1 = your_x
        n2 = str(your_y + n)
        if n1 >= 'A' and n1 <= 'Z' and n2 >= '1' and n2 <= '9':
            dist_dic[n].add(n1 + n2)
            print('0-2:', n,  n1 + n2)
            #print('0-2:', n, your_x + str(your_y + n))
        # if n % 2 == 0:
        #     if chr(ord(your_x) - 2) >= 'A' and chr(ord(your_x) - 2) <= 'Z' and (your_y) >= 0 and (your_y) <= 9:
        #         dist_dic[n].add(chr(ord(your_x) - 2) + str(your_y))
        #         print('1-1:', chr(ord(your_x) - 2) + str(your_y))
        #     if chr(ord(your_x) + 2) >= 'A' and chr(ord(your_x) + 2) <= 'Z' and (your_y) >= 0 and (your_y) <= 9:
        #         dist_dic[n].add(chr(ord(your_x) + 2) + str(your_y))
        #         print('1-2:', chr(ord(your_x) + 2) + str(your_y))

        # upper diagonal
        sh = n
        for i in range(1, n):
            n1 = chr(ord(your_x) - i)
            n2 = str(your_y - sh)
            if n1 >= 'A' and n1 <= 'Z' and n2 >= '1' and n2 <= '9':
                dist_dic[n].add(n1 + n2)
                print('1-1:', n, (-i, -sh), n1 + n2)
            n1 = chr(ord(your_x) + i)
            n2 = str(your_y - sh)
            if n1 >= 'A' and n1 <= 'Z' and n2 >= '1' and n2 <= '9':
                dist_dic[n].add(n1 + n2)
                print('1-1:', n, (i, -sh), n1 + n2)
            sh -= 1

        # bottom diagonal
        sh = n - 1
        for i in range(-n + 1, 0, +1):
            n1 = chr(ord(your_x) - i)
            n2 = str(your_y + sh)
            if n1 >= 'A' and n1 <= 'Z' and n2 >= '1' and n2 <= '9':
                dist_dic[n].add(n1 + n2)
                print('2-1:', n, (-i, -sh), n1 + n2)
            n1 = chr(ord(your_x) + i)
            n2 = str(your_y + sh)
            if n1 >= 'A' and n1 <= 'Z' and n2 >= '1' and n2 <= '9':
                dist_dic[n].add(n1 + n2)
                print('2-1:', n, (i, -sh), n1 + n2)
            if i > 2:
                sh -= 1

        # legt and righ bars
        sh = -1 * int((n + 1) // 2)
        for i in range(-n - 1, 0, +1):
            dist_dic[n].add(chr(ord(your_x) - n) + str(your_y + sh))
            #print('3-1:', n, (-n, sh), chr(ord(your_x) - n) + str(your_y + sh))
            dist_dic[n].add(chr(ord(your_x) + n) + str(your_y + sh))
            #print('3-1:', n, (n, sh), chr(ord(your_x) + n) + str(your_y + sh))
            sh += 1

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
    print(hex_dist('A1', 'J4'))
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
