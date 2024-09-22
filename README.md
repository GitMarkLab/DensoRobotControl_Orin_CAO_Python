# DensoRobotControl_Orin_CAO_Python
There are several ways to control a denso robot.
If you want to control it via python there are two possibilities based on ORIN2
- CAO Engine (only on Windows, compatible to older controller firmware >= 2.8)
    https://support.densorobotics.com/support/solutions/articles/60000698635-orin-2-programming-in-python-2-7-3-cao-engine-
    After ORIN installation in C:\ORiN2\CAO\Samples
- p-cap (only in c available for RC7 controllers)
- p-cap Links
-   https://github.com/ShoheiKobata/orin_bcap_python_samples/tree/master
-   https://github.com/DENSORobot/orin_bcap/tree/master

This repo provide examples based on the CAO. There is no full documentation available for certain commands. so i looked at comparable protocols to find the right commands. To make it easier for others, I have collate them here

My robot setup is the following:
- controller RC7M-HMG4BA-BP (FW 2.5)
- robot HM-40A02G



![Screenshot from 2024-08-18 17-55-15](https://github.com/user-attachments/assets/95aa11a2-d964-42fd-9590-7cd02b1fe5c4)

I would be very happy to know if you use the lib and what you do with it!
just write to me!
