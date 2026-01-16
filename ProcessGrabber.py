import wmi, random

class ProcessGrabber:    
    def __init__(self):
        self.operatingSystem = wmi.WMI()
        self.processes = [(proc.ProcessId, proc.Name) for proc in self.operatingSystem.Win32_Process()]
        random.shuffle(self.processes)
        
    def terminateProcess(self, procID: int):
        self.operatingSystem.Win32_Process(ProcessId=procID).Terminate()