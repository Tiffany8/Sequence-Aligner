##### **Aligner**

### What
**Aligner** is a nifty tool for [FASTA] (https://en.wikipedia
.org/wiki/FASTA_format) DNA sequence alignment.

### How
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



