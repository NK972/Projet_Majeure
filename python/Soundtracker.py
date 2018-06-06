import time

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.tracker = ALProxy( "ALTracker" )
        self.memory = ALProxy("ALMemory")
        try:
            self.soundLocation = ALProxy("ALSoundLocalization")
        except Exception as e:
            self.soundLocation = None
            self.logger.error(e)
        self.targetName = "Sound"
        self.distance = 0.0
        self.soundDistance = 0.5
        self.confidence = 0.0
        self.thresholdX = 0.0
        self.effector = "None"
        self.sensitivity = 0.7
        self.subscribeDone = False
        self.isRunning = False

    def onLoad(self):
        self.BIND_PYTHON(self.getName(), "setParameter")
        self.BIND_PYTHON(self.getName(), "onTargetLost")
        self.BIND_PYTHON(self.getName(), "onTargetReached")
        self.BIND_PYTHON(self.getName(), "onTargetChanged")
        if self.soundLocation:
            self.memory.subscribeToEvent("ALTracker/ActiveTargetChanged", self.getName(), "onTargetChanged")

    def onUnload(self):
        if self.subscribeDone:
            self.memory.unsubscribeToEvent("ALTracker/TargetLost", self.getName())
            self.memory.unsubscribeToEvent("ALTracker/TargetReached", self.getName())
            self.subscribeDone = False

        if self.isRunning:
            self.tracker.setEffector("None")
            self.tracker.stopTracker()
            self.tracker.unregisterTarget(self.targetName)
            self.isRunning = False

    def onInput_onStart(self):
        self.memory.subscribeToEvent("ALTracker/TargetLost", self.getName(), "onTargetLost")
        self.memory.subscribeToEvent("ALTracker/TargetReached", self.getName(), "onTargetReached")
        self.subscribeDone = False

        mode = self.getParameter("Mode")
        self.confidence = self.getParameter("Threshold to be sure of the location (%)") / 100.0
        self.distance = self.getParameter("Distance (m)")
        self.thresholdX = self.getParameter("Threshold X (m)")
        self.effector = self.getParameter("Effector")
        self.sensitivity = self.getParameter("Sensitivity")

        if self.soundLocation:
            self.soundLocation.setParameter("Sensitivity", self.sensitivity)

        self.tracker.setEffector(self.effector)

        self.tracker.registerTarget(self.targetName, [self.soundDistance, self.confidence])
        self.tracker.setRelativePosition([-self.distance, 0.0, 0.0,
                                            self.thresholdX, 0.1, 0.3])
        self.tracker.setMode(mode)

        self.tracker.track(self.targetName) #Start tracker
        self.isRunning = True

    def onInput_onStop(self):
        self.onStopped()
        self.onUnload()

    def setParameter(self, parameterName, newValue):
        GeneratedClass.setParameter(self, parameterName, newValue)
        if (parameterName == 'Mode'):
            self.tracker.setMode(newValue)
            return

        if (parameterName == "Threshold to be sure of the location (%)"):
            self.confidence = self.getParameter("Threshold to be sure of the location (%)") / 100.0
            self.tracker.registerTarget(self.targetName, [self.soundDistance, self.confidence])
            return

        if (parameterName == "Distance (m)"):
            self.distance = newValue
            self.tracker.setRelativePosition([-self.distance, 0.0, 0.0,
                                                self.thresholdX, 0.1, 0.3])
            return

        if (parameterName == "Threshold X (m)"):
            self.thresholdX = newValue
            self.tracker.setRelativePosition([-self.distance, 0.0, 0.0,
                                                self.thresholdX, 0.1, 0.3])
            return

        if(parameterName == "Effector"):
            self.tracker.setEffector(newValue)
            self.effector = newValue
            return

        if(parameterName == "Sensitivity"):
            self.sensitivity = newValue
            if self.soundLocation:
                self.soundLocation.setParameter("Sensitivity", self.sensitivity)
            return


    def onTargetLost(self, key, value, message):
        self.targetLost()

    def onTargetReached(self, key, value, message):
        self.targetReached()

    def onTargetChanged(self, key, value, message):
        if value == self.targetName and not self.subscribeDone:
            self.memory.subscribeToEvent("ALTracker/TargetLost", self.getName(), "onTargetLost")
            self.memory.subscribeToEvent("ALTracker/TargetReached", self.getName(), "onTargetReached")
            self.subscribeDone = True
        elif value != self.targetName and self.subscribeDone:
            self.memory.unsubscribeToEvent("ALTracker/TargetLost", self.getName())
            self.memory.unsubscribeToEvent("ALTracker/TargetReached", self.getName())
            self.subscribeDone = False
