from operator import itemgetter
from typing import List, Tuple, Dict

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

# Sample data (moved outside main to be accessible for tests)
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

# Helper functions
def create_one_to_many_relation(conductors: List[Conductor], orchestras: List[Orchestra]) -> List[Tuple[int, int, str]]:
    return [(h.number, h.cost, s.name)
            for h in conductors
            for s in orchestras
            if h.orchestra_id == s.id]


def create_many_to_many_relation(
    conductors: List[Conductor],
    orchestras: List[Orchestra],
    conductor_orchestra: List[ConductorOrchestra]
) -> List[Tuple[int, int, str]]:
    return [(h.number, h.cost, s.name)
            for hs in conductor_orchestra
            for h in conductors if h.id == hs.conductor_id
            for s in orchestras if s.id == hs.orchestra_id]


def filter_orchestras_by_starting_letter(orchestras: List[Orchestra], letter: str, conductors: List[Conductor]) -> Dict[str, List[Tuple[int, int]]]:
    res = {}
    for s in orchestras:
        if s.name[0] == letter:
            h_s = [(conductor.number, conductor.cost) for conductor in conductors if conductor.orchestra_id == s.id]
            res[s.name] = h_s
    return res

def get_max_conductor_cost_per_orchestra(
    orchestras: List[Orchestra],
    one_to_many_relation: List[Tuple[int, int, str]]
) -> List[Tuple[str, int]]:
        res = []
        for s in orchestras:
            s_conductors = list(filter(lambda i: i[2] == s.name, one_to_many_relation))
            if len(s_conductors) > 0:
                s_costs = [cost for _, cost, _ in s_conductors]
                s_max = max(s_costs)
                res.append((s.name, s_max))
        return sorted(res, key=itemgetter(1), reverse=True)


def sort_many_to_many_by_orchestra_name(many_to_many_relation: List[Tuple[int, int, str]]) -> List[Tuple[int, int, str]]:
    return sorted(many_to_many_relation, key=itemgetter(2))

def main():
    one_to_many = create_one_to_many_relation(conductors, orchestras)
    many_to_many = create_many_to_many_relation(conductors, orchestras, conductor_orchestra)

    print('Task G1')
    res_1 = filter_orchestras_by_starting_letter(orchestras, 'S', conductors)
    print(res_1)

    print('Task G2')
    res_2 = get_max_conductor_cost_per_orchestra(orchestras, one_to_many)
    print(res_2)

    print('Task G3')
    res_3 = sort_many_to_many_by_orchestra_name(many_to_many)
    print(res_3)

if __name__ == '__main__':
    main()
