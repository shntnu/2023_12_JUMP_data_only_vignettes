# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3.10.6 ('datasets-WmsNNUi2')
#     language: python
#     name: python3
# ---
# ruff: noqa: E402

# %% [markdown]
# # Loading profiles from the JUMP Cell Painting Datasets
# This notebook loads a small number of plates with precomputed features and the metadata information.
# ## Import libraries

# %%
import os
import pandas as pd

# %% [markdown]
# ## Helper functions

# %%
profile_formatter = (
    "s3://cellpainting-gallery/cpg0016-jump/"
    "{Metadata_Source}/workspace/profiles/"
    "{Metadata_Batch}/{Metadata_Plate}/{Metadata_Plate}.parquet"
)

loaddata_formatter = (
    "s3://cellpainting-gallery/cpg0016-jump/"
    "{Metadata_Source}/workspace/load_data_csv/"
    "{Metadata_Batch}/{Metadata_Plate}/load_data_with_illum.parquet"
)

# %% [markdown]
# ## Load metadata
#
# The following files contain the metadata information for the entire dataset.
# The schema is [here](metadata/README.md).

# %%
# Base URL for the raw GitHub content
BASE_URL = "https://raw.githubusercontent.com/jump-cellpainting/datasets/50cd2ab93749ccbdb0919d3adf9277c14b6343dd/metadata"

# Define the file paths
files = {
    "plates": f"{BASE_URL}/plate.csv.gz",
    "wells": f"{BASE_URL}/well.csv.gz",
    "compound": f"{BASE_URL}/compound.csv.gz",
    "orf": f"{BASE_URL}/orf.csv.gz",
}

# Load the data directly from GitHub
plates = pd.read_csv(files["plates"])
wells = pd.read_csv(files["wells"])
compound = pd.read_csv(files["compound"])
orf = pd.read_csv(files["orf"])

# %% [markdown]
# ## Sample plates
# Let's sample two plates of a certain type (encoded in `Metadata_PlateType`) from each data-generating center (`Metadata_Source`). Note that only 10 out of the 13 sources are currently available and `source_1` does not have the plate type being queried below.

# %%
sample = (
    plates.query('Metadata_PlateType=="TARGET2"')
    .groupby("Metadata_Source")
    .sample(2, random_state=42)
)
sample

# %% [markdown]
# `TARGET2` plates are "sentinel" plates that are run in each batch. More on all this in future updates.

# %% [markdown]
# ## Loading profiles
# Now let's load the profiles from these plates.
#
# Setting `columns = None` below will load all of the features.
#
# <div class="alert alert-warning">
# WARNING: Files are located in S3. This loop loads only two features per each sampled plate; loading many features and/or many plates can take several minutes.
# </div>

# %%
columns = [
    "Metadata_Source",
    "Metadata_Plate",
    "Metadata_Well",
    "Cells_AreaShape_Eccentricity",
    "Nuclei_AreaShape_Area",
]

import polars as pl

# Create a list of S3 paths first
s3_paths = [profile_formatter.format(**row.to_dict()) for _, row in sample.iterrows()]

# Read and concatenate all parquet files in one go
dframes = pl.concat(
    [
        pl.scan_parquet(
            path,
        )
        .select(columns)
        .collect()
        for path in s3_paths
    ]
)

# %% [markdown]
# Each row in `dframes` is well-level profile, containing thousands of features (n=4762) averaged over (typically) a couple of thousand cells per well.

# %% [markdown]
# ## Join features with metadata
#
# The profiles are annotated with only three columns of metadata (source, plate, well).
#
# Let's add more metadata!

# %%
dframes = dframes.to_pandas()
metadata = compound.merge(wells, on="Metadata_JCP2022")
ann_dframe = metadata.merge(
    dframes, on=["Metadata_Source", "Metadata_Plate", "Metadata_Well"]
)

# %% [markdown]
# We now know a little bit more about each profile:

# %%
ann_dframe.sample(2, random_state=42)

# %% [markdown]
# More metadata information will be added in the future.

# %% [markdown]
# ## Plot features
#
#
# The scatterplot below contains every well in the sampled dataset.
#
# In the interactive plot (see settings for `pio.renderers.default` above), you can hover over the points to see the JCP ID and the InChiKey for a given compound.
#
# <div class="alert alert-warning">
# NOTE: Because these are raw, unnormalized features, you will notice discernable clusters corresponding to each source due to batch effects.
# Upcoming data releases will included normalized features, where these effects are mitigated to some extent.
# </div>

# %%

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=ann_dframe,
    x="Cells_AreaShape_Eccentricity",
    y="Nuclei_AreaShape_Area",
    hue="Metadata_Source",
    alpha=0.6,
)

plt.title("Cell Eccentricity vs Nuclear Area by Source")
plt.legend(title="Source", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.tight_layout()
plt.show()


# %% [markdown]
# So that's just a couple of (raw) measurements from the sentinel plates for 12/13 of the sources, for the principal dataset alone.

# %% [markdown]
# ## Load images
#
# [LoadData](https://cellprofiler-manual.s3.amazonaws.com/CPmanual/LoadData.html) CSV files provide Metadata associated with the images to be processed.

# %%
load_data = []
for _, row in sample.iterrows():
    s3_path = loaddata_formatter.format(**row.to_dict())
    load_data.append(pd.read_parquet(s3_path, storage_options={"anon": True}))
load_data = pd.concat(load_data)

# %% [markdown]
# Let's pick a row at random and inspect it

# %%
sample_loaddata = load_data.sample(1, random_state=42)
pd.melt(sample_loaddata)

# %% [markdown]
# The `Metadata_` columns can be used to link the images to profiles.
# Let's pick a profile and view it's corresponding image.

# %%
sample_profile = ann_dframe.sample(1, random_state=22)
sample_profile.melt()

# %% [markdown]
# First link the profile to its images.
# These are well-level profiles, and each well has typically 9 sites imaged.

# %%
sample_linked = pd.merge(
    load_data, sample_profile, on=["Metadata_Source", "Metadata_Plate", "Metadata_Well"]
)
sample_linked[["Metadata_Well", "Metadata_Site"]]

# %% [markdown]
# Inspect details of a single site for this profile

# %%
sample_linked.iloc[:1].melt()

# %% [markdown]
# Now load and display a single channel of this 5-channel image

# %%
from io import BytesIO
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import boto3
from botocore import UNSIGNED
from botocore.config import Config

image_url = os.path.join(
    sample_linked.iloc[0].PathName_OrigDNA, sample_linked.iloc[0].FileName_OrigDNA
)
s3_client = boto3.client("s3", config=Config(signature_version=UNSIGNED))
response = s3_client.get_object(
    Bucket=image_url.split("/")[2], Key="/".join(image_url.split("/")[3:])
)
image = mpimg.imread(BytesIO(response["Body"].read()), format="tiff")

plt.imshow(image, cmap="gray")
image_url

# %% [markdown]
# That should get you started. Check out the remaining notebooks to learn more about the dataset and how to use it.
