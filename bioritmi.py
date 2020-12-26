# ____  _            _ _             _ 
#| __ )(_) ___  _ __(_) |_ _ __ ___ (_)
#|  _ \| |/ _ \| '__| | __| '_ ` _ \| |
#| |_) | | (_) | |  | | |_| | | | | | |
#|____/|_|\___/|_|  |_|\__|_| |_| |_|_|
# un semplice progamma per la visualizzazione
# dei bioritmi

from datetime import date
import matplotlib.dates
import matplotlib.pyplot as plt
from pylab import *
from numpy import array,sin,pi

data=date(1972,6,9)     # Data di nascita 
t0 = data.toordinal()   # Data di nascita
t1 = date.today().toordinal()
t = array(range((t1-33),(t1+33))) # range di 66 giorni

y = 100*[sin(2*pi*(t-t0)/23),  	  # Fisico
         sin(2*pi*(t-t0)/28),     # Emozionale
         sin(2*pi*(t-t0)/33)];    # Intellettuale

# converting ordinals to date
label = []
for p in t:
	label.append(date.fromordinal(p))

fig = figure()
ax = fig.gca()

datas=data.strftime('%m/%d/%Y')

plt.title("Bioritmi. Data: "+ datas)
plt.plot(label,y[0],label,y[1],label,y[2])
plt.legend(['Fisico', 'Emozionale', 'Intellettuale'])
# formatting the dates on the x axis
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d/%b'))
plt.grid()
plt.show()
