#!/usr/bin/env jupyter
# ---
# title: Available genes
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
# Is my Gene in JUMP or other associated tables?


# %%
# | code-fold: true
import polars as pl
import pooch
from itables import show

# %%
# | code-fold: true
logger = pooch.get_logger()
logger.setLevel("WARNING")
df = pl.read_csv(
    pooch.retrieve(
        "https://zenodo.org/api/records/15059555/files/table.csv/content",
        known_hash="a082225c08a09f95fd6578dc7d2114aea772ff728f75314fc1350647e0ac949f",
    )
)
show(df, maxBytes=0)
df = pl.read_csv(pooch.retrieve("https://zenodo.org/api/records/15059555/files/table.csv/content", known_hash  = "a082225c08a09f95fd6578dc7d2114aea772ff728f75314fc1350647e0ac949f"))
show(df, maxBytes=0)
