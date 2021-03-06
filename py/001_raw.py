#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 23:43:03 2019

@author: Kazuki
"""

import numpy as np
import pandas as pd
from tqdm import tqdm
import os
import utils

PREF = 'f001'

dirs  = [f'../data/var_{i:03}' for i in range(200)]
var_names = [f'var_{i:03}' for i in range(200)]

d_v = list(zip(dirs, var_names))

def output(df, name):
    """
    name: 'train' or 'test'
    """
    
    for d,v in tqdm(d_v):
        df.filter(regex=f'^(?=.*{v}).*$').to_pickle(f'{d}/{name}_{PREF}.pkl')
    
    return

# =============================================================================
# main
# =============================================================================
if __name__ == "__main__":
    utils.start(__file__)
    
    tr = utils.load_train().drop(['ID_code', 'target'], axis=1)
    tr = tr.add_prefix(PREF+'_')
    output(tr, 'train')
    
    te = utils.load_test().drop(['ID_code'], axis=1)
    fake_index = np.load('../data/fake_index.npy')
    te = te.drop(fake_index).add_prefix(PREF+'_').reset_index(drop=True)
    output(te, 'test')
    
    
    utils.end(__file__)

