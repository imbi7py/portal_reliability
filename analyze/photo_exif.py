# https://steemit.com/utopian-io/@steempytutorials/extracting-exif-meta-data-from-images-with-python

import exifread
import os,sys

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # Open image file for reading (binary mode)
path_name = 'https://postfiles.pstatic.net/MjAyMDAxMDZfMTg3/MDAxNTc4Mjk1NTc0ODE2.CKcCZDx7HOZmHoToXuaqnJ6UU1yjx2IwvQtDaNnMgKwg.gRphPjFExbEPQcT5iDBlRUBpfKxD9ux2AAf60pOkXhcg.JPEG.imdressholic/20200105_161110.jpg?type=w966'

def process_image(filename):
    # Open image file for reading (binary mode)
    f = open(filename, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)

    '''
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            print("Key: %s, value %s" % (tag, tags[tag]))
    '''
    # DSLR 정보와 관련 있는 key 는 Image Make, Image Model

    return tags['Image Make']

print(f"EXIF Image Make : {process_image(path_name)}")
