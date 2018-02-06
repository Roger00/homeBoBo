# homeBoBo
Home surveillance using RPi

Crontab scripts - $ sudo crontab -e

	# m h  dom mon dow   command
	*/10 * * * * sudo /home/pi/scripts/photo.sh > /tmp/photo.output
	* * * * * env > /tmp/env.output
	# 0 4 * * * sudo /home/pi/scripts/time.sh > /tmp/time.output
	@reboot sudo python /home/pi/scripts/pir.py > /tmp/pir.output


* Note: need to add Apache Linux user (www-data) to the permission group which allows GPIO usage.
