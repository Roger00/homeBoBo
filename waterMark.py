import cv2

def main(in_file, out_file):
    print('Reading from image: ' + in_file)
    img = cv2.imread(in_file)

    from time import localtime, strftime
    text = strftime('%Y-%m-%d %H:%M:%S', localtime())
    font = cv2.FONT_HERSHEY_SIMPLEX
    height, width, _channels = img.shape
    position = (width-250, height-10)
    f_size = .6
    f_color = (0, 106, 255)
    cv2.putText(img, text, position, font, f_size, f_color)

    print('Saving to image: ' + out_file)
    cv2.imwrite(out_file, img)

if __name__ == '__main__':
    from sys import argv
    main(argv[1], argv[2])
