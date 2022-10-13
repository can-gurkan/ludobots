import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/BackLegSensorData.npy')
frontLegSensorValues = numpy.load('data/FrontLegSensorData.npy')
print(backLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues,label='BackLeg',linewidth=3)
matplotlib.pyplot.plot(frontLegSensorValues,label='FrontLeg')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

