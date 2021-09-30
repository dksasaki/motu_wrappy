# motu_wrappy
## A wrapper for Copernicus data download (Motu client) in python

  Motu_wrappy wraps the motu client commands used to download data from the Copernicus catalogue.

  Four steps are required in order to download a dataset from Copernicus with motu_wrappy, 

  1. get the motuclient info of your desired dataset in the [catalogue](https://resources.marine.copernicus.eu/). You'll need to check the download scripts.
  2. add the motuclient info on the dataset in `motu_params` dictionary in `scripts/utils/configs.py`.
  3. add specific information in `motu_info.txt`
  4. update the dictionary items in `scripts/download_motu.py`

  In order to use the services of copernicus via `scripts/download_motu.py`, a credential is needed. It should be provided as a text file named `scripts/.copernicus_credentials`, where the first line is the user name and the second line the password as in the example below:

  `scripts/.copernicus_credentials`:

    your_copernicus_username
    your_copernicus_password

  Available download options are in `scripts/utils/config.py`. You can add new inputs to the configs by finding a product in https://resources.marine.copernicus.eu and checking the download scripts. 

