import numpy as np
import scipy.integrate as integral
#import weighted as wp
from scipy.interpolate import interp1d

# script to compute magnitudes

def get_mag(filterdata, specdata):
# filterdata is a np.array([wavelength, T]), specdata is a np.array([wavelength,flux])
# This assumes AB magnitudes, with wavelengths in Angstroms, and fluxes in erg s-1 cm-2 A-1

  nz = np.where(filterdata[:,1] != 0)
  # interpolation of spectrum
  specwfilt = interp1d(specdata[:,0],specdata[:,1],kind='linear',fill_value=0.0,bounds_error=False) 
  # normalization in Flambda due to filter transmission curve
  int_ab = integral.simps(filterdata[nz,1]/filterdata[nz,0],filterdata[nz,0])
  mag = -2.5 * (np.log10(integral.simps(specwfilt(filterdata[nz,0])*filterdata[nz,1],
  filterdata[nz,0])/ int_ab )- 18 - np.log10(3.0)) - 48.60
  return mag

def get_spec(specdict, i,namespec=False):
  
  if namespec:
    specname = namespec
  else:
    specname = specdict['speclist'][i]
  
  specdata = specdict[specname][1].data
  nw = len(specdata['wavelength'])
  spec = np.zeros([nw,2])
  spec[:,0] = specdata['wavelength']
  spec[:,1] = specdata['flux']
  return spec

def get_filterdata(filterdict,i):
  filname = filterdict['filters'][i]
  fdata = filterdict[filname]
  return fdata
  

def modelcolor(filterdict,spec, *p):
  nfilters = len(filterdict['filters'])
  result = p[0]
  for j in range(nfilters-1):
    fj  = get_filterdata(filterdict,j)
    fj1 = get_filterdata(filterdict,j+1) 

    magj  = get_mag(fj,spec)
    magj1 = get_mag(fj1,spec)

    result += p[j+1] * (magj - magj1)

  return result
    
def modelcolor_poly(filterdict,spec,centralw, deg,*p):
  nfilters = len(filterdict['filters'])
  result = p[0]
  warr = filterdict['MeanWavelength']
  
  iclose = np.argmin(np.abs(centralw - warr))

  i0 = iclose if (centralw - warr[iclose]) > 0 else iclose -1
  i1 = i0 -1 if i0 == nfilters-1 else i0 + 1

  result = p[0]

  for i in range(deg):
    
    fj  = get_filterdata(filterdict,i0)
    fj1 = get_filterdata(filterdict,i1)

    magj  = get_mag(fj,spec)
    magj1 = get_mag(fj1,spec)

    result += p[i+1] * (magj - magj1)**(i+1)

  return result

  
