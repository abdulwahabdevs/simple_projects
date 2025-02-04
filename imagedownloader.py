import os
import requests

def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg']
    for ext in extensions:
        if ext in image_url:
            return ext


def download_image(image_url: str, name: str, folder: str | None):
    if ext:= get_extension(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name: str = f'{name}{ext}'

    else:
        raise Exception(f'Invalid image url: {image_url}')

    # checking if file name we want to create already exists
    if os.path.isfile(image_name):
        raise Exception('File name already exists')


    # download image process
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as file:
            file.write(image_content)
            print(f"Downloaded {image_name} successfully")
    except Exception as e:
        print(f"{e} downloading image")


if __name__ == '__main__':
    input_url: str = input('Enter image url: ')
    input_name: str = input('Please name it: ')

    print('Downloading...')
    download_image(input_url, name=input_name, folder='images')





