import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rcParams, patches
import numpy
import pandas
#from pylab import savefig, subplot

rcParams['axes.titlepad'] = 20
rcParams['figure.subplot.hspace'] = 0.4

#rcParams['figure.edgecolor'] = 'k'
#rcParams['figure.facecolor'] = 'k'
#rcParams['axes.facecolor'] = 'w'
##rcParams['axes.edgecolor'] = 'k'
##rcParams['grid.color'] = 'w'
#rcParams['xtick.color'] = 'w'
#rcParams['ytick.color'] = 'w'
#rcParams['axes.labelcolor'] = 'w'

fig = plt.figure(figsize=(10, 8), facecolor='lightblue', frameon=True)
#rcParams['figure.figsize'] = (10.0, 8.0)
fig.canvas.set_window_title('Geekbrains lesson 8')

#t = numpy.linspace(0, 100, 100)
t = numpy.arange(0, 100, 1)
ax1 = fig.add_subplot(311)
#subplot(311)
f = t ** 3 - numpy.sqrt(t)

p = pandas.DataFrame({'t': t, 'f': f})
data = p.to_csv('sqrt.csv')
df = pandas.read_csv('sqrt.csv', sep=',')

#plt.plot(t, f, color='#FF6600', marker='<', linestyle=':', lw=2, mec='green', markerfacecolor='orange', label='Line1')
ax1.plot(t, f, color='#FF6600', marker='<', linestyle=':', lw=2, mec='green', markerfacecolor='orange', label='Line1')
#plt.grid(c='#BFEFEF', ls='--', lw=0.5)
patch = patches.Patch(color='#FF6600', label='f = t ^ 3 - sqrt(t)')
plt.legend(handles=[patch])
#plt.legend(loc='best')

plt.xlabel('t', fontsize=7)
plt.ylabel('f(t)', fontsize=7)

plt.ylim(0, 800)
plt.xlim(0, 10)

plt.title(r'Графики функций $f = t ^ 3 - sqrt(t), f = t * 2 - cos(t), f = sin(t) +3$', fontsize=14, y=1.05)

for label in ax1.get_xaxis().get_ticklabels():
    # цвет подписи деленений оси OX
    label.set_color('blue')
    # поворот подписей деленений оси OX
    label.set_rotation(45)
    # размер шрифта подписей делений оси OX
    label.set_fontsize(14)

t = numpy.linspace(0., 100, 200)
ax2 = fig.add_subplot(312)
#subplot(312)
f = t*2 - numpy.cos(t)
#plt.plot(t, f, color='red', label='Line2')
ax2.plot(t, f, color='red', label='Line2')
#plt.plot(t, f, color='red', marker='o', linestyle='--', markerfacecolor='blue', label='Line1')
#plt.grid()

patch = patches.Patch(color='red', label='f = t * 2 - cos(t)')
plt.legend(handles=[patch])
#plt.legend('', loc='upper center', ncol=1)

plt.xlabel('t', fontsize=7)
plt.ylabel('f(t)', fontsize=7)

plt.ylim(0, 120)
plt.xlim(0, 60)

for tick in ax2.yaxis.get_major_ticks():
    tick.label1On = True
    tick.label1.set_color('green')
    tick.label2On = True
    tick.label2.set_color('blue')
    # серые деления на оси ОY слева
    tick.tick1line.set_color('grey')
    tick.tick1line.set_markeredgewidth(2)
    tick.tick1line.set_markersize(2)
    # линии вспомогательной сетки для оси OX
    tick.gridOn = True
    tick.gridline.set_color('white')
    tick.gridline.set_linewidth(1.5)

for tick in ax2.xaxis.get_major_ticks():
    tick.label1On = True
    tick.label1.set_color('red')
    tick.label2On = True
    tick.label2.set_color('orange')
    # розовые деления на оси ОX сверху
    tick.tick2line.set_color('pink')
    tick.tick2line.set_markeredgewidth(2)
    tick.tick2line.set_markersize(25)
    # линии вспомогательной сетки для оси OY
    tick.gridOn = True
    tick.gridline.set_color('yellow')
    tick.gridline.set_linewidth(2.)

t = numpy.linspace(0., 4 * numpy.pi, 101)
ax3 = fig.add_subplot(313)
#subplot(313)
f = numpy.sin(t) + 3
ax3.plot(t,f)
#plt.plot(t,f)

plt.fill(t, f, 'r')
plt.axhline(3, color='lightgray', linestyle='--')
plt.text(10.5, 3.05, 'Среднее', fontsize=8)
plt.annotate('Локальный\nминимум', xy=(3 * numpy.pi / 2, 2),
                           xytext=(3.7, 2.7), fontsize=8,
                           arrowprops=dict(arrowstyle='->', color='red'));

plt.plot(t, f, color='lightblue', marker='1', linestyle='-.', lw=3)

plt.xlabel('t', fontsize=7)
plt.ylabel('f(t)', fontsize=7)

patch = patches.Patch(color='lightblue', label='f = sin(t) +3')
plt.legend(handles=[patch])

for ax in fig.axes:
    ax.grid(c='#BFEFEF', ls='--', lw=0.5)


plt.savefig('plot.pdf')
#savefig('plot.pdf')
plt.show()



