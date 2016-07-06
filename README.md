# **Aligner**

### What
**Aligner** is a tool for [FASTA] (https://en.wikipedia
.org/wiki/FASTA_format) DNA sequence alignment.


### How to use
**Aligner** is fairly simple to use.  All you need is a standard FASTA text
file (*.txt).

By the way, included in this package are two example files (fasta_example_1
.txt,
fasta_example_2.txt).

In order to install,

```
pip install sequence_aligner
```

To use aligner from the command line, you run the following commands:

```
aligner [-h] --file_path FILE_PATH [--storage_path STORAGE_PATH] [--results_name
RESULTS_NAME]
```

FILE PATH is the path to the fasta sequence text file.

While FILE PATH is required, STORAGE_PATH and FILE_NAME are optional.

By default, the result file will be stored in the following generated directory:
`/tmp/sequence_results`

And the file name will be generated with the following pattern:
`sequence_read-<datetime here>.txt` for example: `sequence_read-2016-07-01T16.42.21.246183.txt`

Once you run the command line, within seconds, your results will be
generated, and you'll receive a print out of the location and name of your file.

For example:
```Sequence Alignment results stored --> /tmp/sequence_results/sequence_read-2016-07-01T17.59.48.458859.txt```


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

## Caveats/Issues
* One issue I dealt with was speed.  After many iterations of 
refactoring, I was able to bring runtime down from ~45-50 min to ~10-11
 min. 
* This program assumes that sequences overlap and that there are no 
mutations.

## Next Steps
* Improve efficiency
* Improve 'match-iness' algorithm -- right now, my 'score' is merely 
based on length of overlap at a given state of the anchor sequence.
More preprocessing could be done before commencing alignment in order
 to score the level of 'matchiness' between all pairs of sequences.  

