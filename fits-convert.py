from astropy.table import Table
from astropy.io import fits

# u = Table.read('corr.fits')
# print("-===================")
# print(u[0])
# image_data = fits.getdata('corr.fits')
# print(type(image_data))
from astropy.utils.data import get_pkg_data_filename

# how to get coordinates of pixels
fits_image_filename = get_pkg_data_filename('corr.fits')
table_data = fits.getdata(fits_image_filename,ext=1)
# print(table_data)
u = Table.read('corr.fits')
# print(u.info)


# how to get image data
fits_image_filename2 = get_pkg_data_filename('new-image.fits')
image_data = fits.getdata(fits_image_filename2,ext=0)
# print(image_data[0])
# print(image_data.shape)
# print(fits_image_filename2.info())
print(fits.info(fits_image_filename2))
# only the


v = Table.read('rdls.fits')
print(v.info)
"""
name  dtype  unit
---- ------- ----
  RA float64  deg
 DEC float64  deg
 """
print(v)

fits_image_filename2 = get_pkg_data_filename('wcs.fits')
# image_data = fits.getdata(fits_image_filename2,ext=0)
# print(image_data[0])
# print(image_data.shape)
# print(fits_image_filename2.info())
print(fits.info(fits_image_filename2))


# fits.info(fits_image_filename)

# with fits.open(fits_image_filename) as hdul:  # open a FITS file
#     data = hdul[1].data  # assume the first extension is an image

# image = fits.open('jet.fits')
# image.info()

# ccd = CCDData.read('corr.fits')

# print(data)
# print(u)
