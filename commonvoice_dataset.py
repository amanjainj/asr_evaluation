import pandas
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--data_root_dir",
    required=True,
    help="Absolute path to the root directory of the commonvoice dataset")

parser.add_argument("--output_path",
                    required=True,
                    help="Path to the output file to save the dataset")
args = parser.parse_args()

audio_clips_dir = os.path.join(args.data_root_dir,
                               "cv-corpus-10.0-2022-07-04/ja/clips")
test_data_path = os.path.join(args.data_root_dir,
                              "cv-corpus-10.0-2022-07-04/ja/test.tsv")

# Attributes to use for filtering
ages_filter = ["teens", "fifties"]
genders_filter = ["male", "female"]

test_data_df = pandas.read_csv(test_data_path, sep='\t').astype(str)

# Filter data according to age and gender
test_data_df.loc[test_data_df["age"].isin(ages_filter)
                 & test_data_df["gender"].isin(genders_filter)]

# Replace the path with full path
test_data_df["path"] = test_data_df["path"].map(
    lambda p: os.path.join(audio_clips_dir, p))

test_data_df.rename(columns={
    "path": "audio_path",
    "sentence": "utterance"
},
                    inplace=True)

test_data_df.to_csv(args.output_path, columns=["audio_path", "utterance"])
