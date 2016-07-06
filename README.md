# **Aligner**

### What
**Aligner** is a tool for [FASTA] (https://en.wikipedia
.org/wiki/FASTA_format) DNA sequence alignment.



### How to use
**Aligner** is fairly simple to use.  All you need is a standard FASTA text
file (*.txt).

In order to install,

```
pip install SequenceAligner
```

To use aligner from the command line, you run the following commands:

```
aligner [-h] --file_path FILE_PATH [--storage_path STORAGE_PATH] [--results_name RESULTS_NAME]
```

FILE PATH is the path to the fasta sequence text file.

While FILE PATH is required, STORAGE_PATH and FILE_NAME are optional.

By default, the result file will be stored in the following generated directory:
`/tmp/sequence_results`

and the file name will be generated with the following pattern:
`sequence_read-<datetime here>.txt` for example: `sequence_read-2016-07-01T16.42.21.246183.txt`

Once you run the commands, your results will start generating.  
Once completed (for 50 sequence of ~1000 bp, expected ~ 11 min), you'll 
receive a print out of the location and name of your file.

For example:

```Sequence Alignment results stored --> /tmp/sequence_results/sequence_read-2016-07-01T17.59.48.458859.txt```

By the way, included in this package are two example files (fasta_example_1
.txt, fasta_example_2.txt).



### How it works
In order to align sequences, first, I created a dictionary of all 
subsequences from the size 'greater than half' to full length.  

One sequence in the list of sequences was designated the "anchor 
sequence".  

I gathered that at any given state of the anchor sequence, there 
would exist a sequence with the the greatest overlap.  Iterating 
through the sequence list,  the sequence with the 
sub-sequence (from the dictionary mentioned above) having the 
greatest 'score' is identified.  The score is based on the amount of 
overlap with the anchor sequence.  This subsequence is then merged 
into the anchor sequence.  This iteration continues until all 
sequences in the sequence list have been merged into the anchor 
sequence.  



### Caveats/Issues
* One issue I dealt with was speed.  After many iterations of 
refactoring, I was able to bring runtime down from ~45-50 min to ~10-11
 min. 
* This program assumes that sequences overlap and that there are no 
mutations.
* It is also assumed that all overlaps between pairs occur at greater 
than half.



### Next Steps
* Improve efficiency/runtime with additional optimizations.
* Introduce pre-processing to improve efficiency/runtime and account for 
data sets with multiple sequences at any given step that may have the 
highest ‘score’ or circumstances where choosing the highest ‘score’ at a 
given step will allow all sequences in the data set to be aligned. 
One method would be to pre-process each sequence to determine whether 
it is ‘matchy’ with every other sequence - where ‘matchy’ is defined as 
at greater than 50% overlap and the degree of ‘matchy-ness’ is 
determined by the amount of overlap of the 2 sequences. Matrixes which 
determine the degree of overlap of the 2 sequences could be used in the 
pre-processing and could reduce the need to determine all possible 
sub-sequences within the comparison of 2 sequences. Once pre-processing 
is completed, for the first sequence determine the second sequence to 
align with it based on the sequence with highest ‘matchy-ness’ score 
with the first sequence. Since the pre-processed ‘matchy-ness’ of the 
second sequence selected with all other sequences has been determined, 
limited additional processing of the matchy-ness would be needed to 
determine the third sequence to align. If you encounter a situation in 
which there are no matchy sequences to align and all sequences have not 
yet been aligned - walk back to the last sequence which had at least 2 
matchy sequences and choose the next highest score and repeat align the 
most matchy sequences from that step (while avoiding additional 
processing). 
