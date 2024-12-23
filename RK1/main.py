from operator import itemgetter

class Conductor:
    def __init__(self, id, number, cost, orchestra_id):
        self.id = id
        self.number = number
        self.cost = cost
        self.orchestra_id = orchestra_id

class Orchestra:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ConductorOrchestra:
    def __init__(self, orchestra_id, conductor_id):
        self.orchestra_id = orchestra_id
        self.conductor_id = conductor_id


orchestras = [
    Orchestra(1, 'Symphony Orchestra #1'),
    Orchestra(2, 'Chamber Orchestra #2'),
    Orchestra(3, 'Jazz Orchestra #3'),
    Orchestra(4, 'Folk Orchestra #4'),
    Orchestra(5, 'Pop Orchestra #5'),
    Orchestra(6, 'Wind Orchestra #6'),
]

conductors = [
    Conductor(1, 111, 9000, 1),
    Conductor(2, 123, 4500, 2),
    Conductor(3, 125, 3300, 2),
    Conductor(4, 635, 1200, 3),
    Conductor(5, 325, 6300, 4),
    Conductor(6, 265, 4400, 4),
]

conductor_orchestra = [
    ConductorOrchestra(1, 1),
    ConductorOrchestra(2, 2),
    ConductorOrchestra(2, 3),
    ConductorOrchestra(3, 4),
    ConductorOrchestra(4, 5),
    ConductorOrchestra(4, 6),
    ConductorOrchestra(5, 1),
    ConductorOrchestra(6, 2),
]


def main():
    one_to_many = [(h.number, h.cost, s.name)
                   for h in conductors
                   for s in orchestras
                   if h.orchestra_id == s.id]

    many_to_many_temp = [(s.name, hs.conductor_id, hs.orchestra_id)
                         for s in orchestras
                         for hs in conductor_orchestra
                         if s.id == hs.orchestra_id]

    many_to_many = [(h.number, h.cost, s.name)
                    for hs in conductor_orchestra
                    for h in conductors if h.id == hs.conductor_id
                    for s in orchestras if s.id == hs.orchestra_id]

    print('Task G1')
    res_1 = {}
    for s in orchestras:
        if s.name[0] == 'S':
            h_s = [(conductor.number, conductor.cost) for conductor in conductors if conductor.orchestra_id == s.id]
            res_1[s.name] = h_s
    print(res_1)

    print('Task G2')
    res_2 = []
    for s in orchestras:
        s_conductors = list(filter(lambda i: i[2] == s.name, one_to_many))
        if len(s_conductors) > 0:
            s_costs = [cost for _, cost, _ in s_conductors]
            s_max = max(s_costs)
            res_2.append((s.name, s_max))
    res_2 = sorted(res_2, key=itemgetter(1), reverse=True)
    print(res_2)

    print('Task G3')
    res_3 = sorted(many_to_many, key=itemgetter(2))
    print(res_3)


if __name__ == '__main__':
    main()
