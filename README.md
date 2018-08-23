#	OMERO Downloader

This utility executes a batch download and rescaling of images from an OMERO server provided a table of image IDs.
Accessible images are sized and scaled according to user specification and saved in numpy's .npy format, allowing for arbitrarily deep image channels.

##	Requirements

A few typical libraries are required, but most importantly the OMERO gateway requires Python 2.7.
Create a new conda environment, add the following 

```bash
conda config --add channels defaults
conda config --add channels conda-forge
conda config --add channels bioconda
```

```bash
 conda install -c bioconda python-omero numpy pandas scipy
 ```

###	ZeroC ICE Framework

The local machine to which you download files will require the ZeroC ICE framework to handle requests, and may need to be installed by a system admin.
<https://zeroc.com/downloads/ice>

## Usage

Downloading images from OMERO requires a .csv file that contains the image IDs to download under header 'ImageID', similar to the example below.
Although other fields may be provided, the only necessary header is 'ImageID'.

Barcode | Ligand | ImageID
--- | --- | ---
LI8XX1111 | EGF | 3066019
LI8XX1111 | EGF | 3066020
LI8XX1111 | EGC | 3066020


Assuming the .csv file is saved in the current working directory as IDfile.csv, this utility can be called from the command line as usual.
This command will access lincs.ohsu.edu, download all of the ImageIDs in IDfile.csv, rescale them to 64x64 pixels, and save them to save\_dir

```bash
python download_omero.py -s save_dir -i IDfile.csv -x 64 -y 64 -c 255 -o lincs.ohsu.edu
```

You will then be promped for both your username and password for the specified OMERO host.
Once accepted, your download should begin.
