#!/bin/sh

# define a timestamp function
timestamp() {
  date +"%Y-%m-%d_%H-%M-%S"
}

f_name="photo.jpg"
bak_f_name="$(timestamp).jpg"

echo "Switching to correct dir"
cd /home/pi/scripts/

echo "Taking photo...${bak_f_name}"
raspistill -o "./out/${f_name}" -w 720 -h 720 -hf -vf 2>&1

echo "Rotating photo..."
convert -rotate 270 "./out/${f_name}" "./out/${f_name}"

echo "Copy to backup dir"
cp "./out/${f_name}" "./out/${bak_f_name}"

# echo "Copy to www dir"
# cp "./out/${f_name}" "/var/www/html/out/${f_name}"

# echo "Touch www index file"
# touch "/var/www/html/index.html"

echo "Calling animated Gif script"
/bin/bash ./animation.sh
