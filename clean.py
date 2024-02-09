def clean(input1, input2):
    import pandas as pd

    df1 = pd.read_csv(input1)          # respondent_contact.csv file
    df2 = pd.read_csv(input2)          # respondent_other.csv file

    combined_df = df1.merge(df2, how = 'outer', left_on= 'respondent_id', right_on='id')                  # merge the two input data files (i.e., respondent_contact.csv, respondent_other.csv)
    combined_df.dropna(axis = 0, how = 'any', inplace=True)                                               # drop any rows with missing values
    combined_df.drop('id', axis = 1, inplace=True)                                                  # you may remove one column to avoid redundancy after merging
    combined_df = combined_df.loc[~combined_df['job'].str.contains('insurance|Insurance', regex=True)]    # drop any rows if their job value contains ‘insurance’ or ‘Insurance’

    return combined_df

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('input1', help='respondent_contact.csv)')
    parser.add_argument('input2', help='respondent_other.csv')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2)
    cleaned.to_csv(args.output, index=False)
