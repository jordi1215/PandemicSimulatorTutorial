# Confidential, Copyright 2020, Sony Corporation of America, All rights reserved.

from .person_routines import DefaultPersonRoutineAssignment
from ..environment import Home, GroceryStore, Office, School, UTAustin, ZilkerPark, BartonCreekMall, Hospital, RetailStore, HairSalon, Restaurant, Bar, \
    PandemicSimConfig, LocationConfig

__all__ = ['austin_config', 'town_config', 'small_town_config', 'test_config',
           'tiny_town_config', 'medium_town_config',
           'above_medium_town_config', 'experiment_config']

"""
A few references for the numbers selected:

http://www.worldcitiescultureforum.com/data/number-of-restaurants-per-100.000-population (Austin)

"""
# num_persons = 964177
# #num_persons = 9642
# home = (int)(num_persons * 0.3)
# groceryStore = (int)(num_persons * 0.004)
# office = (int)(num_persons * 0.005)
# school = (int)(num_persons * 0.01)
# hospital = (int)(num_persons * 0.001)
# retailStore = (int)(num_persons * 0.004)
# hairSalon = (int)(num_persons * 0.004)
# restaurant = (int)(num_persons * 0.002)
# bar = (int)(num_persons * 0.002)

# experiment_config = PandemicSimConfig(
#     # num_persons=1251000,  # 1.251 million (2020)
#     num_persons=num_persons,  # https://datacommons.org/place/geoId/4805000?utm_medium=explore&mprop=count&popt=Person&hl=en
#     # num_persons=164177, # run test to see how running time correlates with the number of people
#     # Population: ? (2020) www2.census.gov
#     # Population: 964,177 (2021) www2.census.gov
#     location_configs=[
#         LocationConfig(Home, num=home),
#         LocationConfig(GroceryStore, num=groceryStore, num_assignees=5, state_opts=dict(visitor_capacity=30)),
#         LocationConfig(Office, num=office, num_assignees=150, state_opts=dict(visitor_capacity=0)),
#         LocationConfig(School, num=school, num_assignees=4, state_opts=dict(visitor_capacity=30)),
#         LocationConfig(University, num=1, num_assignees=3000, state_opts=dict(visitor_capacity=52000)),
#         LocationConfig(Hospital, num=hospital, num_assignees=30, state_opts=dict(patient_capacity=10)),
#         LocationConfig(RetailStore, num=retailStore, num_assignees=5, state_opts=dict(visitor_capacity=30)),
#         LocationConfig(HairSalon, num=hairSalon, num_assignees=3, state_opts=dict(visitor_capacity=5)),
#         LocationConfig(Restaurant, num=restaurant, num_assignees=6, state_opts=dict(visitor_capacity=30)),
#         LocationConfig(Bar, num=bar, num_assignees=5, state_opts=dict(visitor_capacity=30)),
#     ],
#     person_routine_assignment=DefaultPersonRoutineAssignment())


austin_config = PandemicSimConfig(
    num_persons=964177,  # https://datacommons.org/place/geoId/4805000?utm_medium=explore&mprop=count&popt=Person&hl=en
    # Population: ? (2020) www2.census.gov
    # Population: 964,177 (2021) www2.census.gov
    location_configs=[
        LocationConfig(Home, num=289253),
        LocationConfig(GroceryStore, num=3857, num_assignees=5, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Office, num=4500, num_assignees=150, state_opts=dict(visitor_capacity=0)),
        LocationConfig(School, num=900, num_assignees=40, state_opts=dict(visitor_capacity=300)),
        LocationConfig(UTAustin, num=1, num_assignees=3000, state_opts=dict(visitor_capacity=52000)),
        LocationConfig(ZilkerPark, num=1, num_assignees=4, state_opts=dict(visitor_capacity=6849)),
        LocationConfig(BartonCreekMall, num=1, num_assignees=180*5, state_opts=dict(visitor_capacity=180*30)),
        LocationConfig(Hospital, num=1000, num_assignees=30, state_opts=dict(patient_capacity=10)),
        LocationConfig(RetailStore, num=3857, num_assignees=5, state_opts=dict(visitor_capacity=30)),
        LocationConfig(HairSalon, num=3857, num_assignees=3, state_opts=dict(visitor_capacity=5)),
        LocationConfig(Restaurant, num=1900, num_assignees=6, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Bar, num=1900, num_assignees=5, state_opts=dict(visitor_capacity=30)),
    ],
    person_routine_assignment=DefaultPersonRoutineAssignment())


town_config = PandemicSimConfig(
    num_persons=10000,
    location_configs=[
        LocationConfig(Home, num=3000),  # 10:3
        LocationConfig(GroceryStore, num=40, num_assignees=5, state_opts=dict(visitor_capacity=30)),  # 250 :1
        LocationConfig(Office, num=50, num_assignees=150, state_opts=dict(visitor_capacity=0)),
        LocationConfig(School, num=10, num_assignees=40, state_opts=dict(visitor_capacity=300)),
        LocationConfig(Hospital, num=10, num_assignees=30, state_opts=dict(patient_capacity=10)),
        LocationConfig(RetailStore, num=40, num_assignees=5, state_opts=dict(visitor_capacity=30)),
        LocationConfig(HairSalon, num=40, num_assignees=3, state_opts=dict(visitor_capacity=5)),
        LocationConfig(Restaurant, num=20, num_assignees=6, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Bar, num=20, num_assignees=5, state_opts=dict(visitor_capacity=30)),
    ],
    person_routine_assignment=DefaultPersonRoutineAssignment())

above_medium_town_config = PandemicSimConfig(
    num_persons=4000,
    location_configs=[
        LocationConfig(Home, num=1200),
        LocationConfig(GroceryStore, num=16, num_assignees=5, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Office, num=20, num_assignees=150, state_opts=dict(visitor_capacity=0)),
        LocationConfig(School, num=40, num_assignees=4, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Hospital, num=4, num_assignees=30, state_opts=dict(patient_capacity=10)),
        LocationConfig(RetailStore, num=16, num_assignees=5, state_opts=dict(visitor_capacity=30)),
        LocationConfig(HairSalon, num=16, num_assignees=3, state_opts=dict(visitor_capacity=5)),
        LocationConfig(Restaurant, num=8, num_assignees=6, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Bar, num=8, num_assignees=4, state_opts=dict(visitor_capacity=30))
    ],
    person_routine_assignment=DefaultPersonRoutineAssignment())

medium_town_config = PandemicSimConfig(
    num_persons=2000,
    location_configs=[
        LocationConfig(Home, num=600),
        LocationConfig(GroceryStore, num=8, num_assignees=5, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Office, num=10, num_assignees=150, state_opts=dict(visitor_capacity=0)),
        LocationConfig(School, num=2, num_assignees=40, state_opts=dict(visitor_capacity=300)),
        LocationConfig(Hospital, num=2, num_assignees=30, state_opts=dict(patient_capacity=10)),
        LocationConfig(RetailStore, num=8, num_assignees=5, state_opts=dict(visitor_capacity=30)),
        LocationConfig(HairSalon, num=8, num_assignees=3, state_opts=dict(visitor_capacity=5)),
        LocationConfig(Restaurant, num=4, num_assignees=6, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Bar, num=4, num_assignees=3, state_opts=dict(visitor_capacity=30))
    ],
    person_routine_assignment=DefaultPersonRoutineAssignment())

small_town_config = PandemicSimConfig(
    num_persons=1000,
    location_configs=[
        LocationConfig(Home, num=300),
        LocationConfig(GroceryStore, num=4, num_assignees=5, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Office, num=5, num_assignees=150, state_opts=dict(visitor_capacity=0)),
        LocationConfig(School, num=1, num_assignees=40, state_opts=dict(visitor_capacity=300)),
        LocationConfig(Hospital, num=1, num_assignees=30, state_opts=dict(patient_capacity=10)),
        LocationConfig(RetailStore, num=4, num_assignees=5, state_opts=dict(visitor_capacity=30)),
        LocationConfig(HairSalon, num=4, num_assignees=3, state_opts=dict(visitor_capacity=5)),
        LocationConfig(Restaurant, num=2, num_assignees=6, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Bar, num=2, num_assignees=5, state_opts=dict(visitor_capacity=30)),
    ],
    person_routine_assignment=DefaultPersonRoutineAssignment())

tiny_town_config = PandemicSimConfig(
    num_persons=500,
    location_configs=[
        LocationConfig(Home, num=150),
        LocationConfig(GroceryStore, num=2, num_assignees=5, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Office, num=2, num_assignees=150, state_opts=dict(visitor_capacity=0)),
        LocationConfig(School, num=10, num_assignees=2, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Hospital, num=1, num_assignees=15, state_opts=dict(patient_capacity=5)),
        LocationConfig(RetailStore, num=2, num_assignees=5, state_opts=dict(visitor_capacity=30)),
        LocationConfig(HairSalon, num=2, num_assignees=3, state_opts=dict(visitor_capacity=5)),
        LocationConfig(Restaurant, num=1, num_assignees=6, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Bar, num=1, num_assignees=3, state_opts=dict(visitor_capacity=30))
    ],
    person_routine_assignment=DefaultPersonRoutineAssignment())

test_config = PandemicSimConfig(
    num_persons=100,
    location_configs=[
        LocationConfig(Home, num=30),
        LocationConfig(GroceryStore, num=1, num_assignees=5, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Office, num=1, num_assignees=150, state_opts=dict(visitor_capacity=0)),
        LocationConfig(School, num=10, num_assignees=2, state_opts=dict(visitor_capacity=30)),
        LocationConfig(Hospital, num=1, num_assignees=30, state_opts=dict(patient_capacity=2)),
        LocationConfig(Restaurant, num=1, num_assignees=3, state_opts=dict(visitor_capacity=10)),
        LocationConfig(Bar, num=1, num_assignees=3, state_opts=dict(visitor_capacity=10)),
    ],
    person_routine_assignment=DefaultPersonRoutineAssignment())
