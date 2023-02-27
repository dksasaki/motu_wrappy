# motu_wrappy
 A wrapper for Copernicus data download (Motu client) in python

  Motu_wrappy wraps the motu client commands used to download data from the Copernicus catalogue. The idea is to make tedious repetitive tasks more straightforward by enabling python commands. The following example (`example/example1.py`) downloads data from GLORYS reanalysis:

  ```
  from motu_wrappy import motu_wrappy as mpy

command, dict_request = mpy.build_request(
    serviceid = 'GLOBAL_MULTIYEAR_PHY_001_030-TDS',
    productid = 'cmems_mod_glo_phy_my_0.083_P1D-m',
    area_wesn = [300,330,-37,-16],
    datemin   = "2017-12-26 00:00:00",
    datemax   = "2017-12-28 00:00:00",
    depthmin  = 0.493,
    depthmax  = 5902.0581,
    outdir    = '.',
    outname    = 'swatl',
    variable  = ['mlotst', 'so',  'thetao',  'uo',  'vo',  'zos'],
    motu='https://my.cmems-du.eu/motu-web/Motu',
    credential_path='.copernicus_credentials'
)

mpy.motu_download(command, maxretries=1)
```

All the informations presented above are availabel in the [catalogue](https://resources.marine.copernicus.eu/). Select: `desired data > data access > motu > show API call`. 

Notice that the `credential_path` is a two-lines text file you must generate. The first line is your copernicus user name and the second, the password.

## Installation


### Python Dependencies
`mottu_wrappy` depends on motu client, which is compatible with python version 3.4+ (motu client). To install, follow the instructions below:

- [motuclient](https://help.marine.copernicus.eu/en/articles/4796533-what-are-the-motu-client-motuclient-and-python-requirements)
- pandas


### Install wrapper

To install the wrapper, clone the repository and install using pip:

```
git clone git@github.com:dksasaki/motu_wrappy.git
cd motu_wrappy
pip install .
```