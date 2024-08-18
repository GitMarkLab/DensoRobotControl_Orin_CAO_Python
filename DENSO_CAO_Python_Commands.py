from time import sleep
import win32com.client
import time

eng = win32com.client.Dispatch("CAO.CaoEngine")
# methods = dir(eng)
# print(methods)

ctrl = eng.Workspaces(0).AddController("RC1", "CaoProv.DENSO.RC.X", "", "Server=192.168.0.1")
# methods = dir(ctrl)
# print(methods)


# --- Variable handling ---
I11 = ctrl.AddVariable("I11", "")
print(I11)
I11.Value = 11
print I11.Value

_P5 = ctrl.AddVariable("P5", "")
print(_P5)
_P5.Value = [1,2,3,4,5,1,1] # X 414.5373 , Y -30.7000, Z 305.9200, T -60.31251, RL Lefty ,Fig 1 
print (_P5.Value)


# --- Init Robot ---
Arm1 = ctrl.AddRobot("Arm1", "")

# For older controllers it is needed to start the RobSlave file on the controller
# see also RobMaster.exe with this tool you can download the files to the controller and execute them manually
task1 = ctrl.AddTask("RobSlave", "")
task1.start(1) 

Arm1.Execute("TakeArm", 0)
Arm1.Execute("Motor", [1,0]) #Motor an

# Set/GET MINI IO port
IO_25 = ctrl.AddVariable("IO25", "")
IO_25.Value = 1 # Set HIGH
IO_25.Value = 0 # Set LOW

current_position = Arm1.AddVariable("@Current_Position","")
print(current_position) #(680.2056884765625, -161.53814697265625, 308.7040710449219, 0.0, 0.0, 33.91001510620117, 1.0)



# --- Robot Movement ---
# bcap analogy
# https://github.com/ShoheiKobata/orin_bcap_python_samples/blob/master/SimpleSamples/04_00_Move.py
# Arm1.Move(1, "@P P1", "NEXT")
# File <COMObject AddRobot>:2, in Move(self, lComp, vntPose, bstrOpt)

# Set Parameters
# Interpolation
# --->Comp = 1
# PoseData (string)
#----> Pose = "@P P1"
# m_bcapclient.robot_move(HRobot, Comp, Pose, "SPEED=F2,NEXT")

Arm1.Move(1, "@P P1", "NEXT")
Arm1.Move(1, "@P P1", "SPEED=80,NEXT") #kombination
Arm1.Move(1, "@P P2", "")

# X 414.5373 , Y -30.7000, Z 305.9200, T -60.31251, RL Lefty ,Fig 1
Arm1.Move(1, "@P P(414.0000, -30.0000, 305.0000, -60.00000, 1,1 )", "SPEED=80")

Arm1.Execute("Approach", [1, "P1", "@P 6"]) 

Arm1.Execute("ExtSpeed", [3,10,10]) #Param = [Speed, Accel, Decel]

Arm1.Execute("GiveArm", )
Arm1.Execute("Motor", [0,0]) #Motor aus
task1.stop()


# --- CAO specific ---
# How to look deeper into methods of the CAO Lib
# In general "CAO.CaoEngine" is included into registry under "Computer\HKEY_CLASSES_ROOT\Cao..."
# help("CAO.CaoEngine")

# methods = dir(eng)
# print(methods)

# methods = dir(ctrl)
# print(methods)
