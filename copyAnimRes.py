from shutil import copyfile
import os

def listJPEGs(dirPath):
    return sorted([os.path.join(dirPath, path) for path in os.listdir(dirPath) if path.endswith('.jpg')])

def copy_and_rename(jpgs):
    for i in range(len(jpgs)):
        dst = '%s/image%04d.jpg' % (getOutputDir(), i)
        print 'src: ', jpgs[i]
        print 'dst: ', dst
        copyfile(jpgs[i], dst)

def getOutputDir():
    return './animated'

def getPhotoDir():
    return './out'

def main():
    # list latest photo
    jpgs = listJPEGs(getPhotoDir())[-12:]

    # copy and rename
    copy_and_rename(jpgs)

    # make animated gif using ImageMagick

    print 'Done'

if __name__ == '__main__':
    main()
