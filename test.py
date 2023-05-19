import pandas as pd
import boto3

credential = pd.read_csv("rootkey.csv")
access_key_id = credential['Access key ID'][0]
secret_access_key = credential['Secret access key'][0]
REGION = credential['Region'][0]

client = boto3.client('rekognition', aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key, region_name=REGION)


def get_text(img):
    try:
        img = './images/' + img

        with open(img, 'rb') as source_image:
            source_bytes = source_image.read()

        response = client.detect_text(Image={'Bytes': source_bytes})

        ocr = []

        for i in range(len(response['TextDetections'])):
            if 'ParentId' not in response['TextDetections'][i].keys():
                ocr.append(response['TextDetections'][i]['DetectedText'])

        return ocr
    except:
        statement = "Something went wrong"
        return statement

img = "imgs.jpg"
ocr = get_text(img)
print(ocr)
