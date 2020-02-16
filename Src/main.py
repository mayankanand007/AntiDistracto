from VideoDetection import *
import json
import os
from predict import *
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/umanggupta/Downloads/skilled-drake-268307-9d4ac42fef3e.json"
from google.cloud import automl

project_id = "skilled-drake-268307"
model_id = "ICN8476667302153027584"
file_path = "/Users/umanggupta/Downloads/sleep.png"

def func():

    prediction_client = automl.PredictionServiceClient()

    # Get the full path of the model.
    model_full_id = prediction_client.model_path(
        project_id, "us-central1", model_id
    )

    # Read the file.
    with open(file_path, "rb") as content_file:
        content = content_file.read()

    image = automl.types.Image(image_bytes=content)
    payload = automl.types.ExamplePayload(image=image)

    return get_prediction(content, project_id, model_id)
