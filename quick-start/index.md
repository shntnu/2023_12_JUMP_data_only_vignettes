# Getting Started with JUMP

Welcome to JUMP (Joint Undertaking for Morphological Profiling)! This guide will help you start working with the dataset quickly.

## Choose Your Path

1. **Just exploring?**
   - Use our web interfaces:
     - [JUMP-CP Data Explorer](https://phenaid.ardigen.com/jumpcpexplorer/) by Ardigen
     - [JUMP-CP Data Portal](https://www.springscience.com/jump-cp) by Spring Discovery
   - No programming required
   - Free account creation needed
   - Search for similarities between phenotypes and perturbations

2. **Want to analyze data?**
   - **Local Setup**
     - Install dependencies: `pip install jump_deps` (Python 3.10 or 3.11)
     - Follow our [how-to guides](../howto/) for common analyses
     - Access data directly from AWS S3

   - **Cloud Analysis**
     - Use our [Terra workspace](terra-workspace.md)

3. **Looking to build tools?**
   - Use our Python libraries in the [monorepo](https://github.com/broadinstitute/monorepo/tree/main)
   - Access the [metadata schema](https://github.com/jump-cellpainting/datasets/tree/main/metadata)
   - Explore our [example notebooks](../howto/)

## Dataset Overview

- **Scale:**
  - 116k chemical perturbations
  - >15k genetic perturbations
  - Images from 12 centers
  - Multiple replicates per perturbation

- **Data Types:**
  - Raw microscopy images
  - CellProfiler output
  - Single-cell profiles
  - Aggregated profiles
  - Rich metadata

- **Access Methods:**
  - AWS S3 (free through Open Data Program)
  - Web interfaces
  - Programmatic access
  - Terra workspace

[Learn more about the dataset](../explanations/dataset-overview.md)

## Need Help?

- Check our [FAQ](../explanations/FAQ.md)
- Browse the [glossary](../explanations/glossary.md)
- Raise an [issue](https://github.com/jump-cellpainting/datasets/issues)
- Subscribe to updates at [jump-cellpainting.broadinstitute.org/more-info](https://jump-cellpainting.broadinstitute.org/more-info)
