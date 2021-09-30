from utils import config
from utils import utils as ut
import logging
import pandas as pd


if __name__ == '__main__':
    # This sets the root logger to write to stdout (your console)
    # By default the root logger is set to WARNING and all loggers you define
    # inherit that value. Here we set the root logger to NOTSET. This logging
    # level is automatically inherited by all existing and new sub-loggers
    # that do not set a less verbose level.
    logging.basicConfig(level=logging.NOTSET)


    # BEFORE STARTING, you need to configure:
    
    # - scripts/utils/config.py
    # - data/motu_info.txt 
    

    # 1) Define variables
    # 2) Get information from default dictionary
    # 3) Update dictionary values based on variables defined by the user
    # 4) Get motu client motu_command
    # 5) Download data

    """
    This is an example of the commands used in motuclient used in bash (aviso):
    python -m motuclient --motu https://my.cmems-du.eu/motu-web/Motu
        --service-id SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047-TDS
        --product-id dataset-duacs-rep-global-merged-allsat-phy-l4
        --longitude-min 0.125 --longitude-max -0.125 --latitude-min -50
        --latitude-max -10 --date-min "2020-06-03 00:00:00"
        --date-max "2020-06-03 00:00:00" --variable adt --variable err
        --variable sla --variable ugos --variable ugosa --variable vgos
        --variable vgosa --out-dir <OUTPUT_DIRECTORY>
        --out-name <OUTPUT_FILENAME> --user <USERNAME> --pwd <PASSWORD>
    """

    dataref = 'pcse_bs_aviso'
    # read reference file
    dict_details = ut.get_dict_paths('/path/to/your/motu_info.txt')
    dict_details = dict_details[dataref]

    # 1) Define variables
    database  = dict_details['database']    # the tag for a given dataset in copernicus catalogue
    outname   = dict_details['out_name']    # this is the output tag that will be used in your saved netcdf file
    startTime = dict_details['mparam']['date-min']  # starting date fmt='%Y:%m:d %H:%M:%S'
    endTime   = dict_details['mparam']['date-max']  # ending date fmt='%Y:%m:d %H:%M:%S'
    freq      = dict_details['freq']                # frequency of output (see pd.date_range)
    area      = dict_details['WESN']                # western eastern southern and northern boundaries
    cop_cred  = dict_details['copernicus_credentials']  # username and password dictionary

    outdir = dict_details['data_raw_path']  # output paths

    # 2) Get information from default dictionary
    mparam = config.motu_params[database]   # This values are replaced below

    # 3) Update dictionary values based on variables defined by the user
    for k in dict_details['mparam']:
        mparam[k] = dict_details['mparam'][k]

    mparam['user'] = ut.copernicus_credentials(cop_cred)['user']
    mparam['pwd'] = ut.copernicus_credentials(cop_cred)['pass']
    mparam['out-dir'] = outdir

    timerange = pd.date_range(startTime, endTime, freq=freq)

    for t0, t1 in zip(timerange[:-1], timerange[1:]):
        t0 = str(t0)
        t1 = str(t1)
        mparam['date-min'] = t0
        mparam['date-max'] = t1
        mparam['out-name'] = f"{outname}_{t0.replace(' ', '_')}_{t1.replace(' ', '_')}.nc"
        # 4) Get motu client motu_command
        mcommand = ut.motu_command(mparam)

        # 5) Download data
        # retrying three
        ut.retry(ut.motu_download(mcommand))
