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
df = pl.read_csv(
    pooch.retrieve(
        f"https://zenodo.org/api/records/15065576/files/table.csv/content",
        known_hash="db79d8316dec141802ffad6378ae7ff05921c22551feda6feed117c236315ebd",
    )
)
show(df, maxBytes=0)
