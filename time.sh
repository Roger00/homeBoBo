#!/bin/sh

# define a timestamp function
timestamp() {
  date +"%Y-%m-%d"
}

# timelapse parameters 
width=1280
height=720
total_length=86400000
interval=1200000

f_name="$(timestamp)"

echo "Create today's dir"
mkdir /home/pi/scripts/${f_name}

echo "Switching to today's dir"
cd /home/pi/scripts/${f_name}

echo "Start photo series..."
raspistill -t ${total_length} -tl ${interval} -o %04d.jpg -w ${width} -h ${height} -vf -hf 2>&1

echo "Converting to video"
avconv -r 10 -i %04d.jpg -r 10 -vcodec libx264 -vf scale=1280:720 timelapse.mp4
