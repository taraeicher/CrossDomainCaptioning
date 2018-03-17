from shutil import copyfile
import json
import sys
import os

def main():

	#For each entry in the metadata, check whether it is from MSCOCO.
	#If so, copy the corresponding image to the MSCOCO folder.
	#If not, copy it to the YFCC100M folder.
	metadata = json.load(open(sys.argv[1]))
	mscoco_path = sys.argv[2]
	yfcc100m_path = sys.argv[3]
	image_source_path = sys.argv[4]
	
	for img in metadata:
	
		#The name of the image is after the last slash in the URL.
		#We include the directory name as well so we don't have collisions between the two VC folders.
		img_url = img["url"].split("/")
		img_name = img_url[len(img_url) - 1]
		img_dir = img_url[len(img_url) - 2]

		#If there is no MSCOCO ID, then move to th YFCC100M folder.
		#Otherwise, move it to the MSCOCO folder.
		if img["coco_id"] == None and os.path.exists(image_source_path + img_name):
			copyfile(image_source_path + img_name, yfcc100m_path + img_dir + "_" + img_name)
		elif os.path.exists(image_source_path + img_name):
			copyfile(image_source_path + img_name, mscoco_path + img_dir + "_" + img_name)


if __name__ == "__main__":
	main()