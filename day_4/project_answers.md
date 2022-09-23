# Theory


# Answers for the 1000 genomes data project - 2022/09/23

**Q1 - Which family of mobile elements has the most insertions?**

**Q2 - How many insertions are there in exons? what do we expect?**

110.

**Q3 - How can we quantify those?**

Use the following command:
```
bedtools intersect -a CEU.low_coverage.2010_10.MobileElementInsertions.sites.vcf -b exons_nochr.bed | wc -l
```

Notes: 
1. the utilities offered by `bedtools` allow to compare files of different formats (i.e., .vcf and .bed) automatically
2. remove "chr" in the .bed file so that it can be compared with the .vcf file (`exons.bed` ▶️ `exons_nochr.bed`)

**Q4 - Which family of mobile elements has the most insertions?**

**Q5 - How many insertions are there in exons? what do we expect?**

**Q6 - How can we quantify those?**

Given the low abundance in exons, where do they jump?
Promoters? enhancers? heterochromatin? other repetitive elements?
What can we use as a reference, how do we assign `functions' to all nucleotides in a genome?
