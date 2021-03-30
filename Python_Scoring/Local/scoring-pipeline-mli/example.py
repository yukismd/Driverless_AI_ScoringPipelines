# Copyright 2020 H2O.ai; Proprietary License;  -*- encoding: utf-8 -*-

import pandas as pd
import numpy as np
from numpy import nan
from scipy.special._ufuncs import expit
from scoring_mli_experiment_eb096b2c_4fcd_11eb_9924_0242ac110002 import KLimeScorer

#
# The format of input record to the KLimeScorer.score() method is as follows:
#

# -----------------------
# Name   Type      Range 
# -----------------------
# x3     float64   [0, 0]
# x1     float64   [0, 0]
# x4     float64   [0, 0]
# -----------------------


#
# Create a singleton KLimeScorer instance.
# For optimal performance, create a KLimeScorer instance once, and call score_reason_codes() or score_reason_codes_batch() multiple times.
#
mli_scorer = KLimeScorer()


#
# To get reason codes one row at a time, use the KLimeScorer.score_reason_codes() method:
#

print('---------- Get Reason Codes for One Row ----------')
print(mli_scorer.score_reason_codes([
    '-2.7997',  # x3
    '-2.4307',  # x1
    '-2.3697',  # x4
]))
print(mli_scorer.score_reason_codes([
    '-2.5746',  # x3
    '-2.9838',  # x1
    '-3.4233',  # x4
]))
print(mli_scorer.score_reason_codes([
    '-2.6275',  # x3
    '-2.4492',  # x1
    '-2.4827',  # x4
]))
print(mli_scorer.score_reason_codes([
    '-2.7208',  # x3
    '-2.4307',  # x1
    '-3.4233',  # x4
]))
print(mli_scorer.score_reason_codes([
    '-2.4735',  # x3
    '-2.4871',  # x1
    '-2.3194',  # x4
]))

#
# To score a batch of rows, use the KLimeScorer.score_reason_codes_batch() method (much faster than repeated one-row scoring):
#
print('---------- Get Reason Codes for a Frame ----------')
columns = [
    pd.Series(['-2.7997', '-2.5746', '-2.6275', '-2.7208', '-2.4735'], name='x3', dtype='float64'),
    pd.Series(['-2.4307', '-2.9838', '-2.4492', '-2.4307', '-2.4871'], name='x1', dtype='float64'),
    pd.Series(['-2.3697', '-3.4233', '-2.4827', '-3.4233', '-2.3194'], name='x4', dtype='float64'),
]
df = pd.concat(columns, axis=1)
print(mli_scorer.score_reason_codes_batch(df))

##  Recommended workflow with datatable (fast and consistent with training):
import datatable as dt
dt.Frame(df).to_csv("test.csv")          # turn above dummy frame into a CSV (for convenience)
test_dt = dt.fread("test.csv", na_strings=['', '?', 'None', 'nan', 'NA', 'N/A', 'unknown', 'inf', '-inf', '1.7976931348623157e+308', '-1.7976931348623157e+308'])           # parse test set CSV file into datatable (with consistent NA handling)
preds_df = mli_scorer.score_reason_codes_batch(test_dt)   # make predictions (pandas frame)
dt.Frame(preds_df).to_csv("preds.csv")   # save pandas frame to CSV using datatable


print('---------- Get Quantile Bin Transformation ----------')
print('---------- Automatically done in score* methods -----')
print(mli_scorer.quantile_bin_row([
    '-2.7997',  # x3
    '-2.4307',  # x1
    '-2.3697',  # x4
]))
print(mli_scorer.quantile_bin_row([
    '-2.5746',  # x3
    '-2.9838',  # x1
    '-3.4233',  # x4
]))

#
# To retrieve the original feature column names, use the KLimeScorer.get_column_names() method:
# This method retrieves the input column names
#

print('---------- Retrieve column names ----------')
print(mli_scorer.get_column_names())

#
# To retrieve the reason code column names, use the KLimeScorer.get_reason_code_column_names() method:
# This method retrieves the reason code column names
#
print('---------- Retrieve Reason Code column names ----------')
print(mli_scorer.get_reason_code_column_names())