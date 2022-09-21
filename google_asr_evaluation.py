import json
from google.cloud import speech
import os
import io
import pandas
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--dataset_path",
                    required=True,
                    help="Path to the csv file containing dataset")

parser.add_argument("--output_path",
                    required=True,
                    help="Path to the output file to save the results")
args = parser.parse_args()

# setting Google credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_secret_key.json'
# create client instance
client = speech.SpeechClient()

config = speech.RecognitionConfig(
    # encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    enable_automatic_punctuation=True,
    # audio_channel_count=2,
    language_code="ja-JP",
    model="latest_short",
)

data_df = pandas.read_csv(args.dataset_path)
results = {}

# Iterate over the dataset and pass each audio file to the API
# for trancription one-by-one.
# TODO : Find API call for batch transcription for faster processing
for row in data_df.iterrows():
    audio_filepath = row["audio_path"]

    with io.open(audio_filepath, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    # Sends the request to google to transcribe the audio
    response = client.recognize(request={"config": config, "audio": audio})

    # Reads the response
    transcripts = [res.alternatives[0].transcript for res in response.results]
    confidences = [res.alternatives[0].confidence for res in response.results]

    results[audio_filepath] = {
        "transcripts": transcripts,
        "confidences": confidences,
        "gt_utterance": row["utterance"]
    }

with open(args.output_path, 'w') as out_file:
    json.dump(results, out_file)
