import logging
import ast
from collections import OrderedDict
import os
import subprocess


def build_request(serviceid=None,
                  productid=None,
                  area_wesn=None,
                  datemin=None,
                  datemax=None,
                  depthmin=None,
                  depthmax=None,
                  outdir=None,
                  outname=None,
                  variable=None,
                  motu='https://my.cmems-du.eu/motu-web/Motu',
                  credential_path='.copernicus_credentials'):
    """Build the a motuclient feed using a dictionary. Below is an
    an example of the commands used in motuclient used in bash (aviso):

    python -m motuclient --motu https://my.cmems-du.eu/motu-web/Motu
        --service-id SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047-TDS
        --product-id dataset-duacs-rep-global-merged-allsat-phy-l4
        --longitude-min 0.125 --longitude-max -0.125 --latitude-min -50
        --latitude-max -10 --date-min "2020-06-03 00:00:00"
        --date-max "2020-06-03 00:00:00" --variable adt --variable err
        --variable sla --variable ugos --variable ugosa --variable vgos
        --variable vgosa --out-dir <OUTPUT_DIRECTORY>
        --out-name <OUTPUT_FILENAME> --user <USERNAME> --pwd <PASSWORD>

    The arguments of the function correspond to the entries in the example above

    Args:
        serviceid (string): service id
        productid (string): product id
        area_wesn (list): [west, east, south, north]
        datemin (string): format should be "%Y-%m-%d %H:%M:%S"
        datemax (string): format should be "%Y-%m-%d %H:%M:%S"
        depthmin (float): minimum depth
        depthmax (float): maximum depth
        outdir (string) : output path
        outname (string): prefix of the netcdf file
                          the file will be saved as "{outname}_{datemin}_{datemax}.nc
        variable (list): list of requested  variables
        motu (str): Defaults to 'https://my.cmems-du.eu/motu-web/Motu'.
        credential_path (str): text file consisting two lines, where the first correspond
                               to <USERNAME>, while the second correspond to <PASSWORD>.
                               Defaults to '.copernicus_credentials'.

    Returns:
        _type_: _description_
    """                  
    
    
    request_dict = {
        'motu'         : motu,
        'service-id'   : serviceid,
        'product-id'   : productid,
        'longitude-min': area_wesn[0],
        'longitude-max': area_wesn[1],
        'latitude-min' : area_wesn[2],
        'latitude-max' : area_wesn[3],
        'date-min'     : f'\"{datemin}\"',
        'date-max'     : f'\"{datemax}\"',
        'depth-min'    : depthmin,
        'depth-max'    : depthmax,
        'out-dir'      : outdir,
        'out-name'     : f"{outname}_{datemin.replace(' ', 'T')}_{datemax.replace(' ', 'T')}.nc",
        'variable'     : variable,
    }

    cc = copernicus_credentials(fpath=credential_path)

    for i in cc:
        request_dict[i] = cc[i]

    request_dict2 = {}
    for k in request_dict:
        if request_dict[k] is not None:
            request_dict2[k] = request_dict[k]
        else:
            pass

    motucommand = motu_command(request_dict2)
    return motucommand, request_dict2


def motu_command(request_dict):
    """
    Build the motuclient string command based on the mparam dict contents.
    
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
    mainstr = 'python -m motuclient '

    motudict = OrderedDict(request_dict)

    for k in motudict.keys():
        # the dictionary may contain lists and simple variables
        if type(motudict[k]) != list:                   # simple variable
            mainstr = mainstr + f'--{k} {motudict[k]}'
            if k == 'pwd':
                pass  # avoids having an extra ' ' by the end mainstr
            else:
                mainstr += ' '
        elif type(motudict[k]) == list:  # iterate over list
            for i in motudict[k]:
                mainstr = mainstr + f'--{k} {i} '
    return mainstr


def copernicus_credentials(fpath='scripts/.copernicus_credentials'):
    """ read credentials to download copernicus data """

    with open(fpath,'r') as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    credential = {
        'user': content[0],
        'pwd': content[1]
    }

    return credential


def retry(fun, maxretries=3):
    """Retry to run the function 3 times.

    Parameters
    ----------
    fun : functin
        The function to be retried

    Returns
    -------
        None

    """

    nth = { 1: "1st", 2: "2nd", 3: "3rd"}
    for i in range(maxretries):
        try:
           time.sleep(0.3)
           fun()
           logging.info(f'{nth[i]} attempt')
           break
        except Exception:
            continue


def motu_download(mcommand, maxretries=3):
    """Download data using motu client. 


    Args:
        mcommand (string): motu request
        maxretries (int, optional): number of retries if something goes wrong.
                    Defaults to 3.
    """    
    logging.info(mcommand)  # print log information on screen
    print(mcommand)

    # run mcommand in shell and output shell log into shellOutputBin
    shellOutputBin = retry(subprocess.check_output(mcommand, shell=True),
                           maxretries=maxretries)

    # decode from byte format
    shellOutputStr = shellOutputBin.decode()

    # success or error
    if 'Done' in shellOutputStr:
        logging.info(shellOutputStr)
        return 'Success'
    elif 'Excp 11' in shellOutputStr:
        raise TimeoutError(shellOutputStr)
    else:
        raise EOFError(shellOutputStr)


if __name__ == '__main__':

    command, dict_request = build_request(
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
        credential_path='../.copernicus_credentials'
    )

    motu_download(command, maxretries=1)










