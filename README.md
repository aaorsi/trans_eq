# trans_eq

Computes transformation equations between filter systems. Currently, it computes transformations between the J-PLUS and either SDSS or CFHTLS filter systems. The code can be easily extended to deal with any filter system. To find the coefficients, the code uses the NGSL catalogue of standard stars. Future updates should allow to use any spectroscopic library of objects.

The method used to construct the transformation equations is described in detail in Section 4 of Aparicio-Villegas et al. (2010) for the ALHAMBRA photometric system:

http://adsabs.harvard.edu/abs/2010AJ....139.1242A


The output is a file containing a LateX table with all coefficients, and a set of plots showing the performance of the equations over the set of templates used.

**Example of usage**
```python
from main import *
compute_transform('CFHTLS')

```

**Example of output**
The figure shows the performance of the equations (model - real magnitude) of a J-PLUS narrow filter expressed as a function of CFHT broad band filters.

![Example](https://github.com/aaorsi/trans_eq/blob/master/plots/all.F378_with_ccd_qe.png)
