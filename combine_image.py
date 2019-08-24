import os
from PIL import Image

HOME = os.environ['HOME']
IMAGES_PATH = HOME + '/Desktop/images'  # 图片集地址
IMAGES_FORMAT = ['.png', '.jpeg', '.jpg']  # 图片格式
IMAGE_BASE_WIDTH_SIZE = 800  # 每张图片的宽度
IMAGE_SAVE_PATH = HOME + '/Desktop/merged'  # 图片转换后的地址


def main():
    file_names = image_file_names_in_dir(IMAGES_PATH)
    file_names.sort()
    new_sizes, total_hight = unify_image_width(IMAGE_BASE_WIDTH_SIZE, file_names)
    resize_and_combine(file_names, new_sizes, total_hight, IMAGE_BASE_WIDTH_SIZE)


def image_file_names_in_dir(dir):
    return [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if os.path.splitext(name)[1] == item]


def unify_image_width(base_width, file_names):
    new_sizes = []
    h_sum = 0
    for name in file_names:
        im = Image.open(os.path.join(IMAGES_PATH, name))
        w, h = im.size
        wpercent = (base_width/float(w))
        new_h = int(h * wpercent)
        h_sum += new_h
        new_sizes.append((base_width, new_h))
    return new_sizes, h_sum


def resize_and_combine(file_names, new_sizes, total_hight, base_width):
    new_im = Image.new('RGB', (base_width, total_hight))
    copy_pos_down = 0
    assert len(file_names) == len(new_sizes)
    for i in range(len(file_names)):
        im = Image.open(os.path.join(IMAGES_PATH, file_names[i])).resize((new_sizes[i][0], new_sizes[i][1]), Image.ANTIALIAS)
        new_im.paste(im, (0, copy_pos_down))
        copy_pos_down += new_sizes[i][1]
    new_im.save(IMAGE_SAVE_PATH, "JPEG")


if __name__ == '__main__':
    main()
