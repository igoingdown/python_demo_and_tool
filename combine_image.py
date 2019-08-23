import os
from PIL import Image

IMAGES_PATH = './'  # 图片集地址
IMAGES_FORMAT = ['.png', '.jpeg', '.jpg']  # 图片格式
IMAGE_BASE_WIDTH_SIZE = 800  # 每张小图片的大小
IMAGE_SAVE_PATH = '/Users/mingxing.zhao/Desktop/merged'  # 图片转换后的地址


def main():
    file_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if os.path.splitext(name)[1] == item]
    print(file_names)
    file_names.sort()
    resize_image(IMAGE_BASE_WIDTH_SIZE, file_names)


def resize_image(base_width, file_names):
    h_sum = 0
    for name in file_names:
        fname, ext = os.path.splitext(name)
        im = Image.open(name)
        w, h = im.size
        wpercent = (base_width/float(w))
        new_h = int(h * wpercent)
        h_sum += new_h

    new_im = Image.new('RGB', (base_width, h_sum))
    i = 0
    for name in file_names:
        fname, ext = os.path.splitext(name)
        print(fname)
        im = Image.open(name)
        w, h = im.size
        wpercent = (base_width/float(w))
        new_h = int(h * wpercent)
        im = im.resize((base_width, new_h), Image.ANTIALIAS)
        new_im.paste(im, (0, i))
        i += new_h
    new_im.save(IMAGE_SAVE_PATH, "JPEG")


if __name__ == '__main__':
    main()
