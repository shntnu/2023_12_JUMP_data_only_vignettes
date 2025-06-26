# Notes and Frequently Asked Questions

## Analyses

### How can I reproduce an environment to explore JUMP data?

The easiest way to set things up will be installing from pip in your environment of choice:

```
pip install jump-deps
```

## Data

### Does JUMP contain my compound/gene of interest?

The easiest way to find out is to follow the instructions on the perturbation availability  [section](https://broadinstitute.github.io/jump_hub/howto/interactive/0_overview.html#perturbation-availability). Alternatively, you can explore the [metadata tables](https://github.com/jump-cellpainting/datasets/tree/main/metadata) on the datasets repository, which are used to generate the explorable table.

### Where are the datasets' specifications?

The main resource to understand the technicalities of the JUMP datasets collection and assembly is on this [repo](https://github.com/jump-cellpainting/datasets).

### Why do some samples have images but no downstream analysis?

Some plates failed Quality Control (QC) but we kept them because they may be useful for developing QC methods.

### Why do some perturbations have so many replicates? 

Some genetic and chemical perturbations are positive or negative controls (see next question) and thus appear frequently in the dataset.

### What are the identifiers for positive and negative controls?

You can find all positive and negative controls for JUMP-ORF, -CRISPR, and -compound [here](https://lite.datasette.io/?url=https://zenodo.org/api/records/13255965/files/babel.db/content#/babel/babel?_filter_column=pert_type&_filter_op=contains&_filter_value=con&_sort=rowid).
For the compounds dataset the only negative control is 'JCP2022_033924' (DMSO). 
Most chemical compound plates contain 16 negative control wells, while some have as many as 28 wells. In the ORF dataset, replicates are positioned in wells O23, O24, P23 and P24. The remaining wells contain ORF treatments, with a single replicate of each per plate map and with five replicate plates produced per plate map ([private link](https://github.com/jump-cellpainting/megamap/issues/8#issuecomment-1413606031) | [html](https://zenodo.org/records/15699904/files/megamap_no_replicates.html?download=1)).

### Which pipelines produced the final datasets?

Details on the pipelines at each step can be found on [this](../reference/computational_pipelines.md) page.

### Do we expect one gene’s JCP ID (JUMP Cell Painting ID) to be associated with multiple targets?

Yes, many genes are associated with multiple targets and are correctly annotated as such. For instance, `JCP2022_050797` (quinidine/quinine) has the targets `KCNK1` and `KCNN4`. Other genes are annotated as targeting genes in disparate families.

### Do JCP IDs within the compound dataset refer to the same compound?

Sometimes, two compounds were given separate JCP IDs because they had different names and `broad_sample` names. But after all of the data cleanup steps, they ended up being the same. Hence two different entries.

### Do JCP IDs within either the CRISPR or ORF datasets refer to the same gene?

In CRISPR, each JCP ID corresponds to a different gene. But in ORF there are frequently multiple reagents representing the same gene. In this case, we compute consensus profiles at the gene level by aggregating profiles by `Metadata_NCBI_Gene_ID` rather than by `Metadata_JCP2022`. This approach was selected after testing six different consensus strategies and evaluating their performance using phenotypic activity metrics ([private link](https://github.com/jump-cellpainting/morphmap/issues/178) | [html](https://zenodo.org/records/15699904/files/morphmap_consensus_profiles.html?download=1)).

## Quirks and details

There are additional details that are not commonly asked but it is important to retain on record. This is a compendium of those.

- Source 1 and 9 use higher-density plates (1536 vs the standard 384\)  
- Source 7 and 13 are the same laboratory
- In JUMP-Target there is an InChIKey that maps to 2 different perturbations: ‘LOUPRKONTZGTKE-UHFFFAOYSA-N’ maps to both quinidine and quinine.  
- The definition of controls, especially positive controls, can be tricky: Some are hard-coded in [broad\_babel](https://github.com/broadinstitute/monorepo/blob/febe56c27e490c110d8b5a871de974a4293176c6/libs/jump_babel/tools/gen_database.py#L70-L87), based on internal knowledge that was not recorded at the time of assembling the datasets. In certain datasets, such as JUMP-ORF, there are additional types of positive controls: poscon\_orf, poscon\_cp (compound probe), and poscon\_diverse.
- The treatment compounds were assayed at 10 uM for all sources, except for
source_7 where the compounds were assayed at 0.625 uM (the goal being to assay some of the
compounds at a low concentration in addition to the higher concentration used for most of data
production). The positive control compounds in compound, ORF and CRISPR plates were assayed at 5
uM. JUMP-Target-1-Compound and JUMP-Target-2-Compound plates were also assayed at 5 uM
- Due to some plates having letters and numbers and others only numbers, be careful when loading multiple `load_data_csv`s. We treat all columns as strings to avoid any potential casting issue.
