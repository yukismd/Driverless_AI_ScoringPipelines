# Copyright 2020 H2O.ai; Proprietary License;  -*- encoding: utf-8 -*-

import pandas as pd
import numpy as np
from numpy import nan
from scipy.special._ufuncs import expit
from scoring_h2oai_experiment_0bdb6222_458f_11eb_91c1_0242ac110002 import Scorer

#
# The format of input record to the Scorer.score() method is as follows:
#

# ----------------------------------------------------------
# Name   Type      Range                                    
# ----------------------------------------------------------
# x1     float32   [-3.0065999031066895, 2.7874999046325684]
# x2     float32   [-4.136000156402588, 3.256700038909912]  
# x3     float32   [-3.0952999591827393, 3.3822999000549316]
# x4     float32   [-3.42330002784729, 3.0445001125335693]  
# ----------------------------------------------------------


#
# Create a singleton Scorer instance.
# For optimal performance, create a Scorer instance once, and call score() or score_batch() multiple times.
#
scorer = Scorer()


#
# To score one row at a time, use the Scorer.score() method (this can seem slow due to one-time overhead):
#

print('---------- Score Row ----------')
print(scorer.score([
    '-2.631500005722046',  # x1
    '-2.277899980545044',  # x2
    '-2.7997000217437744',  # x3
    '-2.3194000720977783',  # x4
]))
print(scorer.score([
    '-2.4870998859405518',  # x1
    '-2.550600051879883',  # x2
    '-2.9811999797821045',  # x3
    '-2.3696999549865723',  # x4
]))
print(scorer.score([
    '-2.5062999725341797',  # x1
    '-4.136000156402588',  # x2
    '-2.7997000217437744',  # x3
    '-2.3696999549865723',  # x4
]))
print(scorer.score([
    '-2.6043999195098877',  # x1
    '-2.3060998916625977',  # x2
    '-2.5227999687194824',  # x3
    '-2.4237000942230225',  # x4
]))
print(scorer.score([
    '-2.4442999362945557',  # x1
    '-2.550600051879883',  # x2
    '-2.9811999797821045',  # x3
    '-2.3696999549865723',  # x4
]))


#
# To score a batch of rows, use the Scorer.score_batch() method (much faster than repeated one-row scoring):
#
print('---------- Score Frame ----------')
columns = [
    pd.Series(['-2.631500005722046', '-2.4870998859405518', '-2.5062999725341797', '-2.6043999195098877', '-2.4442999362945557', '-2.4307000637054443', '-2.983799934387207', '-2.449199914932251', '-2.4307000637054443', '-2.4870998859405518', '-2.4442999362945557', '-3.0065999031066895', '-2.5062999725341797', '-3.0065999031066895', '-2.4307000637054443'], name='x1', dtype='float32'),
    pd.Series(['-2.277899980545044', '-2.550600051879883', '-4.136000156402588', '-2.3060998916625977', '-2.550600051879883', '-2.277899980545044', '-2.501499891281128', '-2.2207999229431152', '-4.136000156402588', '-2.2112998962402344', '-4.136000156402588', '-2.501499891281128', '-2.550600051879883', '-2.501499891281128', '-2.7822000980377197'], name='x2', dtype='float32'),
    pd.Series(['-2.7997000217437744', '-2.9811999797821045', '-2.7997000217437744', '-2.5227999687194824', '-2.9811999797821045', '-2.5227999687194824', '-2.7207999229431152', '-3.0952999591827393', '-2.627500057220459', '-2.9811999797821045', '-2.627500057220459', '-2.4607999324798584', '-2.4607999324798584', '-2.7207999229431152', '-3.0952999591827393'], name='x3', dtype='float32'),
    pd.Series(['-2.3194000720977783', '-2.3696999549865723', '-2.3696999549865723', '-2.4237000942230225', '-2.3696999549865723', '-2.4237000942230225', '-2.7878000736236572', '-3.3620998859405518', '-2.847599983215332', '-2.4827001094818115', '-2.847599983215332', '-2.4827001094818115', '-2.4237000942230225', '-2.3901000022888184', '-2.781599998474121'], name='x4', dtype='float32'),
]
df = pd.concat(columns, axis=1)
print(scorer.score_batch(df))

##  Recommended workflow with datatable (fast and consistent with training):
import datatable as dt
dt.Frame(df).to_csv("test.csv")          # turn above dummy frame into a CSV (for convenience)
test_dt = dt.fread("test.csv", na_strings=['', '?', 'None', 'nan', 'NA', 'N/A', 'unknown', 'inf', '-inf', '1.7976931348623157e+308', '-1.7976931348623157e+308'])           # parse test set CSV file into datatable (with consistent NA handling)
preds_df = scorer.score_batch(test_dt)   # make predictions (pandas frame)
dt.Frame(preds_df).to_csv("preds.csv")   # save pandas frame to CSV using datatable


#
# The following lines demonstrate how to obtain per-feature prediction contributions per row. These can be
# very helpful in interpreting the model's predictions for individual observations (rows).
# Note that the contributions are in margin space (link space), so for binomial models the application of the
# final logistic function is omitted, while for multinomial models, the application of the final softmax function is
# omitted and for regression models the inverse link function is omitted (such as exp/square/re-normalization/etc.).
# This ensures that we can provide per-feature contributions that add up to the model's prediction.
# To simulate the omission of the transformation from margin/link space back to the probability or target space,
# and to get the predictions in the margin/link space, enable the output_margin flag. To get the prediction
# contributions, set pred_contribs=True. Note that you cannot provide both flags at the same time.
#

print('---------- Get Per-Feature Prediction Contributions for Row ----------')
print(scorer.score([
    '-2.631500005722046',  # x1
    '-2.277899980545044',  # x2
    '-2.7997000217437744',  # x3
    '-2.3194000720977783',  # x4
], pred_contribs=True))


print('---------- Get Per-Feature Prediction Contributions for Frame ----------')
pred_contribs = scorer.score_batch(df, pred_contribs=True, fast_approx=True)  # per-feature prediction contributions
print(pred_contribs)


#
# The following lines demonstrate how to perform feature transformations without scoring.
# You can use this capability to transform input rows and fit models on the transformed frame
#   using an external ML tool of your choice, e.g. Sparkling Water or H2O.
#

#
# To transform a batch of rows (without scoring), use the Scorer.fit_transform_batch() method:
# This method fits the feature engineering pipeline on the given training frame, and applies it on the validation set,
# and optionally also on a test set.
#

# Transforms given datasets into enriched datasets with Driverless AI features')
#    train - for model fitting (do not use parts of this frame for parameter tuning)')
#    valid - for model parameter tuning')
#    test  - for final model testing (optional)')

print('---------- Transform Frames ----------')

# The target column 'y' has to be present in all provided frames.
df['y'] = pd.Series(['-3.9127', '-3.4779', '-3.0888', '-3.7408', '-3.0888', '-4.1274', '-3.7408', '-4.1274', '-2.7917', '-2.4938', '-2.7917', '-2.7917', '-4.1274', '-2.4938', '-2.7917'], dtype='float64')

#  For demonstration only, do not use the same frame for train, valid and test!
train_munged, valid_munged, test_munged = \
  scorer.fit_transform_batch(train_frame=df, valid_frame=df, test_frame=df)
print(train_munged)  # for model fitting (use entire frame, no cross-validation)
print(valid_munged)  # for model validation (parameter tuning)
print(test_munged)   # for final pipeline testing (one time)

#
# To retrieve the original feature column names, use the Scorer.get_column_names() method:
# This method retrieves the input column names 
#

print('---------- Retrieve column names ----------')
print(scorer.get_column_names())

#
# To retrieve the transformed column names, use the Scorer.get_transformed_column_names() method:
# This method retrieves the transformed column names
#

print('---------- Retrieve transformed column names ----------')
print(scorer.get_transformed_column_names())

