#!/usr/bin/python
# coding= utf8

""" In this module resides the engine of the Sequence Aligner."""
from datetime import datetime


class SequenceAligner(object):
    """ The SequenceAligner is a machine that takes a list of sequence
    fragments and constructs them into one read based on the overlaps.

    """

    def __init__(self, sequence_list):
        self.sequence_list = sequence_list
        self.anchor_sequence = None
        self.__index_left = 0
        self.__index_right = 0
        self.__current_sequence = None
        self.__score_card = dict()

    def __score_overlaps(self):
        # iterate through the sequence_list
        # for each pair, determine the overlap
        # score = abs(len(overlap_seq1) - len(overlap_seq2))/float(max(len(
        # overlap_seq1, overlap_seq2))
        # with each pass, check if length is max, and if so, then update
        for i1 in range(len(self.sequence_list) - 1):
            for i2 in range(1, len(self.sequence_list)):
                pass

    def __check_overlap(self):


    def __find_overlapping_substring(self):
        """
        Finding overlapping substrings
        - Take two sequences (anchor_sequence and sequence), and split the
          sequence by more than half.
        - Check to see if sub-sequence is in the anchor_sequence.
        - If not, walk down  sub - sequence down the full length of sequence,
          checking to see if it exist in anchor_sequence.
        - If a match is not found by the end of sequence, append to the end of
          the sequence_list, to try again later, when anchor is more fleshed
          out.
        - If match is found with sub-sequence, return sub-sequence.
        :return: sub_sequence: string
        """
        sub_sequence = ''
        self.__index_left = 0
        for self.__index_right in \
                range(len(self.__current_sequence) / 2 + 1,
                      len(self.__current_sequence)): # make len(curr_seq) - 1

            sub_sequence = \
                self.__current_sequence[self.__index_left:self.__index_right]

            if sub_sequence not in self.anchor_sequence: #regex findall trick
                if self.__index_right == len(self.__current_sequence) - 1:
                    self.sequence_list.append(self.__current_sequence)
                    # return sub_sequence
                    break
                self.__index_left = self.__index_left + 1
            else:
                return sub_sequence
        return sub_sequence

    def __check_for_left_matches(self, sub_sequence_match):
        """
        Checking for matches left of sub_sequence match
        - If the index_left >0, then keep extending left of the
          sub_sequence_match
        - Check to see if that match with left extension is found in anchor
          sequence
        - Stop when extension reaches far left or match found and return the
          left-extended sub_sequence
        :param sub_sequence_match: string
        :return: sub_sequence_left: string
        """

        left_match = True
        while self.__index_left > 0 and left_match:
            next_left = self.__index_left - 1 # temp
            next_seq = self.__current_sequence[next_left:self.__index_right] # t
            if next_seq in self.anchor_sequence:
                sub_sequence_match = \
                    self.__current_sequence[self.__index_left:self.__index_right]
                self.__index_left = self.__index_left - 1
                left_match = True
            else:
                left_match = False

        return sub_sequence_match

    def __check_for_right_matches(self):
        """
        Checking for matches right of sub_sequence match
        - If the index_right is less than the length of sequence, then keep
          extending right of the sub_sequence match
        - Check if match with right extension is found in anchor sequence
        - Stop when extension reaches far right or match found and return the
          right-extended sub_sequence
        :return: sub_sequence_right: string
        """
        sub_sequence_right = ''
        right_match = True
        current = self.__current_sequence
        while self.__index_right < len(current) and right_match:
            next_right = self.__index_right + 1 # temp
            c = current[self.__index_left:self.__index_right + 1]  # temp
            if current[self.__index_left:self.__index_right + 1] \
                    in self.anchor_sequence:

                sub_sequence_right = sub_sequence_right + \
                                     current[self.__index_right]

                self.__index_right = self.__index_right + 1
                right_match = True
            else:
                right_match = False
        return sub_sequence_right

    def __add_right_left_hang(self, sub_sequence_full):
        """
        Adding the additional left and/or right hanging characters from
        anchor_sequence
        - First, find the anchor_sequence index where the match with
        sub_sequence starts
        - check for sequence left and right of where the match starts on
        anchor_sequence, and add accordingly
        - check for sequence left and right of where match starts on sequence,
        if so, and add accordingly
        :param sub_sequence_full: string
        :return: sub_sequence_full: string
        """
        as_left_align_index = self.anchor_sequence.find(sub_sequence_full)
        s = self.anchor_sequence[:as_left_align_index] # t
        if self.anchor_sequence[:as_left_align_index]:
            sub_sequence_full = \
                self.anchor_sequence[:as_left_align_index] + sub_sequence_full
        s = self.__current_sequence[:self.__index_left] # t
        if self.__current_sequence[:self.__index_left]:
            sub_sequence_full = \
                self.__current_sequence[:self.__index_left] + sub_sequence_full

        fr_rightmost_index = as_left_align_index + \
                             (self.__index_right - self.__index_left)
        s = self.anchor_sequence[fr_rightmost_index:] # t
        if self.anchor_sequence[fr_rightmost_index:]:
            sub_sequence_full = \
                sub_sequence_full + self.anchor_sequence[fr_rightmost_index:]
        s = self.__current_sequence[self.__index_right:] # t
        if self.__current_sequence[self.__index_right:]:
            sub_sequence_full = \
                sub_sequence_full + self.__current_sequence[self.__index_right:]
        return sub_sequence_full

    def __check_for_false_match(self, sub_sequence_full):
        as_left_align_index = self.anchor_sequence.find(sub_sequence_full)
        if self.__current_sequence[:self.__index_left] and \
            self.anchor_sequence[:as_left_align_index]:
            return False
        as_rightmost_index = as_left_align_index + len(self.__current_sequence)
        if self.anchor_sequence[as_rightmost_index:] and \
            self.__current_sequence[self.__index_right:]:
            return False
        return True

    def get_aligned_sequence(self):
        """
        Aligns list of sequences
        Iterate through list of sequences to generate final, anchor_sequence
        :return: final, single constructed sequence
        """
        self.anchor_sequence = self.sequence_list[0]

        list_index = 1
        while list_index < len(self.sequence_list):
            self.__current_sequence = self.sequence_list[list_index]
            if self.anchor_sequence == self.__current_sequence:
                list_index = list_index + 1
                continue

            sub_sequence_match = self.__find_overlapping_substring()

            if sub_sequence_match:
                sub_sequence_left = \
                    self.__check_for_left_matches(sub_sequence_match)

                sub_sequence_right = self.__check_for_right_matches()

                sub_sequence_full = sub_sequence_left + sub_sequence_right

                if not self.__check_for_false_match(sub_sequence_full):
                    self.sequence_list.append(self.__current_sequence)
                    continue
                sub_sequence_fuller = \
                    self.__add_right_left_hang(sub_sequence_full)

                self.anchor_sequence = sub_sequence_fuller

            print "moving to sequence {}/{}.....{}%".format(
                list_index + 1,
                len(self.sequence_list),
                float(list_index + 1) /
                float(len(self.sequence_list)))
            print "anchor length now: {}".format(len(self.anchor_sequence))
            list_index = list_index + 1

        return self.anchor_sequence
