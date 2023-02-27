from motu_wrappy import motu_wrappy as mpy

command, dict_request = mpy.build_request(
    serviceid = 'SEALEVEL_GLO_PHY_L4_MY_008_047',
    productid = 'cmems_obs-sl_glo_phy-ssh_my_allsat-l4-duacs-0.25deg_P1D',
    area_wesn = [300,330,-37,-16],
    datemin   = "2017-12-26 00:00:00",
    datemax   = "2017-12-28 00:00:00",
    outdir    = '.',
    outname    = 'duacs',
    variable  = ["adt", "err", "sla", "ugos", "ugosa", "vgos", "vgosa"],
    motu='https://my.cmems-du.eu/motu-web/Motu',
    credential_path='./.copernicus_credentials'
)

mpy.motu_download(command, maxretries=1)



