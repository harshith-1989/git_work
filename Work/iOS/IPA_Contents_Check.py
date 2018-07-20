unzip the ipa to the iOS output folder --------- helper function, called main
Checks:
    info.plist checks:
        nsapptransport security & make sure exceptions are added
        URL schemes
    plist checks:
        get list of the plist files
        check contents of the plists for possible harcoded data
    class dump of executable:
        check if ipa in swift or objective c
        use the appropriate tool for class dumping
        check for methods like jailbroken / buy stuff etc
        check for strings
    otool check:
        check for libraries used
        architecture
    gdb check:
        check if process can be attached



###### refer ray wnderlich https://www.raywenderlich.com/45645/ios-app-security-analysis-part-1