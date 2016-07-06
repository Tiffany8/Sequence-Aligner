#!/usr/bin/python
# coding= utf8

""" In this module resides the engine of the Sequence Aligner."""
import re
from datetime import datetime


class SequenceAligner(object):
    """ The SequenceAligner is a machine that takes a list of sequence
    fragments and constructs them into one read based on the overlaps.

    """

    def __init__(self, sequence_list):
        aset = set(sequence_list)
        self.anchor_sequence = aset.pop()
        self.sequence_list = list(aset)
        self.__curr_idx_left = 0
        self.__curr_idx_right = 0
        self.__anchor_idx_left = 0
        self.__anchor_idx_right = 0
        self.__current_sequence = None

    def __generate_subsequence_combos(self):
        combos = set()
        ss = datetime.now()
        range_start = len(self.__current_sequence)/2 + 1
        range_end = len(self.__current_sequence) + 1
        for start in xrange(range_start, range_end + 1):
            the_range = xrange(start, range_end)
            adds = [self.__current_sequence[left:right] for left, right
                           in enumerate(the_range, 0)]
            combos.update(adds)

        elapsed = datetime.now() - ss
        # print "time to generate combos- no regex: {} sec".format(elapsed.total_seconds())
        return combos

    def __check_for_false_match(self, max_seq):
        self.__anchor_idx_left = self.anchor_sequence.find(max_seq)
        self.__curr_idx_left = self.__current_sequence.find(max_seq)
        if self.__current_sequence[:self.__curr_idx_left] and \
                self.anchor_sequence[:self.__anchor_idx_left]:
            return False
        self.__anchor_idx_right = self.__anchor_idx_left + len(max_seq)
        self.__curr_idx_right = self.__curr_idx_left + len(max_seq)
        if self.anchor_sequence[self.__anchor_idx_right:] and \
                self.__current_sequence[self.__curr_idx_right:]:
            return False
        return True

    def __add_right_left_hang(self, seq_info):
        # matched_seq_info (full_seq, [matched_seq, curr_l, curr_r, a_l, a_r])

        seq_left = seq_info[1][1]
        seq_right = seq_info[1][2]
        matched_seq = seq_info[1][0]
        full_seq = seq_info[0]
        anchor_left = self.anchor_sequence.find(matched_seq)
        anchor_right = anchor_left + len(matched_seq)

        if self.anchor_sequence[:anchor_left]:
            matched_seq = \
                self.anchor_sequence[:anchor_left] + matched_seq
        if full_seq[:seq_left]:
            matched_seq = \
                full_seq[:seq_left] + matched_seq

        if self.anchor_sequence[anchor_right:]:
            matched_seq = \
                matched_seq + self.anchor_sequence[anchor_right:]
        if full_seq[seq_right:]:
            matched_seq = \
                matched_seq + full_seq[seq_right:]

        return matched_seq

    def get_aligned_sequence(self):
        # while self.sequence_list:
        start_full = datetime.now()
        # list_index = 0
        fail_count = 0
        while len(self.sequence_list) > 0 and fail_count != 5:
            # generate score card
            print "starting list item # {}".format(len(self.sequence_list))
            score_card = self.generate_score_card(self.sequence_list)

            # pull item where len is greatest
            print "score card len: {}".format(len(score_card))
            if not score_card:
                fail_count = fail_count + 1
                continue
            matched_seq_info = max(score_card.iteritems(),
                                   key=lambda x: len(x[1][0]))
            max_len = len(matched_seq_info[1][0])

            top_matches = [i for i in score_card.iteritems()
                            if len(i[1][0]) == max_len]
            print "top matches len {}".format(len(top_matches))

            for match in top_matches:
                matched_seq = match[1][0]
                # align the sequence
                self.anchor_sequence = self.__add_right_left_hang(match)

                self.sequence_list.remove(match[0])
            print "anchor seq len {}".format(len(self.anchor_sequence))
            # list_index = list_index + 1
        elapsed = datetime.now() - start_full
        print "Job completed at {}".format(datetime.now().isoformat())
        print "TOTAL TIME: {} min".format(elapsed.total_seconds())
        print "final sequence list len: {}".format(len(self.sequence_list))
        return self.anchor_sequence

    def generate_score_card(self, sequence_list):
        print "generating score card..{}".format(datetime.now().isoformat())
        start_score = datetime.now()
        # reset score card each time
        score_card = dict()
        # get sequence score
        print "length of seq list in gen score card {}".format(len(sequence_list))
        for list_index in xrange(len(sequence_list)):

            self.__current_sequence = sequence_list[list_index]
            #  generate subsequence combos

            cc = current_combos = self.__generate_subsequence_combos_no_regex()
            print "pre-filter combination list len: {}".format(len(cc))

            # filter out those not found in anchor sequence
            ss = datetime.now()
            sa = self.anchor_sequence
            matched_combo_list = set([s for s in cc if s in
                                      sa[:min(len(sa), len(s))]
                                      or s in sa[-min(len(sa), len(s)):]])
            print "post-filter combination list len: {}".format(len(matched_combo_list))
            # print "len of all strings in list".format([len(i) for i in matched_combo_list])
            # matched_combo_list = filter(lambda x: x in self.anchor_sequence,
            #                             current_combos)
            elapsed = datetime.now() - ss
            print "time to filer combo list {}".format(elapsed.total_seconds())
            # if there are matches, then move forward
            if not matched_combo_list:
                continue
            ss = datetime.now()
            # find the max lengthed matching combo
            max_seq = max(matched_combo_list, key=len)
            elapsed = datetime.now() - ss
            # print "time to find max len combo {} sec".format(
            #     elapsed.total_seconds())

            # exclude matches with non-matching overhangs
            if not self.__check_for_false_match(max_seq):
                continue

            # store in score_card
            start = datetime.now()
            score_card[self.__current_sequence] = [
                max_seq,
                self.__curr_idx_left,
                self.__curr_idx_right]
            elapsed = datetime.now() - start
            # print "time to store in dictionary {} sec".format(elapsed.total_seconds())
        elapsed = datetime.now() - start_score
        print "score card generation total time {} seconds".format(elapsed.total_seconds())
        return score_card
