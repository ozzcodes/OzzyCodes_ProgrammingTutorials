# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 21:29:16 2019

@author: ajwal
"""
#!/usr/bin/python3

import dask.dataframe as dd

indiv = dd.read_parquet("data/indiv-*.parq/")

total_by_employee = (
        indiv.groupby('employer')
        .transaction_amt.sum()
        .nlargest(10))

print(total_by_employee)
