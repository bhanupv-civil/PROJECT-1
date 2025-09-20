# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-22.51.41 127140
# Run by Admin on Mon Dec  2 12:05:25 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=200.708633422852, 
    height=126.907554626465)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
openMdb(pathName='C:/temp/M1.cae')
#: The model database "C:\temp\M1.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
openMdb(
    pathName='C:/Users/Admin/Desktop/bhanu term project/SQUARE standard(250mm).cae')
#: The model database "C:\Users\Admin\Desktop\bhanu term project\SQUARE standard(250mm).cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['30'].parts['P30']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['30'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
o3 = session.openOdb(name='C:/temp/STANDARD.odb')
#: Model: C:/temp/STANDARD.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=574.534, 
    farPlane=961.568, width=601.147, height=272.474, cameraPosition=(109.393, 
    -262.156, 713.206), cameraUpVector=(-0.78472, 0.61728, -0.0563887), 
    cameraTarget=(131.996, 120.739, 47.2637))
session.viewports['Viewport: 1'].view.setValues(nearPlane=515.082, 
    farPlane=1032.95, width=538.942, height=244.279, cameraPosition=(682.069, 
    -247.575, 437.295), cameraUpVector=(-0.813891, 0.0872753, 0.574425), 
    cameraTarget=(131.658, 120.73, 47.4265))
session.viewports['Viewport: 1'].view.setValues(nearPlane=518.66, 
    farPlane=1033.45, width=542.686, height=245.976, cameraPosition=(616.651, 
    -462.344, 174.919), cameraUpVector=(-0.581701, 0.133394, 0.80239), 
    cameraTarget=(131.192, 119.201, 45.558))
session.viewports['Viewport: 1'].view.setValues(nearPlane=518.136, 
    farPlane=1033.98, width=542.138, height=245.728, cameraPosition=(616.651, 
    -462.344, 174.919), cameraUpVector=(-0.246452, 0.428167, 0.869445), 
    cameraTarget=(131.192, 119.201, 45.558))
session.viewports['Viewport: 1'].view.setValues(nearPlane=516.123, 
    farPlane=1034.71, width=540.032, height=244.773, cameraPosition=(621.771, 
    -431.248, 262.404), cameraUpVector=(-0.292626, 0.519373, 0.802884), 
    cameraTarget=(131.242, 119.504, 46.4095))
session.viewports['Viewport: 1'].view.setValues(nearPlane=516.375, 
    farPlane=1034.46, width=540.295, height=244.892, cameraUpVector=(-0.374446, 
    0.449654, 0.810926))
p = mdb.models['30'].parts['P30']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['30'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/STANDARD.odb'])
o3 = session.openOdb(name='C:/temp/240S.odb')
#: Model: C:/temp/240S.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
a = mdb.models['30'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/240S.odb'])
o3 = session.openOdb(name='C:/temp/190S.odb')
#: Model: C:/temp/190S.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=551.627, 
    farPlane=982.206, width=577.179, height=261.61, cameraPosition=(-27.5011, 
    -268.14, 690.638), cameraUpVector=(0.00181118, 0.98078, 0.195107), 
    cameraTarget=(131.996, 120.74, 47.2635))
session.viewports['Viewport: 1'].view.setValues(nearPlane=521.705, 
    farPlane=1015.04, width=545.871, height=247.419, cameraPosition=(-108.191, 
    -515.601, 404.571), cameraUpVector=(-0.00100922, 0.764012, 0.645202), 
    cameraTarget=(132.163, 121.252, 47.8555))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=508.613, 
    farPlane=1025.13, width=532.173, height=241.211, cameraPosition=(-313.088, 
    -485.656, 202.768), cameraUpVector=(0.245272, 0.45992, 0.853414), 
    cameraTarget=(132.198, 121.247, 47.8895))
session.viewports['Viewport: 1'].view.setValues(nearPlane=526.552, 
    farPlane=1011.33, width=550.943, height=249.719, cameraPosition=(-128.294, 
    -579.291, 226.483), cameraUpVector=(0.141743, 0.526641, 0.838187), 
    cameraTarget=(131.805, 121.446, 47.839))
session.viewports['Viewport: 1'].view.setValues(nearPlane=518.033, 
    farPlane=1018.65, width=542.029, height=245.679, cameraPosition=(-185.058, 
    -556.333, 223.377), cameraUpVector=(0.181473, 0.510756, 0.840355), 
    cameraTarget=(131.773, 121.459, 47.8372))
a = mdb.models['30'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/190S.odb'])
o3 = session.openOdb(name='C:/temp/220S.odb')
#: Model: C:/temp/220S.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=613.162, 
    farPlane=919.837, width=641.564, height=290.793, cameraPosition=(141.592, 
    9.63682, 807.633), cameraUpVector=(0.0181318, 0.980872, -0.193806), 
    cameraTarget=(131.997, 120.74, 47.2635))
session.viewports['Viewport: 1'].view.setValues(nearPlane=497.462, 
    farPlane=1033.33, width=520.505, height=235.922, cameraPosition=(-288.671, 
    -403.987, 417.355), cameraUpVector=(0.186115, 0.768016, 0.612791), 
    cameraTarget=(133.122, 121.821, 48.2839))
session.viewports['Viewport: 1'].view.setValues(nearPlane=533.789, 
    farPlane=1003.27, width=558.514, height=253.15, cameraPosition=(-88.0621, 
    -603.337, 171.777), cameraUpVector=(-0.183568, 0.546463, 0.817118), 
    cameraTarget=(132.308, 122.63, 49.2808))
session.viewports['Viewport: 1'].view.setValues(nearPlane=528.469, 
    farPlane=1008.59, width=552.947, height=250.627, cameraPosition=(-88.0621, 
    -603.337, 171.777), cameraUpVector=(0.220615, 0.433338, 0.873812), 
    cameraTarget=(132.308, 122.63, 49.2808))
session.viewports['Viewport: 1'].view.setValues(nearPlane=521.43, 
    farPlane=1014.32, width=545.582, height=247.289, cameraPosition=(-145.69, 
    -577.03, 203.519), cameraUpVector=(0.267456, 0.44793, 0.853127), 
    cameraTarget=(132.306, 122.631, 49.2819))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=522.31, 
    farPlane=1013.44, width=546.503, height=247.706, cameraPosition=(-145.69, 
    -577.03, 203.519), cameraUpVector=(0.152361, 0.494263, 0.855857))
a = mdb.models['30'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/220S.odb'])
o3 = session.openOdb(name='C:/temp/190S.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
a = mdb.models['30'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/190S.odb'])
o3 = session.openOdb(name='C:/temp/150S.odb')
#: Model: C:/temp/150S.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=599.056, 
    farPlane=935.39, width=626.805, height=284.103, cameraPosition=(308.354, 
    161.651, 794.139), cameraUpVector=(-0.41888, 0.860086, -0.29119), 
    cameraTarget=(131.997, 120.74, 47.2635))
session.viewports['Viewport: 1'].view.setValues(nearPlane=501.026, 
    farPlane=1030.72, width=524.234, height=237.612, cameraPosition=(-255.199, 
    -434.658, 408.98), cameraUpVector=(-0.0136884, 0.830919, 0.556224), 
    cameraTarget=(132.938, 121.736, 47.9066))
session.viewports['Viewport: 1'].view.setValues(nearPlane=513.16, 
    farPlane=1019.41, width=536.93, height=243.367, cameraPosition=(-262.581, 
    -487.06, 299.858), cameraUpVector=(-0.0388086, 0.728436, 0.684014), 
    cameraTarget=(132.963, 121.916, 48.2815))
session.viewports['Viewport: 1'].view.setValues(nearPlane=511.383, 
    farPlane=1021.19, width=535.07, height=242.524, cameraPosition=(-262.581, 
    -487.06, 299.858), cameraUpVector=(0.276954, 0.562572, 0.778979), 
    cameraTarget=(132.963, 121.916, 48.2815))
session.viewports['Viewport: 1'].view.setValues(nearPlane=512.52, 
    farPlane=1019.53, width=536.259, height=243.063, cameraPosition=(-335.199, 
    -484.587, -9.03113), cameraUpVector=(0.039057, 0.30076, 0.9529), 
    cameraTarget=(133.173, 121.909, 49.1751))
session.viewports['Viewport: 1'].view.setValues(nearPlane=510.86, 
    farPlane=1020.9, width=534.522, height=242.276, cameraPosition=(-329.111, 
    -484.853, 142.217), cameraUpVector=(0.194167, 0.411525, 0.890475), 
    cameraTarget=(133.153, 121.91, 48.6857))
session.viewports['Viewport: 1'].view.setValues(nearPlane=518.953, 
    farPlane=1015.89, width=542.99, height=246.114, cameraPosition=(-183.883, 
    -549.011, 248.25), cameraUpVector=(0.140372, 0.558935, 0.817244), 
    cameraTarget=(132.656, 122.13, 48.3225))
session.viewports['Viewport: 1'].view.setValues(nearPlane=517.768, 
    farPlane=1017.07, width=541.75, height=245.552, cameraPosition=(-183.883, 
    -549.011, 248.25), cameraUpVector=(0.281158, 0.494147, 0.822659), 
    cameraTarget=(132.656, 122.13, 48.3225))
session.viewports['Viewport: 1'].view.setValues(nearPlane=518.576, 
    farPlane=1016.13, width=542.595, height=245.935, cameraPosition=(-217.135, 
    -556.575, 135.41), cameraUpVector=(0.191111, 0.394064, 0.898994), 
    cameraTarget=(132.703, 122.141, 48.482))
session.viewports['Viewport: 1'].view.setValues(nearPlane=515.629, 
    farPlane=1018.68, width=539.511, height=244.537, cameraPosition=(-211.683, 
    -540.711, 229.066), cameraUpVector=(0.214083, 0.50348, 0.837064), 
    cameraTarget=(132.695, 122.117, 48.3415))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
openMdb(
    pathName='C:/Users/Admin/Desktop/bhanu term project/Hexagon 50mm fix(155mmside).cae')
#: The model database "C:\Users\Admin\Desktop\bhanu term project\Hexagon 50mm fix(155mmside).cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['10'].parts['P10']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['10'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/150S.odb'])
o3 = session.openOdb(name='C:/temp/stdHex.odb')
#: Model: C:/temp/stdHex.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=657.729, 
    farPlane=1082.87, width=705.426, height=319.739, cameraPosition=(472.632, 
    249.82, 846.228), cameraUpVector=(-0.271288, 0.892944, -0.359239), 
    cameraTarget=(140.62, 152.469, 46.145))
session.viewports['Viewport: 1'].view.setValues(nearPlane=628.338, 
    farPlane=1122.64, width=673.903, height=305.451, cameraPosition=(924.045, 
    119.41, 426.093), cameraUpVector=(-0.574072, 0.664058, 0.479028), 
    cameraTarget=(139.899, 152.677, 46.8159))
session.viewports['Viewport: 1'].view.setValues(nearPlane=576.014, 
    farPlane=1178.23, width=617.785, height=280.015, cameraPosition=(803.713, 
    -358.33, 290.125), cameraUpVector=(-0.246545, 0.609997, 0.753073), 
    cameraTarget=(139.377, 150.604, 46.2258))
session.viewports['Viewport: 1'].view.setValues(nearPlane=585.985, 
    farPlane=1166.69, width=628.479, height=284.862, cameraPosition=(-228.986, 
    -608.141, 281.704), cameraUpVector=(0.204791, 0.539812, 0.816495), 
    cameraTarget=(132.981, 149.057, 46.1737))
a = mdb.models['10'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/stdHex.odb'])
o3 = session.openOdb(name='C:/temp/240.odb')
#: Model: C:/temp/240.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=592.652, 
    farPlane=1155.67, width=635.629, height=288.103, cameraPosition=(671.672, 
    -233.252, 619.769), cameraUpVector=(-0.264104, 0.901103, 0.343892), 
    cameraTarget=(140.62, 152.469, 46.1448))
session.viewports['Viewport: 1'].view.setValues(nearPlane=615.08, 
    farPlane=1132.63, width=659.683, height=299.006, cameraPosition=(90.9695, 
    -689.267, 271.406), cameraUpVector=(0.0329032, 0.565659, 0.823983), 
    cameraTarget=(138.978, 151.179, 45.1597))
a = mdb.models['10'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/240.odb'])
o3 = session.openOdb(name='C:/temp/30.odb')
#: Model: C:/temp/30.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=666.041, 
    farPlane=1074.1, width=714.34, height=323.779, cameraPosition=(370.827, 
    24.9791, 877.164), cameraUpVector=(-0.476852, 0.875027, -0.0833082), 
    cameraTarget=(140.62, 152.469, 46.1448))
session.viewports['Viewport: 1'].view.setValues(nearPlane=603.07, 
    farPlane=1125.79, width=646.803, height=293.167, cameraPosition=(-454.158, 
    -43.4509, 651.394), cameraUpVector=(0.683605, 0.61505, 0.392935), 
    cameraTarget=(142.155, 152.596, 46.5648))
session.viewports['Viewport: 1'].view.setValues(nearPlane=578.328, 
    farPlane=1156.28, width=620.266, height=281.139, cameraPosition=(-188.303, 
    -547.638, 443.073), cameraUpVector=(-0.0905546, 0.792563, 0.603029), 
    cameraTarget=(139.923, 156.83, 48.3142))
session.viewports['Viewport: 1'].view.setValues(nearPlane=591.947, 
    farPlane=1144.09, width=634.873, height=287.76, cameraPosition=(-70.9924, 
    -673.288, 209.045), cameraUpVector=(0.0891898, 0.493349, 0.865247), 
    cameraTarget=(139.33, 157.465, 49.4975))
session.viewports['Viewport: 1'].view.setValues(nearPlane=578.936, 
    farPlane=1156.07, width=620.919, height=281.435, cameraPosition=(-167.352, 
    -618.668, 301.127), cameraUpVector=(0.161579, 0.571786, 0.804334), 
    cameraTarget=(139.737, 157.234, 49.1081))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
a = mdb.models['10'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/30.odb'])
o3 = session.openOdb(name='C:/temp/60.odb')
#: Model: C:/temp/60.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=681.8, 
    farPlane=1055.01, width=731.242, height=331.44, cameraPosition=(121.168, 
    -54.5437, 892.673), cameraUpVector=(-0.00982815, 0.994922, -0.100165), 
    cameraTarget=(140.62, 152.469, 46.1449))
session.viewports['Viewport: 1'].view.setValues(nearPlane=560.238, 
    farPlane=1175.97, width=600.865, height=272.346, cameraPosition=(-249.611, 
    -570.284, 333.34), cameraUpVector=(0.0521047, 0.665633, 0.744458), 
    cameraTarget=(142.022, 154.42, 48.2603))
session.viewports['Viewport: 1'].view.setValues(nearPlane=582.047, 
    farPlane=1155.31, width=624.255, height=282.948, cameraPosition=(-210.634, 
    -624.235, 218.849), cameraUpVector=(0.122016, 0.504517, 0.854737), 
    cameraTarget=(141.861, 154.643, 48.7332))
session.viewports['Viewport: 1'].view.setValues(nearPlane=577.052, 
    farPlane=1159.9, width=618.898, height=280.52, cameraPosition=(-222.908, 
    -604.343, 273.933), cameraUpVector=(0.202748, 0.529955, 0.823432), 
    cameraTarget=(141.904, 154.574, 48.5423))
a = mdb.models['10'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/60.odb'])
o3 = session.openOdb(name='C:/temp/110.odb')
#: Model: C:/temp/110.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=672.768, 
    farPlane=1068.67, width=721.555, height=327.049, cameraPosition=(490.17, 
    152.892, 844.679), cameraUpVector=(-0.192296, 0.940486, -0.280193), 
    cameraTarget=(140.62, 152.469, 46.1448))
session.viewports['Viewport: 1'].view.setValues(nearPlane=617.785, 
    farPlane=1116.54, width=662.585, height=300.32, cameraPosition=(-124.985, 
    -210.282, 792.56), cameraUpVector=(0.46457, 0.863444, 0.19657), 
    cameraTarget=(141.306, 152.874, 46.2029))
session.viewports['Viewport: 1'].view.setValues(nearPlane=598.299, 
    farPlane=1140.53, width=641.686, height=290.847, cameraPosition=(-20.4598, 
    -553.309, 529.885), cameraUpVector=(0.0978707, 0.79551, 0.597985), 
    cameraTarget=(140.76, 154.665, 47.5741))
session.viewports['Viewport: 1'].view.setValues(nearPlane=596.87, 
    farPlane=1142.84, width=640.154, height=290.152, cameraPosition=(-12.5182, 
    -632.515, 389.083), cameraUpVector=(0.0428082, 0.678443, 0.733404), 
    cameraTarget=(140.739, 154.872, 47.9426))
session.viewports['Viewport: 1'].view.setValues(nearPlane=588.403, 
    farPlane=1150.89, width=631.073, height=286.036, cameraPosition=(-89.856, 
    -668.467, 217.368), cameraUpVector=(0.100876, 0.501079, 0.859502), 
    cameraTarget=(140.902, 154.948, 48.3048))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
a = mdb.models['10'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/110.odb'])
o3 = session.openOdb(name='C:/temp/150.odb')
#: Model: C:/temp/150.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=693.32, 
    farPlane=1043.91, width=743.597, height=337.04, cameraPosition=(201.64, 
    50.5627, 909.704), cameraUpVector=(-0.268048, 0.941018, -0.206483), 
    cameraTarget=(140.62, 152.469, 46.1448))
session.viewports['Viewport: 1'].view.setValues(nearPlane=571.436, 
    farPlane=1166.67, width=612.875, height=277.789, cameraPosition=(-102.306, 
    -621.641, 360.132), cameraUpVector=(0.0723562, 0.654056, 0.752977), 
    cameraTarget=(141.696, 154.848, 48.0901))
session.viewports['Viewport: 1'].view.setValues(nearPlane=586.775, 
    farPlane=1150.96, width=629.327, height=285.246, cameraPosition=(-128.89, 
    -620.53, 340.342), cameraUpVector=(0.0725173, 0.638239, 0.766415), 
    cameraTarget=(141.777, 154.845, 48.1501))
session.viewports['Viewport: 1'].view.setValues(nearPlane=583.242, 
    farPlane=1154.5, width=625.538, height=283.528, cameraPosition=(-140.629, 
    -634.084, 288.298), cameraUpVector=(0.100951, 0.578365, 0.809508), 
    cameraTarget=(141.815, 154.889, 48.3192))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
a = mdb.models['10'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/temp/150.odb'])
o3 = session.openOdb(name='C:/temp/140.odb')
#: Model: C:/temp/140.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=585.217, 
    farPlane=1161.96, width=627.655, height=284.489, cameraPosition=(474.762, 
    -458.141, 570.88), cameraUpVector=(-0.0998768, 0.856449, 0.506477), 
    cameraTarget=(140.62, 152.469, 46.1448))
session.viewports['Viewport: 1'].view.setValues(nearPlane=596.05, 
    farPlane=1149.07, width=639.274, height=289.755, cameraPosition=(-69.1829, 
    -682.159, 188.59), cameraUpVector=(0.0387452, 0.488387, 0.871767), 
    cameraTarget=(139.438, 151.982, 45.3138))
session.viewports['Viewport: 1'].view.setValues(nearPlane=586.166, 
    farPlane=1157.21, width=628.673, height=284.95, cameraPosition=(-128.162, 
    -648.026, 264.927), cameraUpVector=(0.0997992, 0.556205, 0.825031), 
    cameraTarget=(139.379, 152.016, 45.39))
session.viewports['Viewport: 1'].view.setValues(nearPlane=588.101, 
    farPlane=1156.07, width=630.748, height=285.891, cameraPosition=(-144.028, 
    -661.125, 180.753), cameraUpVector=(0.00215469, 0.500683, 0.865628), 
    cameraTarget=(139.379, 152.016, 45.3901))
session.viewports['Viewport: 1'].view.setValues(nearPlane=594.388, 
    farPlane=1149.87, width=637.491, height=288.947, cameraPosition=(-63.5816, 
    -666.403, 266.399), cameraUpVector=(0.0780009, 0.558631, 0.82574), 
    cameraTarget=(139.416, 152.014, 45.4291))
