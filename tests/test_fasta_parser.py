import unittest

from sequence_aligner.fasta_parser import FastaParser as FP

__author__ = 'tiffany'


class TestFastaParser(unittest.TestCase):
    def setUp(self):
        self.test_file_path = './test_fasta_sequences.txt'

    def tearDown(self):
        pass

    def test_get_sequence_list(self):
        fp = FP(self.test_file_path)
        actual = fp.get_sequence_list()
        expected = ['ATTAGACCTG', 'CCTGCCGGAA', 'AGACCTGCCG', 'GCCGGAATAC']

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
