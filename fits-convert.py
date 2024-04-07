from astropy.table import Table
from astropy.io import fits

t = Table.read('axy.fits')
u = Table.read('corr.fits')

# print(t)
# print(t.info)
print(u.info)

print("-===================")
print(u[0])
image_data = fits.getdata('corr.fits')
print(image_data[0])

# print(u)
