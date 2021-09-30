import logging
import ast
from collections import OrderedDict
import os
import subprocess


def motu_command(mparam):
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

    motudict = OrderedDict(mparam)

    for k in motudict.keys():
        if type(motudict[k]) != list:
            mainstr = mainstr + f'--{k} {motudict[k]} '
        elif type(motudict[k]) == list:
            for i in motudict[k]:
                mainstr = mainstr + f'--{k} {i} '
    return mainstr


def motu_download(mcommand):
    logging.info(mcommand)  # print log information on screen

    # run mcommand in shell and output shell log into shellOutputBin
    shellOutputBin = subprocess.check_output(mcommand, shell=True)

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




def get_dict_paths(fpath):
    """Read a text file with a dictionary and returns
    the dictionary"""
    file = open(fpath, 'r')
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    return dictionary


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

def copernicus_credentials(fpath='scripts/.copernicus_credentials'):
    """ read credentials to download copernicus data """

    with open(fpath,'r') as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    credential = {
        'user': content[0],
        'pass': content[1]
    }

    return credential
