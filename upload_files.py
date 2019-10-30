from googleapiclient.discovery import build
import os, pickle
from googleapiclient.http import MediaFileUpload
import click
from tqdm import tqdm

if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

insta_content_id = '1Nb2vX3QZHA0v1iBLYo0_16kwFFlb5pbW'
drive_service = build('drive', 'v3', credentials=creds)

@click.command()
@click.option('--curr_dir', help='select directory with files to upload')
def upload_file(curr_dir):
    for file_name in tqdm(os.listdir(curr_dir)):
        file_metadata = {'name': file_name, 'parents': [insta_content_id]}
        media = MediaFileUpload(f'{curr_dir}/{file_name}', mimetype='*/*')

        drive_service.files().create(body=file_metadata,
                                     media_body=media,
                                     fields='id').execute()


if __name__ == '__main__':
    upload_file()
