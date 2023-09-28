import mil as MIL


def main():

    # Allocate defaults.
    MilApplication = MIL.MappAlloc("M_DEFAULT", MIL.M_DEFAULT)
    MilSystem = MIL.MsysAlloc(MIL.M_DEFAULT, MIL.M_SYSTEM_DEFAULT, MIL.M_DEFAULT, MIL.M_DEFAULT)

    # alloca two displays
    MilDisplay0 = MIL.MdispAlloc(MilSystem, MIL.M_DEFAULT, 'Display0', MIL.M_DEFAULT, MIL.M_NULL)
    MilDigitizer0 = MIL.MdigAlloc(MilSystem, MIL.M_DEFAULT, "M_DEFAULT", MIL.M_DEFAULT)
    MilImage0 = MIL.MbufAlloc2d(MilSystem, 
                                MIL.MdigInquire(MilDigitizer0, MIL.M_SIZE_X, MIL.M_NULL), 
                                MIL.MdigInquire(MilDigitizer0, MIL.M_SIZE_Y, MIL.M_NULL),
                                8, MIL.M_IMAGE + MIL.M_GRAB, MIL.M_NULL)

    # Grab continuously.
    MIL.MdigGrabContinuous(MilDigitizer0, MilImage0)

    # When a key is pressed, halt. 
    print("\nDIGITIZER ACQUISITION:")
    print("----------------------\n")
    print("Continuous image grab in progress.")
    print("Press <Enter> to stop.\n")
    MIL.MosGetch()

    # Stop continuous grab
    MIL.MdigHalt(MilDigitizer0)

    # Pause to show the result. 
    print("Continuous grab stopped.\n")
    print("Press <Enter> to do a single image grab.\n")
    MIL.MosGetch()

    # Monoshot grab. 
    MIL.MdigGrab(MilDigitizer0, MilImage0)

    # Pause to show the result. 
    print("Displaying the grabbed image.")
    print("Press <Enter> to end.\n")
    MIL.MosGetch()

    # Free defaults.
    MIL.MappFreeDefault(MilApplication, MilSystem, MilDisplay0, MilDigitizer0, MilImage0)

    return 0

if __name__ == "__main__":
   main()