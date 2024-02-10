import unittest
from decoder import Decoder

class TestDecoder(unittest.TestCase):

    puzzle_input_a = "8A004A801A8002F478"
    puzzle_input_b = "620080001611562C8802118E34"
    puzzle_input_c = "C0015000016115A2E0802F182340"
    puzzle_input_d = "A0016C880162017C3686B18A3D4780"
    
    def test_part_one(self):
        decoder = Decoder(self.puzzle_input_a)
        expected_result =  16
        self.assertEqual(decoder.sum_version_numbers(), expected_result)
        decoder = Decoder(self.puzzle_input_b)
        expected_result =  12
        self.assertEqual(decoder.sum_version_numbers(), expected_result)
        decoder = Decoder(self.puzzle_input_c)
        expected_result =  23
        self.assertEqual(decoder.sum_version_numbers(), expected_result)
        decoder = Decoder(self.puzzle_input_d)
        expected_result =  31
        self.assertEqual(decoder.sum_version_numbers(), expected_result)

    def test_part_two(self):
        pass