# Reading routines 

import numpy as np
import pdb
import glob
import string
from astropy.io import fits
import weighted as wp
import os

RootDir = string.rsplit(os.getcwd(),'/',1)[0] + '/data/'

def open_ngsl():

  flist = glob.glob(RootDir + '*fits')
  nfiles = len(flist)
  
  print '%ld files in %s' % (nfiles, RootDir)

  specnamelist = []
  ngsl_data = {}

  for i in range(nfiles):
    specname = string.rsplit(flist[i],'/',1)[1].rsplit('.',1)[0]
    specnamelist.append(specname)
    hdulist = fits.open(flist[i])
    
    ngsl_data.update({specname:hdulist})
  
  ngsl_data.update({'speclist':specnamelist})
  return ngsl_data



def open_filters(fdir,usecols=[0,1]):
  ff = RootDir + fdir + '/'
  fil_ext = 'fil' if fdir == 'CFHTLS' else 'dat'
  flist = glob.glob(ff+'*.'+fil_ext)
  nfilters = len(flist)

  print '%ld filters found for %s' % (nfilters, fdir)
  if nfilters == 0:
    raise ValueError('no filters found!')

  filters = {}#'flist':flist}
  filters_sorted = {}#'flist':flist}
  fname = []
  meanw = []
  for i in range(nfilters):
    fdata = np.loadtxt(flist[i],usecols=usecols)
    filtername = string.rsplit(flist[i],'/',1)[1].rsplit('.',1)[0]
    fname.append(filtername)
    meanw.append(wp.quantile(fdata[:,0],fdata[:,1],0.5))
    filters.update({filtername:fdata})
  filters.update({'filters':fname})
  filters.update({'MeanWavelength':meanw})
  
  wsort = np.argsort(filters['MeanWavelength'])
  fnamelist = np.asarray(filters['filters'])[wsort]

  filters_sorted.update({'filters':fnamelist})
  for i in range(nfilters):
    f_i = fnamelist[i]
    filters_sorted.update({f_i:filters[f_i]})

  filters_sorted.update({'MeanWavelength':np.asarray(filters['MeanWavelength'])[wsort]})

  return filters_sorted




