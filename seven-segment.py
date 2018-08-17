import itertools as it
import string


def seven_segment(lit_seg, broken_seg):

    # replace this for solution
    lid = {0: {'A', 'B', 'C', 'D', 'E', 'F', },
           1: {'B', 'C', },
           2: {'A', 'B', 'G', 'E', 'D', },
           3: {'A', 'B', 'G', 'C', 'D', },
           4: {'F', 'B', 'G', 'C', },
           5: {'A', 'F', 'G', 'C', 'D', },
           6: {'A', 'F', 'G', 'C', 'D', 'E'},
           7: {'A', 'B', 'C', },
           8: {'A', 'B', 'C', 'D', 'E', 'F', 'G', },
           9: {'A', 'B', 'C', 'D', 'F', 'G', },
           }
    all_seg = lit_seg.union(broken_seg)
    lid_f = {x for x in lit_seg if x in string.ascii_uppercase}
    lid_s = {x for x in lit_seg if x in string.ascii_lowercase}
    n = 0
    for i in it.product(range(10), repeat=2):
        second_lid = {l.lower() for l in lid[i[1]]}

        if lid[i[0]].issubset(all_seg) and second_lid.issubset(all_seg)\
                and not lid_f.difference(lid[i[0]])\
                and not lid_s.difference(second_lid):
            n += 1
    return n


if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {
                         'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {
                         'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
