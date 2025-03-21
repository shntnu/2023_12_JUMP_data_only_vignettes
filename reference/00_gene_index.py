#!/usr/bin/env jupyter
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Available genes
# Is my gene of interest in JUMP or other associated tables?

# %%
# | code-fold: true
import requests

import polars as pl
import pooch
from itables import show

logger = pooch.get_logger()
logger.setLevel("WARNING")
latest_id = requests.get(
    "https://zenodo.org/api/records/15059555/versions/latest"
).json()["id"]
df = pl.read_csv(
    pooch.retrieve(
        f"https://zenodo.org/api/records/{latest_id}/files/table.csv/content",
        known_hash="a082225c08a09f95fd6578dc7d2114aea772ff728f75314fc1350647e0ac949f",
    )
)
show(df, maxBytes=0)
