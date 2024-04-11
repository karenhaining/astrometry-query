import os
import subprocess
import json
import re
import numpy as np
import profile

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
    centroids = [[x["pixely"], x["pixelx"], x["names"]] for x in ann_data]

    # get the catalog number
    for c in centroids:
        star_name = c[2][0].split("/")[0].replace(" ", "+")

        # get page from simbad
        loc = path + "/pics/"
        subprocess.run(["mkdir", "-p", loc])

        full_file_name = loc + "/" + star_name + ".html"
        # subprocess.run(["./simbad-requests.sh", full_file_name, star_name])

        # get HR num
        num = get_catalog_num(full_file_name)
        c[2] = num


    # get brightness

    print(centroids)



    file_res['centroids'] = centroids

    
    results[dir.name] = file_res

# write to json file
json_results = json.dumps(results, indent=4)

with open("results.json", 'w') as outfile:
    outfile.write(json_results)