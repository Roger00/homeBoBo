#!/bin/sh

# define a timestamp function
timestamp() {
  date +"%Y-%m-%d_%H-%M-%S"
}

# select output folder
if [ "${1}" = "pir" ]; then
	out_folder="./pir_out/"
else
	out_folder="./out/"
fi

echo "Source argument: $1"
echo "Output folder: ${out_folder}"

f_name="photo.jpg"
bak_f_name="$(timestamp).jpg"

# echo "Switching to correct dir"
# cd /home/pi/scripts/

echo "Taking photo...${bak_f_name}"
raspistill -o "${out_folder}${f_name}" -w 720 -h 720 -hf -vf 2>&1

echo "Rotating photo..."
convert -rotate 270 "${out_folder}${f_name}" "${out_folder}${f_name}"

echo "Adding water mark..."
python waterMark.py "${out_folder}${f_name}" "${out_folder}${f_name}"

echo "Copy to backup dir"
cp "${out_folder}${f_name}" "${out_folder}${bak_f_name}"

# select output folder
if [ "${1}" = "pir" ]; then
	echo "Copy to www dir"
	cp "${out_folder}${f_name}" "/var/www/html/pir_out/${f_name}"

	echo "Touch www index file"
	touch "/var/www/html/index.html"
else
	echo "Calling animated Gif script"
	/bin/bash ./animation.sh
fi
