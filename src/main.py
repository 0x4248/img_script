# img_script
# Use a script to manipulate images.
# Github: https://www.github.com/awesomelewis2007/img_script
# Licence: GNU General Public License v3.0
# By: Lewis Evans

import os
import sys
import cv2
import argparse

SUPPORTED_IMAGES = [".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Use a script to manipulate images.")
    parser.add_argument("script", help="The script to use to edit the images.")
    parser.add_argument("image", help="The image to use the script on. Use * to use the script on all images in the current directory.")
    args = parser.parse_args()

    if not os.path.exists(args.script):
        print("Script does not exist.")
        sys.exit(1)
    
    if args.image != "*" and not os.path.exists(args.image):
        print("Image does not exist.")
        sys.exit(1)

    if args.image == "*":
        for file in os.listdir("."):
            if os.path.splitext(file)[1].lower() in SUPPORTED_IMAGES:
                image = cv2.imread(file)
                with open(args.script, "r") as f:
                    for line in f.readlines():
                        if line.startswith("#"):
                            continue
                        line = line.strip()
                        if line.startswith("SATURATION"):
                            image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                            image[:, :, 1] = image[:, :, 1] * float(line.split(" ")[1])
                            image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
                        elif line.startswith("BRIGHTNESS"):
                            image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                            image[:, :, 2] = image[:, :, 2] * float(line.split(" ")[1])
                            image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
                        elif line.startswith("CONTRAST"):
                            image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                            image[:, :, 2] = image[:, :, 2] * float(line.split(" ")[1])
                            image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
                        elif line.startswith("SHARPNESS"):
                            image = cv2.GaussianBlur(image, (9, 9), float(line.split(" ")[1]))
                        elif line.startswith("BLUR"):
                            image = cv2.GaussianBlur(image, (9, 9), float(line.split(" ")[1]))
                        elif line.startswith("ROTATE"):
                            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
                        elif line.startswith("RESIZE"):
                            image = cv2.resize(image, (int(line.split(" ")[1].split("x")[0]), int(line.split(" ")[1].split("x")[1])))
                        elif line.startswith("CROP"):
                            image = image[int(line.split(" ")[1].split("x")[0]):int(line.split(" ")[1].split("x")[1]), int(line.split(" ")[2].split("x")[0]):int(line.split(" ")[2].split("x")[1])]
                        elif line.startswith("FLIP HORIZONTAL"):
                            image = cv2.flip(image, 1)
                        elif line.startswith("FLIP VERTICAL"):
                            image = cv2.flip(image, 0)
                        elif line.startswith("ADD_TEXT"):
                            cv2.putText(image, line.split(" ")[1], (int(line.split(" ")[2]), int(line.split(" ")[3])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                cv2.imwrite(file, image)
    else:
        image = cv2.imread(args.image)
        with open(args.script, "r") as f:
            for line in f.readlines():
                if line.startswith("#"):
                    continue
                line = line.strip()
                if line.startswith("SATURATION"):
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                    image[:, :, 1] = image[:, :, 1] * float(line.split(" ")[1])
                    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
                elif line.startswith("BRIGHTNESS"):
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                    image[:, :, 2] = image[:, :, 2] * float(line.split(" ")[1])
                    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
                elif line.startswith("CONTRAST"):
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                    image[:, :, 2] = image[:, :, 2] * float(line.split(" ")[1])
                    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
                elif line.startswith("SHARPNESS"):
                    image = cv2.GaussianBlur(image, (9, 9), float(line.split(" ")[1]))
                elif line.startswith("BLUR"):
                    image = cv2.GaussianBlur(image, (9, 9), float(line.split(" ")[1]))
                elif line.startswith("ROTATE"):
                    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
                elif line.startswith("RESIZE"):
                    image = cv2.resize(image, (int(line.split(" ")[1].split("x")[0]), int(line.split(" ")[1].split("x")[1])))
                elif line.startswith("CROP"):
                    image = image[int(line.split(" ")[1].split("x")[0]):int(line.split(" ")[1].split("x")[1]), int(line.split(" ")[2].split("x")[0]):int(line.split(" ")[2].split("x")[1])]
                elif line.startswith("FLIP HORIZONTAL"):
                    image = cv2.flip(image, 1)
                elif line.startswith("FLIP VERTICAL"):
                    image = cv2.flip(image, 0)
                elif line.startswith("ADD_TEXT"):
                    cv2.putText(image, line.split(" ")[1], (int(line.split(" ")[2]), int(line.split(" ")[3])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.imwrite(args.image, image)