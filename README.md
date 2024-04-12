# Astrometry Query

Run images through Astrometry.net to obtain the following information:
- Attitude (ra and dec)
- Centroid location (pixels)
- Centroid pixel brightness
- Star name
- Star magnitude
Queries simbad database to then resolve star name obtained from Astrometry.net to BSC number.

Outputs the data into `results.json`.

## Usage 
Clone the repo. You may need to install astropy: ``pip install astropy``.

1. Get an API key from Astrometry.net. Create a file called `profile.py`, which will simply contain a variable holding your API key (`API_KEY = "*************"`)
2. Create a directory called `raw_data`. Place the images you wish analyzed in here.
3. Run script: `python3 run.py`

## Copyright

Uses a modified file from the Astrometry.net code suite (`client.py`). This file was licensed under a 3-clause BSD style license, which states:

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

* Neither the name of the Astrometry.net Team nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
