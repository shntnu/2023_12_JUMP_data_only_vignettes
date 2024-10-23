# Loading JUMP Data

## Basic Data Loading

```python
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Load metadata
plates = pd.read_csv("metadata/plate.csv.gz")
wells = pd.read_csv("metadata/well.csv.gz")
compound = pd.read_csv("metadata/compound.csv.gz")
orf = pd.read_csv("metadata/orf.csv.gz")

# Configure profile paths
profile_formatter = (
    "s3://cellpainting-gallery/cpg0016-jump/"
    "{Metadata_Source}/workspace/profiles/"
    "{Metadata_Batch}/{Metadata_Plate}/{Metadata_Plate}.parquet"
)

# Example: Sample plates from each source
sample = (
    plates.query('Metadata_PlateType=="TARGET2"')
    .groupby("Metadata_Source")
    .sample(2, random_state=42)
)

# Load profiles from sampled plates
dframes = []
columns = [
    "Metadata_Source",
    "Metadata_Plate",
    "Metadata_Well",
    "Cells_AreaShape_Eccentricity",
    "Nuclei_AreaShape_Area",
]

for _, row in sample.iterrows():
    s3_path = profile_formatter.format(**row.to_dict())
    dframes.append(
        pd.read_parquet(s3_path, storage_options={"anon": True}, columns=columns)
    )
dframes = pd.concat(dframes)

# Add metadata to profiles
metadata = compound.merge(wells, on="Metadata_JCP2022")
ann_dframe = metadata.merge(
    dframes, on=["Metadata_Source", "Metadata_Plate", "Metadata_Well"]
)
```

## Loading Images

```python
# Configure image paths
loaddata_formatter = (
    "s3://cellpainting-gallery/cpg0016-jump/"
    "{Metadata_Source}/workspace/load_data_csv/"
    "{Metadata_Batch}/{Metadata_Plate}/load_data_with_illum.parquet"
)

# Load image metadata
load_data = []
for _, row in sample.iterrows():
    s3_path = loaddata_formatter.format(**row.to_dict())
    load_data.append(pd.read_parquet(s3_path, storage_options={"anon": True}))
load_data = pd.concat(load_data)

# Example: Link profiles to images
sample_profile = ann_dframe.sample(1, random_state=22)
sample_linked = pd.merge(
    load_data, sample_profile, on=["Metadata_Source", "Metadata_Plate", "Metadata_Well"]
)

# Access image paths
image_paths = sample_linked[["Metadata_Well", "Metadata_Site"]]
```

## Notes

- Each well-level profile contains thousands of features (n=4762) averaged over cells
- Typical well contains a couple thousand cells
- TARGET2 plates are sentinel plates run in each batch
- Image files are stored as 5-channel TIFF files

For more examples, see our [how-to guides](../howto/).
