import unittest
from sequence_aligner import SequenceAligner as SA


class TestSequenceAligner(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sequence_aligner(self):
        sequence_list = ['ATTAGACCTG',
                         'CCTGCCGGAA',
                         'AGACCTGCCG',
                         'GCCGGAATAC']
        sa = SA(sequence_list)
        actual = sa.get_aligned_sequence()
        expected = 'ATTAGACCTGCCGGAATAC'
        self.assertEqual(expected, actual)
