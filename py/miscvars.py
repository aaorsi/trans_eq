# additional arrays and vectors

def sdss_strings(fname):
  if fname == 'SDSS_z_thrp':
    strname = 'Sloan_z'
  elif fname == 'SDSS_u_thrp':
    strname = 'Sloan_u'
  elif fname == 'SDSS_r_thrp':
    strname = 'Sloan_r'
  elif fname == 'SDSS_i_thrp':
    strname = 'Sloan_i'
  elif fname == 'SDSS_g_thrp':
    strname = 'Sloan_g'
  else: 
    print 'filter name '+fname+' not recognised'
    strname = ''
  
  return strname

def cfhtls_strings(fname):
  if fname == 'uMega':
    strname = r'u_{\rm CFHT}'
  elif fname == 'gMega':
    strname = r'g_{\rm CFHT}'
  elif fname == 'rMega':
    strname = r'r_{\rm CFHT}'
  elif fname == 'iMega':
    strname = r'i_{\rm CFHT}'
  elif fname == 'zMega':
    strname = r'z_{\rm CFHT}'
  else: 
    print 'filter name '+fname+' not recognised'
    strname = ''
  
  return strname

def jplus_strings(fname):
  if fname == 'z_sdss_with_ccd_qe':
    strname = r'z_{\rm JAVA}'
  elif fname == 'r_sdss_with_ccd_qe':
    strname = r'r_{\rm JAVA}'
  elif fname == 'i_sdss_with_ccd_qe':
    strname = r'i_{\rm JAVA}'
  elif fname == 'g_sdss_with_ccd_qe':
    strname = r'g_{\rm JAVA}'
  elif fname == 'F861_with_ccd_qe':
    strname = 'J0861'
  elif fname == 'F660_with_ccd_qe':
    strname = 'J0660'
  elif fname == 'F515_with_ccd_qe':
    strname = 'J0515'
  elif fname == 'F430_with_ccd_qe':
    strname = 'J0430'
  elif fname == 'F410_with_ccd_qe':
    strname = 'J0410'
  elif fname == 'F395_with_ccd_qe':
    strname = 'J0395'
  elif fname == 'F378_with_ccd_qe':
    strname = 'J0378'
  elif fname == 'F348_with_ccd_qe':
    strname = r'u_{\rm JAVA}'
  else: 
    print 'filter name '+fname+' not recognised'
    strname = ''

  return strname

ob_stars_list = ['h_stis_ngsl_bd+75d325_v2',
                 'h_stis_ngsl_cd-691618_v2',
                 'h_stis_ngsl_hd000358_v2',
                 'h_stis_ngsl_hd000886_v2',
                 'h_stis_ngsl_hd003360_v2',
                 'h_stis_ngsl_hd004727_v2',
                 'h_stis_ngsl_hd017081_v2',
                 'h_stis_ngsl_hd027295_v2',
                 'h_stis_ngsl_hd030614_v2',
                 'h_stis_ngsl_hd034078_v2',
                 'h_stis_ngsl_hd034797_v2',
                 'h_stis_ngsl_hd034816_v2',
                 'h_stis_ngsl_hd036960_v2',
                 'h_stis_ngsl_hd037202_v2',
                 'h_stis_ngsl_hd047839_v2',
                 'h_stis_ngsl_hd048279_v2',
                 'h_stis_ngsl_hd057060_v2',
                 'h_stis_ngsl_hd057061_v2',
                 'h_stis_ngsl_hd079469_v2',
                 'h_stis_ngsl_hd091316_v2',
                 'h_stis_ngsl_hd096446_v2',
                 'h_stis_ngsl_hd106304_v2',
                 'h_stis_ngsl_hd109387_v2',
                 'h_stis_ngsl_hd110073_v2',
                 'h_stis_ngsl_hd117880_v2',
                 'h_stis_ngsl_hd128801_v2',
                 'h_stis_ngsl_hd138749_v2',
                 'h_stis_ngsl_hd142926_v2',
                 'h_stis_ngsl_hd147394_v2',
                 'h_stis_ngsl_hd147550_v2',
                 'h_stis_ngsl_hd149382_v2',
                 'h_stis_ngsl_hd155763_v2',
                 'h_stis_ngsl_hd160762_v2',
                 'h_stis_ngsl_hd163641_v2',
                 'h_stis_ngsl_hd164353_v2',
                 'h_stis_ngsl_hd164402_v2',
                 'h_stis_ngsl_hd174959_v2',
                 'h_stis_ngsl_hd175156_v2',
                 'h_stis_ngsl_hd175640_v2',
                 'h_stis_ngsl_hd176437_v2',
                 'h_stis_ngsl_hd187879_v2',
                 'h_stis_ngsl_hd196426_v2',
                 'h_stis_ngsl_hd196662_v2',
                 'h_stis_ngsl_hd224801_v2',
                 'h_stis_ngsl_hd224926_v2'
                 ]


a_stars_list = ['h_stis_ngsl_bd-122669_v2',
                'h_stis_ngsl_cd-259286_v2',
                'h_stis_ngsl_hd000319_v2',
                'h_stis_ngsl_hd002857_v2',
                'h_stis_ngsl_hd015089_v2',
                'h_stis_ngsl_hd018769_v2',
                'h_stis_ngsl_hd019445_v2',
                'h_stis_ngsl_hd028978_v2',
                'h_stis_ngsl_hd038237_v2',
                'h_stis_ngsl_hd040573_v2',
                'h_stis_ngsl_hd041357_v2',
                'h_stis_ngsl_hd050420_v2',
                'h_stis_ngsl_hd059612_v2',
                'h_stis_ngsl_hd072968_v2',
                'h_stis_ngsl_hd074721_v2',
                'h_stis_ngsl_hd078362_v2',
                'h_stis_ngsl_hd086986_v2',
                'h_stis_ngsl_hd087737_v2',
                'h_stis_ngsl_hd093329_v2',
                'h_stis_ngsl_hd095418_v2',
                'h_stis_ngsl_hd097633_v2',
                'h_stis_ngsl_hd108945_v2',
                'h_stis_ngsl_hd109995_v2',
                'h_stis_ngsl_hd111786_v2',
                'h_stis_ngsl_hd114330_v2',
                'h_stis_ngsl_hd140232_v2',
                'h_stis_ngsl_hd141795_v2',
                'h_stis_ngsl_hd141851_v2',
                'h_stis_ngsl_hd142703_v2',
                'h_stis_ngsl_hd143459_v2',
                'h_stis_ngsl_hd163346_v2',
                'h_stis_ngsl_hd164257_v2',
                'h_stis_ngsl_hd164967_v2',
                'h_stis_ngsl_hd166283_v2',
                'h_stis_ngsl_hd166991_v2',
                'h_stis_ngsl_hd167946_v2',
                'h_stis_ngsl_hd170973_v2',
                'h_stis_ngsl_hd172230_v2',
                'h_stis_ngsl_hd174240_v2',
                'h_stis_ngsl_hd174966_v2',
                'h_stis_ngsl_hd183324_v2',
                'h_stis_ngsl_hd194453_v2',
                'h_stis_ngsl_hd201377_v2',
                'h_stis_ngsl_hd201601_v2',
                'h_stis_ngsl_hd204041_v2',
                'h_stis_ngsl_hd205811_v2',
                'h_stis_ngsl_mmj6476_v2',
                'h_stis_ngsl_mmj6490_v2',
                'h_stis_ngsl_vbnvul_v2']

