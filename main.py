import time
import mil as MIL
import numpy as np

def main():

    # Allocate defaults.
    MilApplication = MIL.MappAlloc("M_DEFAULT", MIL.M_DEFAULT)
    MilSystem = MIL.MsysAlloc(MIL.M_DEFAULT, MIL.M_SYSTEM_DEFAULT, MIL.M_DEFAULT, MIL.M_DEFAULT)
    MilDisplay = MIL.MdispAlloc(MilSystem, MIL.M_DEFAULT, "M_DEFAULT", MIL.M_WINDOWED)
    MilDigitizer = MIL.MdigAlloc(MilSystem, MIL.M_DEFAULT, "M_DEFAULT", MIL.M_DEFAULT)
    MilContainerDisp = MIL.MbufAllocContainer(MilSystem, MIL.M_PROC + MIL.M_DISP + MIL.M_GRAB, MIL.M_DEFAULT)
    
    ###############################
    # Set sensor parameters
    ###############################

    # load default parameters
    MIL.MdigControlFeature(MilDigitizer, MIL.M_FEATURE_VALUE, "UserSetDefault", MIL.M_TYPE_STRING, "Default")
    MIL.MdigControlFeature(MilDigitizer, MIL.M_FEATURE_EXECUTE, "UserSetLoad", MIL.M_DEFAULT, MIL.M_NULL)

    MIL.MdigControlFeature(MilDigitizer, MIL.M_FEATURE_VALUE, "ExposureAuto", MIL.M_TYPE_STRING, "Off")
    MIL.MdigControlFeature(MilDigitizer, MIL.M_FEATURE_VALUE, "ExposureTime", MIL.M_TYPE_DOUBLE, np.array(2000.0))

    ##############

    # Allocate an image buffer.
    MilImage = MIL.MbufAllocColor(MilSystem, 3, 1024, 768, 8 + MIL.M_UNSIGNED, MIL.M_IMAGE + MIL.M_GRAB + MIL.M_DISP, MIL.M_NULL)
 
    # # Display the image buffer.
    # MIL.MdispSelect(MilDisplay, MilImage)

    for ind in range(10):

        # start acquisition
        MIL.MdigGrab(MilDigitizer, MilImage)
        MIL.MbufExport(str(ind) + '.png', MIL.M_PNG, MilImage)
    
        # sleep 1 sec
        time.sleep(1)

    return 0

if __name__ == "__main__":
   main()