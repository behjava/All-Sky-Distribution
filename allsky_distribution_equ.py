#plot union2.1 all sky

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
import matplotlib
import math


def galat(alpha,delta):
    return np.arcsin(np.cos(delta)*np.cos(0.4735)*np.cos(alpha-3.3660)+np.sin(delta)*np.sin(0.4735))

def galong(alpha,delta,gal_lat):
    return np.arctan2((np.sin(delta)-np.sin(gal_lat)*np.sin(0.4735)),(np.cos(delta)*np.sin(alpha-3.3660)*np.cos(0.4735)))+0.5747


galat=np.vectorize(galat) 
galong=np.vectorize(galong) 

alpha = np.linspace(0,2*np.pi,5000)

equatorlat=galat(alpha,0)
equatorlong=galong(alpha,0,equatorlat)

for i in range(len(equatorlat)):
    if equatorlong[i]<np.pi:
        equatorlong[i]=-equatorlong[i]
    else:
        equatorlong[i]=2*np.pi-equatorlong[i]
        

#RA,DEC,longt,lat,t,et,v, bt, ebt, btc, mabs=np.genfromtxt("hyperleda_all_gals_vless7000.txt", unpack=True)
#RA,DEC,longt,lat,t,et,v, bt, ebt, btc, mabs=np.genfromtxt("ra_dec_l_b_t-et_v_bt-ebt_btc_mabs_have-t_only.txt", unpack=True)
RA,DEC,longt,lat,t,et,v, bt, ebt, btc, mabs=np.genfromtxt("ra_dec_l_b_t-et_v_bt-ebt_btc_mabs_have-t-and-mabs.txt", unpack=True)
#longt,lat,btc, mabs,v=np.genfromtxt("l_b_btc_mabs_v_have_not_t.txt", unpack=True)    

  
l=np.zeros(len(longt))
b=np.zeros(len(longt))
ra=np.zeros(len(longt))
dec=np.zeros(len(longt))


for i in range(len(longt)):
    b[i]=lat[i]*math.pi/180.0
    if longt[i]<180:
        l[i]=-(longt[i]*math.pi/180.0)
    else:
        l[i]=2*math.pi-(longt[i]*math.pi/180.0)
    
# 0=0 180=-pi 180=pi 270 =3pi/2 360 = 0
for i in range(len(longt)):
    dec[i]=DEC[i]*math.pi/180.0
    if RA[i]*15<180:
        ra[i]=-(RA[i]*15*math.pi/180.0)
    else:
        ra[i]=2*math.pi-(RA[i]*15*math.pi/180.0)

# 0=-pi 360=pi
#for i in range(len(longt)):
#    dec[i]=DEC[i]*math.pi/180.0
#    ra[i]=(RA[i]*15*math.pi/180.0)-math.pi
   


    
    
#fig = plt.figure(figsize=(23,14))
#fig = plt.figure(figsize=(13,8))
fig = plt.figure(figsize=(16,10))
ax = fig.add_subplot(111, projection="mollweide")
plt.setp(ax.get_yticklabels(), visible=False)
plt.setp(ax.get_xticklabels(), visible=False)
plt.grid(True)
ax.grid(color='black', linestyle='-', linewidth=1)
#im=ax.scatter(l,b,c=btc,s=10,edgecolors='none')#,cmap='ocean')
im=ax.scatter(l,b,c=v,s=10,edgecolors='none',cmap='jet')
#im=ax.scatter(l,b,c=np.log10(v),s=10,edgecolors='none',cmap='Paired')
#im=ax.scatter(ra,dec,c=t,s=10,edgecolors='none')
#im=ax.scatter(l,b,c=mabs,s=10,edgecolors='none')

#cbar=fig.colorbar(im,cax=None,shrink=0.7,ticks=np.arange(-5,10.1,1),orientation="horizontal",pad=0.02)
#cbar.set_label("de Vaucouleurs morphological type $T$", size=25)

#cbar=fig.colorbar(im,cax=None,shrink=0.7,ticks=np.arange(1,5,1),orientation="horizontal",pad=0.02)
#cbar.set_label("$log_{10}(Radial$ $Velocity)$", size=25)

cbar=fig.colorbar(im,cax=None,shrink=0.7,orientation="horizontal",pad=0.02)
cbar.set_label("$V_{CMB}$ (km/s)", size=25)

#cbar=fig.colorbar(im,cax=None,shrink=0.7,orientation="horizontal",pad=0.02)
#cbar.set_label("Corrected apparent total B magnitude", size=25)

cbar.ax.tick_params(labelsize=25) 



imequator=ax.scatter(equatorlong,equatorlat,s=10,marker='.',facecolor='None',lw=0.8,color="black")

ax.text(0,-1.5,"(0,-90)",fontsize=25)
ax.text(0,1.4,"(0,90)",fontsize=25)
ax.text(-math.pi/2.0,0,"(90,0)",fontsize=25)
ax.text(math.pi/2.0,0,"(270,0)",fontsize=25)
ax.text(0,0,"(0,0)",fontsize=25)
ax.text(-0.95,0.2,"Celestial Equator",fontsize=20,rotation='67')

plt.tight_layout(pad=0.9)


#plt.savefig("v_all_gals_vless14000_have-t-and-mabs.pdf")
plt.show()
