# implement dijkstra algorithm
from SPF import *


def dijkatra(spf):
    while not spf.is_Nbar_same_as_N():
        w = spf.find_minimum()
        spf.Nbar.append(w)
        spf.update_D(w)


if __name__ == '__main__':
    LST = {}
    LST.update({('u', 'v'): 2})
    LST.update({('u', 'w'): 5})
    LST.update({('u', 'x'): 1})
    LST.update({('v', 'w'): 3})
    LST.update({('v', 'x'): 2})
    LST.update({('x', 'w'): 3})
    LST.update({('x', 'y'): 1})
    LST.update({('w', 'y'): 1})
    LST.update({('w', 'z'): 5})
    LST.update({('y', 'z'): 2})

    spf_in_u = SPF(LST=LST,
                   host='u',
                   N=['u', 'x', 'v', 'w', 'y', 'z'])

    dijkatra(spf_in_u)

    print(spf_in_u.D)
