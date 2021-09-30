import os
#############################################################
##----------------- General Configuration -----------------##
#############################################################

local_dir = os.path.dirname(os.path.abspath(__file__)) # auxiliar

"""
the following dictionaries are dummies used by download_motu.py 
the values are replaced within the script by configuration files
motu_info.txt
- the first level of items in motu_params is simply a tag,
used to select a product.
- the second level of items in motu_params are the motuclient's
keys. These information are replaced in download_motu.py
"""


motu_params =   {
    'phy-001-031-daily' : {
        'motu': 'http://my.cmems-du.eu/motu-web/Motu',
        'service-id' : 'GLOBAL_REANALYSIS_PHY_001_031-TDS',
        'product-id': 'global-reanalysis-phy-001-031-grepv2-daily',
        'longitude-min': -180,
        'longitude-max': 179.5,
        'latitude-min': -80,
        'latitude-max': 90,
        'date-min': "2017-12-26 00:00:00",
        'date-max': "2017-12-27 00:00:00",
        'depth-min': 0.5057,
        'depth-max': 5902.0581,
        'out-dir': '<OUTPUT_DIRECTORY>',
        'out-name': '<OUTPUT_DIRECTORY>',
        'variable': [
            'mlotst_cglo', 'mlotst_foam', 'mlotst_glor', 'mlotst_oras',
            'so_cglo', 'so_foam', 'so_glor', 'so_oras',
            'thetao_cglo', 'thetao_foam', 'thetao_glor', 'thetao_oras',
            'uo_cglo', 'uo_foam', 'uo_glor', 'uo_oras',
            'vo_cglo', 'vo_foam', 'vo_glor', 'vo_oras',
            'zos_cglo', 'zos_foam', 'zos_glor', 'zos_oras'],
        'user': '<USERNAME>',
        'pwd': '<PASSWD>',
            },
    'phy-001-031-monthly' : {
        'motu': 'http://my.cmems-du.eu/motu-web/Motu',
        'service-id' : 'GLOBAL_REANALYSIS_PHY_001_031-TDS',
        'product-id': 'global-reanalysis-phy-001-031-grepv2-monthly',
        'longitude-min': -180,
        'longitude-max': 179.5,
        'latitude-min': -80,
        'latitude-max': 90,
        'date-min': "2017-12-26 00:00:00",
        'date-max': "2017-12-27 00:00:00",
        'depth-min': 0.5057,
        'depth-max': 5902.0581,
        'out-dir': '<OUTPUT_DIRECTORY>',
        'out-name': '<OUTPUT_DIRECTORY>',
        'variable': [
            'mlotst_cglo', 'mlotst_foam', 'mlotst_glor', 'mlotst_oras',
            'so_cglo', 'so_foam', 'so_glor', 'so_oras',
            'thetao_cglo', 'thetao_foam', 'thetao_glor', 'thetao_oras',
            'uo_cglo', 'uo_foam', 'uo_glor', 'uo_oras',
            'vo_cglo', 'vo_foam', 'vo_glor', 'vo_oras',
            'zos_cglo', 'zos_foam', 'zos_glor', 'zos_oras'],
        'user': '<USERNAME>',
        'pwd': '<PASSWD>',
            },
    'phy-001-030-daily' : {
        'motu': 'http://my.cmems-du.eu/motu-web/Motu',
        'service-id' : 'GLOBAL_REANALYSIS_PHY_001_030-TDS',
        'product-id': 'global-reanalysis-phy-001-030-daily',
        'longitude-min': -180,
        'longitude-max': 179.5,
        'latitude-min': -80,
        'latitude-max': 90,
        'date-min': "2017-12-26 00:00:00",
        'date-max': "2017-12-27 00:00:00",
        'depth-min': 0.493,
        'depth-max': 5902.0581,
        'out-dir': '<OUTPUT_DIRECTORY>',
        'out-name': '<OUTPUT_DIRECTORY>',
        'variable': ['mlotst', 'so',  'thetao',  'uo',  'vo',  'zos'],
        'user': '<USERNAME>',
        'pwd': '<PASSWD>',
            },
    'SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047': {
        'motu': 'http://my.cmems-du.eu/motu-web/Motu',
        'service-id' : 'SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047-TDS',
        'product-id': 'dataset-duacs-rep-global-merged-allsat-phy-l4',
        'longitude-min': 0.125,
        'longitude-max': -0.125,
        'latitude-min': -89.875,
        'latitude-max': 89.875,
        'date-min': "2017-12-26 00:00:00",
        'date-max': "2017-12-27 00:00:00",
        'out-dir': '<OUTPUT_DIRECTORY>',
        'out-name': '<OUTPUT_DIRECTORY>',
        'variable': ['adt', 'err', 'sla', 'ugos', 'ugosa', 'vgos', 'vgosa'],
        'user': '<USERNAME>',
        'pwd': '<PASSWD>',
            }
        }

