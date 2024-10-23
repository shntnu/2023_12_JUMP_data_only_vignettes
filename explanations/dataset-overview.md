# JUMP Dataset Overview

## Dataset Collection

This collection comprises 4 datasets:

- Principal dataset (`cpg0016`): 116k chemical and >15k genetic perturbations created in tandem, split across 12 data-generating centers using human U2OS osteosarcoma cells
- 3 pilot datasets testing:
  - Different perturbation conditions (`cpg0000`, including different cell types)
  - Staining conditions (`cpg0001`)
  - Microscopes (`cpg0002`)

## Design of the Dataset

### Cell Line Selection

- We chose U2OS (osteosarcoma) cells for our major data production work
- Selected for robustness and wide use in screening applications

### Perturbation Types

- **Genetic Perturbations:**
  - CRISPR knockdowns of subset of genome
  - ORF (overexpression) reagents with some overlap with CRISPR targets
- **Chemical Perturbations:**
  - Partners exchanged ~120,000 compounds
  - ~5 replicates of each compound
  - Performed as 1-2 replicates at 3-5 different sites globally

### Control Sets

- **JUMP-Target:**
  - 306 compounds and corresponding genetic perturbations
  - Designed to assess connectivity in profiling assays
  - Includes 384-well plate maps
  - [Detailed documentation](https://github.com/jump-cellpainting/JUMP-Target)

- **JUMP-MOA:**
  - 90 compounds in quadruplicate
  - Represents 47 mechanism-of-action classes
  - Designed for assessing connectivity
  - [Documentation available](https://github.com/jump-cellpainting/JUMP-MOA)

- **Positive Controls:**
  - Set of 8 compounds per sample plate
  - [List of recommended controls](https://github.com/jump-cellpainting/JUMP-Target#positive-control-compounds)

## Available Components

### Principal Dataset Components

From 12 sources (data-generating centers):

- Raw microscopy images
- CellProfiler analysis output
- Single-cell profiles
- Aggregated profiles
- Complete metadata files

### Data Processing Levels

1. **Images**
   - 5 channels (DNA, RNA, ER, AGP, Mito)
   - Multiple sites per well
   - Quality-controlled microscopy data

2. **CellProfiler Output**
   - Feature extraction results
   - Cell segmentation data
   - Quality metrics

3. **Profile Data**
   - Single-cell level measurements
   - Well-aggregated profiles
   - Normalized features
   - Feature selection applied

4. **Assembled Subsets**
   - Combined datasets in parquet format
   - URLs available in [profile index](https://github.com/jump-cellpainting/datasets/blob/main/manifests/profile_index.csv)
   - Includes all data modalities in single dataframe

## Data Access

### AWS Storage

- Hosted on Cell Painting Gallery ([registry.opendata.aws/cellpainting-gallery/](https://registry.opendata.aws/cellpainting-gallery/))
- Free access through AWS Open Data Program

### Interactive Tools

1. **Ardigen JUMP-CP Explorer**
   - Free public access at [phenaid.ardigen.com/jumpcpexplorer](https://phenaid.ardigen.com/jumpcpexplorer/)
   - Search similarities between phenotypes and perturbations
   - Account creation required

2. **Spring Discovery JUMP-CP Portal**
   - Available at [springscience.com/jump-cp](https://www.springscience.com/jump-cp)
   - Data exploration interface
   - Requires account

### Programmatic Access

- Python package `jump_deps` available
- Notebooks and tutorials provided
- [Sample code available](https://github.com/jump-cellpainting/datasets/blob/main/sample_notebook.ipynb)

## Latest Updates

### Current Status

- All pilot dataset components available
- Principal dataset: most components available from 12 sources
- Key metadata files accessible
- Assembled profile subsets ready for analysis

### Coming Soon

- Extension of metadata and notebooks to pilots
- Curated compound annotations from ChEMBL
- Deep learning embeddings using pre-trained networks
- Simplified access tools and methods
  - `cpgdata`
  - `jump-portraits`
  - `jump-babel`

### Quality Notes

- Cross-modality matching still being improved
- Some wells/plates excluded for quality control
- Within-modality matching generally reliable

For the most current updates, subscribe to our [email list](https://jump-cellpainting.broadinstitute.org/more-info).
