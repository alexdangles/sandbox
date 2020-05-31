from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

# Set graphical window, its title and size
win = pg.GraphicsWindow(title="Sample process")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

# Random data process
p6 = win.addPlot(title="Updating plot")
curve = p6.plot(pen='y')
data = np.random.normal(size=(10,1000)) #  If the Gaussian distribution shape is, (m, n, k), then m * n * k samples are drawn.

# plot counter
ptr = 0 

# Function for updating data display
def update():
    global curve, data, ptr, p6
    curve.setData(data[ptr%10])
    if ptr == 0:
        p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
    ptr += 1

# Update data display    
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()