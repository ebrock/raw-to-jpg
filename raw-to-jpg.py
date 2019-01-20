import sys, os, argparse
from rawkit.raw import Raw
import numpy as np
from PIL import Image

def raw_to_jpg(file):
	try:
		with Raw(file) as raw_image:
			buffered_image = np.array(raw_image.to_buffer())
			im = Image.frombuffer('RGB', (raw_image.metadata.width, raw_image.metadata.height), buffered_image, 'raw', 'RGB', 0, 1)
			im.save(os.path.split(file)[1] + '.jpg')
			print('Successfully saved file as JPG.')
	except OSError:
		print('Invalid file or location. Check your data. File: %s' % file)


def check_if_raw(file):
	filename = file
	try:
		filename_ext = filename.split('.')

		if filename_ext[1] == 'CR2':
			print('PASS: \'%s\' is CR2 file.' % filename)
			raw_to_jpg(filename)
		else:
			print('FAIL: \'%s\' is \'%s\', not CR2.' % (filename, filename_ext[1]))

	except IndexError:
		print('FAIL: \'%s\' is not a valid file.' % filename)

photo = sys.argv[1]
if os.path.exists(photo):
	raw_to_jpg(photo)
else:
	print("Not a valid file")