import argparse
import os
import shutil
from random import seed
from random import sample

# Add Parser
parser = argparse.ArgumentParser()
   
parser.add_argument("--folder", type=str, default="img", help="Folder that contain image")
parser.add_argument("--dest", type=str, default="img-dest", help="Destination")


args = parser.parse_args()

def get_difference_from_2_list(list1, list2):
	set_list1 = set(list1)
	set_list2 = set(list2)

	diff = list(set_list1.difference(set_list2))

	return diff

def make_folder():
    folders = ["images", "labels"]
    inner_folders = ["train", "val", "test"]

    if(not os.path.isdir(args.dest)):
        os.mkdir(args.dest)

    for folder in folders:
        path = os.path.join(args.dest, folder)
        # Check existing folder
        if(not os.path.isdir(path)):
            os.mkdir(path)
        
        for in_folder in inner_folders:
            inner_path = os.path.join(path, in_folder)
            # Check existing inner folder
            if(not os.path.isdir(inner_path)):
                os.mkdir(inner_path)     

def copy_image(file, id_folder):
    inner_folders = ["train", "val", "test"]

    # Image
    source = os.path.join(args.folder, file)
    out_dest = os.path.join(args.dest, 'images')
    destination = os.path.join(out_dest, inner_folders[id_folder])    

    try:
        shutil.copy(source, destination)
        # print("File copied successfully.")

    # If source and destination are same
    except shutil.SameFileError:
        print("Source and destination represents the same file.")

    # labels   
    separator = file.find(".")
    filename = file[0:separator]+".txt" 

    source = os.path.join(args.folder, filename)
    out_dest = os.path.join(args.dest, 'labels')
    destination = os.path.join(out_dest, inner_folders[id_folder])

    try:
        shutil.copy(source, destination)
        # print("File copied successfully.")

    # If source and destination are same
    except shutil.SameFileError:
        print("Source and destination represents the same file.") 

make_folder()

with open("autosplit_train.txt", "r") as file:
    filenames_train = [line.strip().split("/")[-1] for line in file]
    #filenames_train = [line.strip('/')[-1] for line in filenames]
count = 0
for file in filenames_train:
	if ((file.endswith(".jpg")) or (file.endswith(".png"))):
		copy_image(file, 0)
		count+=1
print(f"Train size: {count}")

with open("autosplit_val.txt", "r") as file:
    filenames_val = [line.strip().split("/")[-1] for line in file]
count = 0
for file in filenames_val:
	if ((file.endswith(".jpg")) or (file.endswith(".png"))):
		copy_image(file, 1)
		count+=1
print(f"Valid size: {count}")

with open("autosplit_test.txt", "r") as file:
    filenames_test = [line.strip().split("/")[-1] for line in file]
count = 0
for file in filenames_test:
	if ((file.endswith(".jpg")) or (file.endswith(".png"))):
		copy_image(file, 2)
		count+=1
print(f"Test size: {count}")
