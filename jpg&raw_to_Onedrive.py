# 2021-01-07
from PIL import Image
import PIL
import os
import glob
import math
def compress_images(directory=False, quality=30):
    # 1. If there is a directory then change into it, else perform the next operations inside of the
    # current working directory:
    if directory:
        os.chdir(directory)

    # 2. Extract all of files
    files = os.listdir()

    # 3. Extract all of the images:
    images = [file for file in files if file.endswith(('jpg', 'png', 'JPG', 'PNG'))]

    # 4. Loop over every image:
    for image in images:
        print(image)

        # 5. Open every image:
        img = Image.open(image)

        # 5. Compress every image and save it with a new name:
        img.save("Kopia_"+image, optimize=True, quality=quality)


def compress_one_image(directory=False, quality=10):
    if directory:
        os.chdir(os.path.dirname(os.path.abspath(directory)))
    img = Image.open(directory)
    img.save('_' + os.path.basename(directory) , optimize=True, quality=quality)


def images_change_resolution(directory=False, quality=50, resize=0.8, png_jpg_conv=False, file=None):
    if directory:
        os.chdir(directory)

    # 2. Extract all of files
    files = os.listdir()

    # 3. Extract all of the images:
    images = [file for file in files if file.endswith(('jpg', 'png', 'JPG', 'PNG'))]

    # 4. Loop over every image:
    for image in images:
        print(image)

        # 5. Open every image:
        img = Image.open(image)

        # 5. Compress every image and save it with a new name:
        width, height = img.size
        old_width, old_height = img.size
        width = math.floor(width * resize)
        height = math.floor(height * resize)
        img = img.resize((width, height))
        extension = os.path.splitext(file)[1]
        filename = os.path.basename(file)
        if (extension == '.png' and png_jpg_conv == True):
            img = img.convert('RGB')
            quality = 80
            filename = filename.replace('.png', '_zmn' + '.jpg')
        else:
            filename = filename.replace(extension, '_zmn' + extension)
        img.save(filename, optimize=True, quality=quality)




def image_change_resolution(file=False, quality=50, resize=0.5, png_jpg_conv=False):
    if file:
        os.chdir(os.path.dirname(os.path.abspath(file)))
    img = Image.open(file)
    width, height = img.size
    old_width, old_height = img.size
    width= math.floor(width*resize)
    height = math.floor(height * resize)
    img = img.resize((width , height))
    extension = os.path.splitext(file)[1]
    filename = os.path.basename(file)
    if (extension =='.png' and png_jpg_conv == True):
        img = img.convert('RGB')
        quality=80
        filename = filename.replace('.png','_zmn' + '.jpg')
    #else:
    #    filename = filename.replace(extension, '_zmn' + extension) # bez "zmn"
    img.save(filename, optimize=True, quality=quality)

    print('Resize img completed: [ratio = ' + str(resize) + ']')
    print('Width: ',old_width, ' -->', width)
    print('Height: ', old_height, '-->', height)


def image_info(directory=False):
    if directory:
        os.chdir(os.path.dirname(os.path.abspath(directory)))
    img = Image.open(directory)
    width, height = img.size
    print('width: ',width, 'height: ', height)
subdirectory_path = r'G:\głoszenia'
dir_path_one_image = r'G:\Dom_P1090417.JPG'
# compress_one_image(dir_path_one_image, 30)
# image_change_resolution(dir_path_one_image, 30, 0.6, True)
# image_info(dir_path_one_image)
# images_change_resolution(subdirectory_path, resize=0.5)
compress_images(directory=subdirectory_path)

for filename in os.listdir(subdirectory_path):
     sciezka= os.path.join(subdirectory_path, filename)
     img = Image.open(sciezka)
     width, height = img.size
     if width>2000 or height>2000:
        print(filename, width, height)
        image_change_resolution(sciezka,quality= 50, resize=0.5,png_jpg_conv= True)