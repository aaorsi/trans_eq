import numpy as np
import pylab as pl
import os


import read_data as read
import tools 
from scipy.optimize import curve_fit
from miscvars import *
import matplotlib.gridspec as gridspec

RootDir = os.getcwd()

def compute_transform(FilterSetName, use_subsample=None,fitting_function='linear',makeplot=True):

  Filterstrings = cfhtls_strings if FilterSetName == 'CFHTLS' else sdss_strings

  ngsl = read.open_ngsl()
  jplus_filters = read.open_filters('JPLUS_CCD_QE')
  sdss_filters = read.open_filters(FilterSetName)

  jpluscentralw = jplus_filters['MeanWavelength']
  sdsscentralw  = sdss_filters['MeanWavelength']

  print 'spectra and filters data read'

  njplus = len(jplus_filters['filters'])
  nsdss  = len(sdss_filters['filters'])
  nspec  = len(ngsl['speclist'])

  print 'nspec %ld ' % nspec

  use_subsample = 'None'

  use_OB = True if use_subsample == 'OB' else False
  use_A  = True if use_subsample == 'A' else False

  outname = ''

  if use_OB:
    nspec = len(ob_stars_list)
    outname = 'ob.'
  elif use_A:
    nspec = len(a_stars_list)
    outname = 'a.'
  else:
    outname = 'all.'

  strfitfunc = fitting_function # [fitfunc]

  if strfitfunc == 'linear':
    FittingFunction = tools.modelcolor
  else:
    FittingFunction = tools.modelcolor_poly

  if strfitfunc == 'secondgrade':
    deg = 2
  elif strfitfunc == 'thirdgrade':
    deg = 3
  else:
    deg = 0

  outName = '%s.%s.%s' % (FilterSetName, strfitfunc,outname)
  
  i_r = 2 # index of i filter [No idea why this]

  coeffFile = '../out/'+outName+'coeff.dat'
  print 'File to be written with transformation equations: \n%s ' % coeffFile
  f = open(coeffFile,'w')

  f.write(r'\begin{tabular}{lccccc}'+'\n')
  f.write(r'\hline'+'\n')
  f.write(r' & $a$ & $g-i$ & $i-r$ & $r-u$ & $u-z$ \\'+'\n')
  f.write(r'\hline'+'\n')

  for ij in range(njplus):  # One equation per J-plus filter
    ydata = np.zeros(nspec) # jplus - sdss
    magj_all = np.zeros(nspec) # jplus alone
    mags_all = np.zeros(nspec) # sdss alone
    jfilter = tools.get_filterdata(jplus_filters,ij)
    sfilter = tools.get_filterdata(sdss_filters,i_r)


    for k in range(nspec):
      if use_OB:
        kspec = tools.get_spec(ngsl,k,namespec=ob_stars_list[k])
      elif use_A:
        kspec = tools.get_spec(ngsl,k,namespec=a_stars_list[k])
      else:
        kspec = tools.get_spec(ngsl,k)
      
      mag_j = tools.get_mag(jfilter,kspec)
      mag_s = tools.get_mag(sfilter,kspec)
      ydata[k] = mag_j - mag_s
      magj_all[k] = mag_j
      mags_all[k] = mag_s


    def fitmodel(x,*p):
      if hasattr(x,"__len__"):
        nx = len(x)
        res = np.zeros(nx)
        for i in range(nx):
          res[i] = FittingFunction(sdss_filters,tools.get_spec(ngsl,x[i]),
          *p) if strfitfunc == 'linear' else FittingFunction(sdss_filters,
          tools.get_spec(ngsl,x[i]),jpluscentralw[ij],deg,*p)
      else:    
        res = FittingFunction(sdss_filters,tools.get_spec(ngsl,x[i]),
        *p) if strfitfunc == 'linear' else FittingFunction(sdss_filters,
        tools.get_spec(ngsl,x[i]),jpluscentralw[ij],deg,*p)
      
      return res
    
    print 'ydata constructed for filter ',ij
    coeff, err = curve_fit(fitmodel,np.arange(nspec),ydata,p0 = [1.,1.,1.,1.,1.])  
    print coeff
    
    coeff_str = ''
    for i in range(len(coeff)):
      coeff_str += '& %.3f ' % (coeff[i]) 

    f.write(r'$'+jplus_strings(jplus_filters['filters'][ij])+'-'+Filterstrings(sdss_filters['filters'][i_r])+'$'+coeff_str+r'\\'+'\n')

    xspec = np.linspace(0,nspec-1,num=nspec,dtype='i')
    
    deltamag = fitmodel(xspec,*coeff) + mags_all - magj_all # jplus_model - jplus_measured

    
    if makeplot:

      gs = gridspec.GridSpec(1,3)
      gs.update(wspace=0.0)
      ax = pl.subplot(gs[0,0:2])


      ax.plot(xspec,deltamag,color='blue',label=jplus_filters['filters'][ij])
      ax.plot([0,nspec],[0,0],'--',color='black')
      ax.fill_between([0,nspec],[-0.1,-0.1],[0.1,0.1],color='gray',alpha=0.5)
      ax.set_xlabel('NGSL star',fontsize=15)
      ax.set_ylabel(r'$J_{+}^{model} - J_{+}^{data}$',fontsize=15)
      ax.set_ylim([-.5,.5])
      ax.legend()
      if use_OB:
        ax.set_title('OB stars from NGSL')
      
      if use_A:
        ax.set_title('A stars from NGSL')
     
      
      ax = pl.subplot(gs[0,2])

      n, nbins,patches = ax.hist(deltamag,np.round(100*(nspec/400.0)**(2./3)),normed=1,label=jplus_filters['filters'][ij],range=[-.5,.5],alpha=0.5,orientation="horizontal")
    #  pl.fill_between([-0.1,0.1],[0.0,0.0],[n.max(),n.max()],color='gray',alpha=0.5)
      
      ax.set_ylim([-.5,.5])
      ax.get_xaxis().set_ticks([])
      ax.get_yaxis().set_ticks([])

      meann = np.median(deltamag)
      stdn  = np.std(deltamag)

      ax.text(0.3,0.9,r'$<\Delta_m> = %.3f$' % (meann),transform=ax.transAxes,fontsize=15)
      ax.text(0.3,0.85,r'$\sigma = %.3f$' % (stdn),transform=ax.transAxes,fontsize=15)

      print meann
  #  import pdb ; pdb.set_trace()
   # pl.legend()
    #pl.xlabel(r'$J_{+}^{model} - J_{+}^{data}$',fontsize=15)
    
  #  pl.show()
      pl.savefig('../plots/'+outname+jplus_filters['filters'][ij]+'.png',dpi=250)
    
  f.write(r'\end{tabular}')
  f.close()

  return 




