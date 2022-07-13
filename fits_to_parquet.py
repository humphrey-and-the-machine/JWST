# Python script to read a .fits data table and save it as a parquet .pq file

import os, sys
import pandas as pd, numpy as np
from astropy.io import fits
from astropy.table import Table

infile = 'data.fits'

path = './'
os.chdir(path)

# read the fits table into pandas dataframe
with fits.open(infile) as data:
    table = Table.read(data,format='fits')
    df = table.to_pandas()

del table

outname = infile.replace('.fits','.pq')
df.to_parquet(outname)
