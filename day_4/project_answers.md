# Theory


# Answers for the 1000 genomes data project - 2022/09/23

**Q1 - Which family of mobile elements has the most insertions?**

13_Heterochrom/lo (2334 insertion sites)

**Q2 - How many insertions are there in exons? What do we expect?**

110: nr of insertions sites in exons

3225: tot nr of insertion sites

Expected: not many insertions, cause they could lead to non-functional gene products. More insertions should happen in non-coding regions, where indels don't have that big of a functional impact... 

It therefore makes sense that the mobile elements with the most insertions are the one in heterocromatine (non-coding regions).


**Q3 - How can we quantify those?**

Use the following command to quantify nr of insertions site in exons:
```
bedtools intersect -a CEU.low_coverage.2010_10.MobileElementInsertions.sites.vcf -b exons_nochr.bed | wc -l
```

Notes: 
1. the utilities offered by `bedtools` allow to compare files of different formats (i.e., .vcf and .bed) automatically
2. remove "chr" in the .bed file so that it can be compared with the .vcf file (`exons.bed` ▶️ `exons_nochr.bed`)


**Q4 - Given the low abundance in exons, where do they jump?
Promoters? enhancers? heterochromatin? other repetitive elements?**

Jumps are manly occuring in heterochromatine.

**Q5 - What can we use as a reference, how do we assign `functions' to all nucleotides in a genome?**

Usually functions are assigned based on similarity of the coding sequences to sequences of known genes (similar sequences ▶️ similar function). Different ways to measure sequence similarity exist. 
