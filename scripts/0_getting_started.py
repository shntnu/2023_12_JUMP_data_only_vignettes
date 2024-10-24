# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3.10.6 ('datasets-WmsNNUi2')
#     language: python
#     name: python3
# ---

# # Loading profiles from the JUMP Cell Painting Datasets
# This notebook loads a small number of plates with precomputed features and the metadata information.
# ## Import libraries

# +
import io
import os
import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "png"  # Set to "svg" or "png" for static plots or "notebook_connected" for interactive plots
# -

# ## Helper functions

# +
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
# -

# ## Load metadata
#
# The following files contain the metadata information for the entire dataset.
# The schema is [here](metadata/README.md).

if "WORKSPACE_BUCKET" in os.environ:
    # This notebook is running on Terra.
    # Notebook 'workspace_setup.ipynb' cloned the git repo to this directory under $HOME.
    # If you cloned this repository manually to a different directory, edit this value to reflect that location.
    GIT_CLONE_DIR = "~/jump-cellpainting-datasets"
else:
    GIT_CLONE_DIR = "./"

plates = pd.read_csv(os.path.join(GIT_CLONE_DIR, "metadata/plate.csv.gz"))
wells = pd.read_csv(os.path.join(GIT_CLONE_DIR, "metadata/well.csv.gz"))
compound = pd.read_csv(os.path.join(GIT_CLONE_DIR, "metadata/compound.csv.gz"))
orf = pd.read_csv(os.path.join(GIT_CLONE_DIR, "metadata/orf.csv.gz"))

# ## Sample plates
# Let's sample two plates of a certain type (encoded in `Metadata_PlateType`) from each data-generating center (`Metadata_Source`). Note that only 10 out of the 13 sources are currently available and `source_1` does not have the plate type being queried below.

sample = (
    plates.query('Metadata_PlateType=="TARGET2"')
    .groupby("Metadata_Source")
    .sample(2, random_state=42)
)
sample

# `TARGET2` plates are "sentinel" plates that are run in each batch. More on all this in future updates.

# ## Loading profiles
# Now let's load the profiles from these plates.
#
# Setting `columns = None` below will load all of the features.
#
# <div class="alert alert-warning">
# WARNING: Files are located in S3. This loop loads only two features per each sampled plate; loading many features and/or many plates can take several minutes.
# </div>

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

# Each row in `dframes` is well-level profile, containing thousands of features (n=4762) averaged over (typically) a couple of thousand cells per well.

# ## Join features with metadata
#
# The profiles are annotated with only three columns of metadata (source, plate, well).
#
# Let's add more metadata!

metadata = compound.merge(wells, on="Metadata_JCP2022")
ann_dframe = metadata.merge(
    dframes, on=["Metadata_Source", "Metadata_Plate", "Metadata_Well"]
)

# We now know a little bit more about each profile:

ann_dframe.sample(2, random_state=42)

# More metadata information will be added in the future.

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

# +
from pickle import FALSE, TRUE

px.scatter(
    ann_dframe,
    x="Cells_AreaShape_Eccentricity",
    y="Nuclei_AreaShape_Area",
    color="Metadata_Source",
    hover_name="Metadata_JCP2022",
    hover_data=["Metadata_InChIKey"],
)
# -

# So that's just a couple of (raw) measurements from the sentinel plates for 12/13 of the sources, for the principal dataset alone.

# ## Load images
#
# [LoadData](https://cellprofiler-manual.s3.amazonaws.com/CPmanual/LoadData.html) CSV files provide Metadata associated with the images to be processed.

load_data = []
for _, row in sample.iterrows():
    s3_path = loaddata_formatter.format(**row.to_dict())
    load_data.append(pd.read_parquet(s3_path, storage_options={"anon": True}))
load_data = pd.concat(load_data)

# Let's pick a row at random and inspect it

sample_loaddata = load_data.sample(1, random_state=42)
pd.melt(sample_loaddata)

# The `Metadata_` columns can be used to link the images to profiles.
# Let's pick a profile and view it's corresponding image.

sample_profile = ann_dframe.sample(1, random_state=22)
sample_profile.melt()

# First link the profile to its images.
# These are well-level profiles, and each well has typically 9 sites imaged.

sample_linked = pd.merge(
    load_data, sample_profile, on=["Metadata_Source", "Metadata_Plate", "Metadata_Well"]
)
sample_linked[["Metadata_Well", "Metadata_Site"]]

# Inspect details of a single site for this profile

sample_linked.iloc[:1].melt()

# Now load and display a single channel of this 5-channel image

# +
import os
import requests
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
# -

# There's a lot more to come! We will add more example notebooks as we go.
