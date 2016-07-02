#!/usr/bin/python
# coding= utf8

"""This module is responsible for parsing FASTA files."""

import re


class FastaParser(object):
    """
    FastaParser takes a path to a FASTA sequence file,
    parses the file (stripping the sequence identification, returning a
    list of the parsed sequences.
    """
    def __init__(self, fasta_file_path):
        self.file_path = fasta_file_path

    @staticmethod
    def __extract_fasta_string_from_file(file_path):
        fasta_file = open(file_path, 'r')
        fasta_string = fasta_file.read()
        return fasta_string

    @staticmethod
    def __split_fasta_string_to_list(fasta_string):
        regex_pattern = re.compile('^>.+$', re.MULTILINE)
        return re.split(regex_pattern, fasta_string)

    @staticmethod
    def __filter_fasta_list(unfiltered_fasta_list):
        filter_fasta_list = filter(None, unfiltered_fasta_list)
        return [sequence.replace('\n', '') for sequence in filter_fasta_list]

    def get_sequence_list(self):
        """
        Gets the list of sequences.
        :return: list string of sequences
        """
        fasta_string = self.__extract_fasta_string_from_file(self.file_path)
        fasta_list = self.__split_fasta_string_to_list(fasta_string)
        return self.__filter_fasta_list(fasta_list)
