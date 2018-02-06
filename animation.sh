#!/bin/sh

f_name="animation.gif"

echo "Switching to correct dir"
cd /home/pi/scripts/

echo "Copy latest photos to animated directory"
python copyAnimRes.py

echo "Generating gif..."
convert -resize 480x480 -delay 40 -loop 0 ./animated/image*.jpg "./out/${f_name}"

echo "Copy to www dir"
cp "./out/${f_name}" "/var/www/html/out/${f_name}"

echo "Touch www index file"
touch "/var/www/html/index.html"
