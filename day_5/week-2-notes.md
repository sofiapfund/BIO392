## Genome Analysis Technologies

### Non-Sequence Genomics
1. Cytogenetics (chromosomal analysis - **no** knowdlege about sequence alterations needed)
2. Comparative Genomic Hybridization (CGH - **indirect** attribution of involved target genes)
3. Array Comparative Genomic Hybridization (aCGH - **direct** attribution of involved target genes)

### Genome Analysis
* SNP Genotyping: only look at specific alterations in the genomes

* Whole Exome Sequencing: only look at the part of the genome that contains protein coding genes (exomes)

* Sanger Sequencing vs. NGS 

* Advantage of Nanopore sequencing: can sequence very long reads (**cons**: fidelity not very high: not good to identify new SNPs and for disease diagnostics! **pros**: identify DNA of known composition and for de-novo assembly for telomere/repeat regions)

* sequences like telomeres and centromeres have a lot of repeat and are hard to sequence 

* exome sequencing: information about exomes is extracted by means of reverse transcription (aka starting from RNA)

* target gene panel: very high depth and precise, but you will miss out on a lot of information (not good to study unknown variants; only good to find whether known variants are present ▶️ good for diagnostics)

### Genomic File Formats

* ‼️ **one 30x BAM file = 100 GB**
* either **text** or **binary** formats are used 
* what are possible ways to compress a **BAM** even more? Comparison to a reference genome: only store the differences compared to the reference genome (**CRAM**): there is an API for this ▶️ RefGet
* ‼️ VCF (**slide 15**): variant call format ▶️ why "call"? 
    * 😄 good because you don't have to store sequences
    * 😞 inefficient when you have many samples: with 1000s of individuals it gets messy    
    * in a given population, most calls are from frequent variants 
    * 😞 not good for structure variants 

## Genome Editions

* mess with genome editions: how do you count bases in the genome? Genomic data has to be evaluated in the context of the correct edition!
* reference genome that is used as standard now: GRCh38
* ‼️ **250 Mb**: size of chr1 (it's the largest chromosome) - **47 Mb**: size of smallest chromosome (chr21)
* **3 Gb**: size of the whole genome
* tools for genome reading: e.g. `samtools`, `bcftools`, ... (recall: week 1 bash)

### Genome Liftover
* moving between different genome editions (e.g., from edition 19 to edition 38), e.g. using a Python tool like `segment_liftover`: shifts from change in regional lenths are defined in *chain files*
* ‼️ Task: read up on liftover techniques (check their article)
* use positional scaffolding: use info about which regions have been re-assigned

## Genome Resources
Many different places where sequences are stored.

* **UCSC Genome Browser**: 
   * most widely used general genome browser
   * costumization with BED files
   * lots of genome editions available
   * genomes from many species
* **NCBI**:
   * where reference genome data is stored
   * lots of human variants are stored here
* **ENSEMBL**:

### Resources for genome variant data
* NCBI:dbSNP, NCBI:dbVAR, NCBI:ClinVar, EMBL-EBI:EVA

### Resources for cancer genomics
* COSMIC

### Beyond a single resource: federation
* data sharing approaches: combine all the data from different resources
* ‼️ federated approach: connecting national genomic initiatives (original data stays on the local resoures): you don't get access to the data itself, but you get back information about the existance of a certain variant in a certain database
* **Progenetix**: focus on data aggregation and curation; most of the data is coming from genomic arrays
* **CURIES**: compact URIs 👉 used to identify resources (prefix + code, e.g. PMID:1234567)

## BLAST


## Terminology
* Gb = Giga bases

* BAC = bacterial artificial chromosome

* YAC = yeast artificial chromosome

