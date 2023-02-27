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



