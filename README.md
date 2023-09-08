# Bionicle: powerful command line tools for bioinformatics
Bionicle is based on the three main ideas:
* The Unix philosophy: 1) Write programs that do one thing and do it well. 2) Write programs to work together. 3) Write programs to handle text streams, because that is a universal interface.
many small talls for small tasks, but chained together they can be powerfule
* Integration with existing Unix command line tools; Bionicle thus enforces that all bioinformatics objects are handled in single lines. For example the fasta and fastq format will be converted to single lines. To allow identifying the handled object and prevent errors, all lines will start with the ID of the handled bioinformatics objects, eg fasta, gtf, fastq, sam, rm; Bionicle thus handles typical bioinformatics objects
* Not all tools are compatible with each other; the tool-name should quickly allow to identify which tools are compatible with each other; the tool name has three part input_ID-name-output_ID; for "custom" formats the id is ommited;  therefore read-fasta | fasta-subseq-fasta but not fasta-writer | fasta-subseq-fasta

# Example uses
## fasta

### filter a single fasta IDs

```
reader-fasta.py myfile.fasta | grep "ID_of_interest" | fasta-formater > outputfile.fasta
```
### filter several fasta IDs

```
reader-fasta.py myfile.fasta | fasta-subseq-fasta --fasta-ids "id1,id2,id3" | fasta-formater > outputfile.fasta
```

### extract subsequences from a fasta file

```
reader-fasta.py myfile.fasta | fasta-subseq-fasta --bed file.bed | fasta-formater > outputfile.fasta
```

### extract sequences flanking some entries

```
reader-fasta.py myfile.fasta | fasta-flanker-fasta --flank-leng 10 --bed file.bed | fasta-formater > outputfile.fasta
```


### get the length of each fasta sequence in a file

```
reader-fasta.py myfile.fasta | fasta-length
```

### convert fasta to fastq

```
reader-fasta.py myfile.fasta | fasta-2-fastq | fastq-writer > output.file
```