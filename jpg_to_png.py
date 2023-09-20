import os
import sys
from PIL import Image

# this algorythm is for: python file_path_of_jpegs desired_only_folder_name_to_save_into_path_of_jpegs
result_path_existance = os.path.exists(sys.argv[2])
new_folder = sys.argv[2]
existing_folder = sys.argv[1]

if not result_path_existance:
    try:
        path = os.path.join(sys.argv[1], new_folder)
        os.mkdir(path)
        print("Directory '% s' created" % new_folder)
    except:
        if FileExistsError:
            print(f'{new_folder} folder already exists')

pics = os.listdir(existing_folder)
for pic in pics:
    if pic.endswith(".jpg"):
        f, e = os.path.splitext(pic)
        outfile = f + ".png"
        if pic != outfile:
            try:
                with Image.open(os.path.join(existing_folder, pic)) as im:
                    im.save(os.path.join(path, outfile))
            except OSError:
                print("cannot convert", pic)
