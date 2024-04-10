import os
import subprocess
import profile

from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename

# send pics & obtain results from astrometry
# subprocess.run(["./requests.sh", profile.API_KEY])

# process results
results_dir = './processed_data'

subfolders = [ f.path for f in os.scandir(results_dir) if f.is_dir() ]
for dir in os.scandir(results_dir):

    corr_filename = get_pkg_data_filename(results_dir + '/' + dir.name + '/corr.fits')
    newfits_filename = get_pkg_data_filename(results_dir + '/' + dir.name + '/newfits.fits')

    corr_data = fits.getdata(corr_filename,ext=1)
    newfits_data = fits.getdata(newfits_filename,ext=0)

    

    print(corr_data.shape)
    print(newfits_data.shape)
