# trans_eq

Computes transformation equations between filter systems. Currently, it computes transformations between the J-PLUS and either SDSS or CFHTLS filter systems. The code can be easily extended to deal with any filter system. To find the coefficients, the code uses the NGSL catalogue of standard stars. Future updates should allow to use any spectroscopic library of objects.

The output is a file containing a LateX table with all coefficients, and a set of plots showing the performance of the equations over the set of templates used.

**Example of usage
```python
from main import *
compute_transform('CFHTLS')

```

**Example of output
(https://github.com/aaorsi/trans_eq/blob/master/plots/all.F378_with_ccd_qe.png)
