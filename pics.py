import os
import subprocess
import json
import re
import numpy as np

import profile

from PIL import Image

# gets the catalog number from an html file from simbad
def get_catalog_num(file):
    final = None
    with open(file) as f:
        for line in f:
            match = re.search('https://vizier\.cds\.unistra\.fr/viz-bin/VizieR-S\?HR.*>HR (.*)</A>', line)
            if match != None:
                final = match

    if final is None:
        return final
    return int(final[1])

# send pics & obtain results from astrometry
# subprocess.run(["./astrometry-requests.sh", profile.API_KEY])

# process results from astrometry
processed_dir = './processed_data'
results = {}

# for every picture:
subfolders = [ f.path for f in os.scandir(processed_dir) if f.is_dir() ]
for dir in os.scandir(processed_dir):
    print(dir.name + " ===================")
    file_res = {}

    path = processed_dir + '/' + dir.name

    # process attitude information
    cal_data = json.load(open(path + "/calibrate.json"))
    file_res["att"] = [cal_data["ra"], cal_data["dec"]]

    # process star information
    ann_data = json.load(open(path + "/annotations.json"))["annotations"]
    centroids = [[x["pixely"], x["pixelx"], x["names"], x["vmag"]] for x in ann_data]

    im = Image.open('./raw_data/' + dir.name) # Can be many different formats.
    pix = im.load()

    # get the catalog number
    for c in centroids:
        star_name = c[2][0].split("/")[0].replace(" ", "+")

        # get page from simbad
        loc = path + "/pics/"
        # subprocess.run(["mkdir", "-p", loc])

        full_file_name = loc + "/" + star_name + ".html"
        # subprocess.run(["./simbad-requests.sh", full_file_name, star_name])

        # get HR num
        num = get_catalog_num(full_file_name)
        c.append(num)

        # get brightness
        x = c[0]
        y = c[1]

        # TODO account for grayscale?
        rgb = pix[y,x]
        brightness = (rgb[0] + rgb[1] + rgb[2])/3

        c.append(brightness)


    print(centroids)

    # x, y, names, mag, cat unmm, bri
    file_res['centroids'] = [[x[0], x[1]] for x in centroids]
    file_res['mags'] = [x[3] for x in centroids]
    file_res['stars'] = [x[4] for x in centroids]
    file_res['brightness'] = [x[5] for x in centroids]

    results[dir.name] = file_res

# write to json file
json_results = json.dumps(results, indent=4)

with open("results.json", 'w') as outfile:
    outfile.write(json_results)