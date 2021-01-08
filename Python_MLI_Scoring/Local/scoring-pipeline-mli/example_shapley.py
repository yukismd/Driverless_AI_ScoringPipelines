import pandas
THRESHOLD = 0.2  # the max absolute difference between KLime model score and DAI score where DAI reason codes should be reported
exec(open("../scoring-pipeline/example.py").read())
exec(open("example.py").read())

#Example DataFrame
mli_df = pandas.DataFrame(pandas.np.array([[
    '-2.7997',
    '-2.4307',
    '-2.3697',
]]), columns=mli_scorer.get_column_names())

# Make the row compatible with DAI model input
dai_df = mli_df.reindex(scorer.get_column_names(), axis=1)
# Get the DAI model score
dai_score = scorer.score_batch(dai_df)
# Get the prediction contributions (Shapley reason codes) from DAI model
dai_reason_codes = scorer.score_batch(dai_df, pred_contribs=True)
# Get KLime reason codes
klime_reason_codes = mli_scorer.score_reason_codes_batch(mli_df)
# KLime model score is the sum of all the reason codes+intercept (included in the output of score_reason_codes* methods)
klime_score = mli_scorer.score_reason_codes_batch(mli_df).sum(axis=1)
# If the difference between KLime and the DAI model is greater than a threshold
# then use the reason codes from the actual DAI (in transformed feature space)
if abs(dai_score.values[0][0] - klime_score.values[0]) > THRESHOLD:
    print(" KLIME score vs DAI score difference is higher than threshold. Reporting Reason codes from DAI model:")
    print(str(dai_reason_codes))
else:
    print(" KLIME score within threshold difference of DAI model. Reporting Reason codes from KLIME:")
    print(str(klime_reason_codes))
