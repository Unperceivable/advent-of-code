import unittest
from volcanium import Volcanium
class TestVolcanium(unittest.TestCase):

    puzzle_input = ["Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
                    "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
                    "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
                    "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
                    "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
                    "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
                    "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
                    "Valve HH has flow rate=22; tunnel leads to valve GG",
                    "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
                    "Valve JJ has flow rate=21; tunnel leads to valve II",]
        
    def test_part_one(self):
        volcanium = Volcanium(self.puzzle_input)
        expected_result = 1651
        self.assertEqual(volcanium.max_pressure_release(), expected_result)
    
    def test_part_two(self):
        pass