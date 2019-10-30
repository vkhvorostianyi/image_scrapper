from upload_files import drive_service
import click
@click.command()
@click.option('--dir_name', help='enter a folder name')
def main(dir_name):
    file_metadata = {
                     'name': dir_name,
                     'mimeType': 'application/vnd.google-apps.folder'
                    }
    file = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()
    print(f'folder_name: {dir_name} folder_id {file["id"]}')


if __name__ == '__main__':
    main()