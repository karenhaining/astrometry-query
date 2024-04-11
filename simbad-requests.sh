#!/bin/bash

LOC=$1
ID=$2

echo $ID
curl https://simbad.cds.unistra.fr/simbad/sim-id?Ident=$ID >> $LOC