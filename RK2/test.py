import pytest
from main import (

    Conductor,
    Orchestra,
    ConductorOrchestra,
    create_one_to_many_relation,
    create_many_to_many_relation,
    filter_orchestras_by_starting_letter,
    get_max_conductor_cost_per_orchestra,
    sort_many_to_many_by_orchestra_name,
    conductors,
    orchestras,
    conductor_orchestra
)

# Test data for the tests
sample_conductors = [
    Conductor(1, 111, 9000, 1),
    Conductor(2, 123, 4500, 2),
    Conductor(3, 125, 3300, 2),
]

sample_orchestras = [
    Orchestra(1, 'Symphony Orchestra #1'),
    Orchestra(2, 'Chamber Orchestra #2'),
]

sample_conductor_orchestra = [
    ConductorOrchestra(1, 1),
    ConductorOrchestra(2, 2),
    ConductorOrchestra(2, 3),
]

def test_create_one_to_many_relation():
    expected_relation = [(111, 9000, 'Symphony Orchestra #1'), (123, 4500, 'Chamber Orchestra #2'), (125, 3300, 'Chamber Orchestra #2')]
    assert create_one_to_many_relation(sample_conductors, sample_orchestras) == expected_relation

def test_create_many_to_many_relation():
    expected_relation = [
        (111, 9000, 'Symphony Orchestra #1'),
        (123, 4500, 'Chamber Orchestra #2'),
        (125, 3300, 'Chamber Orchestra #2')
    ]
    assert create_many_to_many_relation(sample_conductors, sample_orchestras, sample_conductor_orchestra) == expected_relation

def test_filter_orchestras_by_starting_letter():
    expected_result = {
        'Symphony Orchestra #1': [(111, 9000)]
    }
    assert filter_orchestras_by_starting_letter(orchestras, 'S', conductors) == expected_result

def test_get_max_conductor_cost_per_orchestra():
    one_to_many = create_one_to_many_relation(conductors, orchestras)
    expected_result = [
        ('Folk Orchestra #4', 6300),
        ('Symphony Orchestra #1', 9000),
        ('Chamber Orchestra #2', 4500),
        ('Jazz Orchestra #3', 1200)
    ]
    assert get_max_conductor_cost_per_orchestra(orchestras, one_to_many) == expected_result

def test_sort_many_to_many_by_orchestra_name():
    many_to_many = create_many_to_many_relation(conductors, orchestras, conductor_orchestra)
    expected_result = [
         (111, 9000, 'Chamber Orchestra #2'),
         (123, 4500, 'Chamber Orchestra #2'),
        (635, 1200, 'Jazz Orchestra #3'),
        (325, 6300, 'Folk Orchestra #4'),
         (265, 4400, 'Folk Orchestra #4'),
        (111, 9000, 'Symphony Orchestra #1'),
    ]
    assert sort_many_to_many_by_orchestra_name(many_to_many) == expected_result
