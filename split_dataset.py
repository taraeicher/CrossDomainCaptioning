#! encoding: UTF-8

import os
import glob
import json
import subprocess

#Base paths for each data set.
mscoco_path = "/fs/project/PAS0272/Tara/nlp_project/visual_genome/mscoco"
yfcc_path = "/fs/project/PAS0272/Tara/nlp_project/visual_genome/yfcc100m"

#Training, testing, and validation JSON paths.
train_json_path = "/fs/project/PAS0272/Tara/nlp_project/im2p/data/train_split.json"
val_json_path = "/fs/project/PAS0272/Tara/nlp_project/im2p/data/val_split.json"
test_json_path = "/fs/project/PAS0272/Tara/nlp_project/im2p/data/test_split.json"

#MSCOCO training, testing, and validation paths.
train_mscoco_savepath = "/fs/project/PAS0272/Tara/nlp_project/visual_genome/mscoco_im2p_train/"
val_mscoco_savepath = "/fs/project/PAS0272/Tara/nlp_project/visual_genome/mscoco_im2p_val/"
test_mscoco_savepath = "/fs/project/PAS0272/Tara/nlp_project/visual_genome/mscoco_im2p_test/"

#YFCC100M training, testing, and validation paths.
train_yfcc_savepath = "/fs/project/PAS0272/Tara/nlp_project/visual_genome/yfcc100m_im2p_train/"
val_yfcc_savepath = "/fs/project/PAS0272/Tara/nlp_project/visual_genome/yfcc100m_im2p_val/"
test_yfcc_savepath = "/fs/project/PAS0272/Tara/nlp_project/visual_genome/yfcc100m_im2p_test/"

#Create a list of all MSCOCO and YFCC100M images.
all_images_mscoco = glob.glob(mscoco_path + "/*.jpg")
all_images_yfcc = glob.glob(yfcc_path + "/*.jpg")

#Create a list of all training images and testing images.
with open(train_json_path, "r") as fr1:
    train_names = json.load(fr1)

with open(val_json_path, "r") as fr2:
    val_names = json.load(fr2)

with open(test_json_path, "r") as fr3:
    test_names = json.load(fr3)

#Print the length of the training, testing, and validation sets.
print "train images num: {}".format(len(train_names))
print "val images num: {}".format(len(val_names))
print "test images num: {}".format(len(test_names))

#For each MSCOCO image, place it into its proper path.
for idx, img in enumerate(all_images_mscoco):
    img_name = int(os.path.basename(img).split(".")[0])
    if img_name in train_names:
        subprocess.call(["cp", img, train_mscoco_savepath])
    elif img_name in val_names:
        subprocess.call(["cp", img, val_mscoco_savepath])
    elif img_name in test_names:
        subprocess.call(["cp", img, test_mscoco_savepath])

#For each YFCC100M image, place it into its proper path.
for idx, img in enumerate(all_images_yfcc):
    img_name = int(os.path.basename(img).split(".")[0])
    if img_name in train_names:
        subprocess.call(["cp", img, train_yfcc_savepath])
    elif img_name in val_names:
        subprocess.call(["cp", img, val_yfcc_savepath])
    elif img_name in test_names:
        subprocess.call(["cp", img, test_yfcc_savepath]) 
