import os
import subprocess
import json
import numpy as np
import profile

from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename


# corr file headers:
# field_x, field_y, field_ra, field_dec, index_x, index_y, index_ra, index_dec, 
# index_id, field_id, match_weight, flux, background
CORR_X_IDX = 0
CORR_Y_IDX = 1
CORR_ID_IDX = 8

# send pics & obtain results from astrometry
# subprocess.run(["./requests.sh", profile.API_KEY])

# process results from astrometry
processed_dir = './processed_data'
results = {}

subfolders = [ f.path for f in os.scandir(processed_dir) if f.is_dir() ]
for dir in os.scandir(processed_dir):
    print(dir.name + " ===================")
    file_res = {}

    path = processed_dir + '/' + dir.name

    # for coordinates + identities
    corr_filename = get_pkg_data_filename(path + '/corr.fits')
    corr_data = fits.getdata(corr_filename,ext=1)
    
    # for actual pixel values
    newfits_filename = get_pkg_data_filename(path + '/newfits.fits')
    newfits_data = np.array(fits.getdata(newfits_filename,ext=0))

    # if its rgb, convert to grayscale
    if newfits_data.shape[0] == 3:
        newfits_data = (newfits_data[0] + newfits_data[1] + newfits_data[2]) / 3
    
    centroids = []
    stars = []
    for star in corr_data:
        x = star[CORR_X_IDX]
        y = star[CORR_Y_IDX]
        id = star[CORR_ID_IDX]

        print(id)

        centroids.append([x, y])


    file_res['centroids'] = centroids

    
    print(corr_data.shape)
    print(newfits_data.shape)

    print(corr_data[0])

    results[dir.name] = file_res

# write to json file
json_results = json.dumps(results, indent=4)

with open("results.json", 'w') as outfile:
    outfile.write(json_results)