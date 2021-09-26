from PIL import Image
import os
import imghdr


def convert_image_to_pdf(filepath: str):
    image1 = Image.open(filepath)
    im1 = image1.convert('RGB')
    im1.save(filepath.rsplit('.', 1)[0] + '.pdf')


def convert_images_from_dir_to_pdf(dirpath: str):
    assert os.path.exists(dirpath)
    assert os.path.isdir(dirpath)

    filepaths = [dirpath+os.sep+filename for filename in os.listdir(dirpath)]

    for filepath in filepaths:
        if imghdr.what(filepath):
            convert_image_to_pdf(filepath)
            os.remove(filepath)
