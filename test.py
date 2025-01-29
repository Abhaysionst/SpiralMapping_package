

import imp,SpiralMap, dtools
imp.reload(SpiralMap)
import SpiralMap as sp
import matplotlib.pyplot as plt
plt.ion()

plt.close('all')
plt.figure(figsize=(6,6))
# plotattrs = {'plot':True,'coordsys':'GC','markSunGC':True,'xmin':-16,'xmax':8,'ymin':-12,'ymax':12}
plotattrs = {'plot':True,'coordsys':'GC','markSunGC':False}
spirals = sp.main_()
spirals.getinfo(model='Drimmel_NIR_2000')
# spirals.readout(plotattrs,model='Reid_2019',arm='Sct-Cen')
spirals.readout(plotattrs,model='Drimmel_NIR_2000',arm='all')


plt.tight_layout()


