class Raspberry:
    #constructor
    def __init__(self,identifiant,gps,volume=None,state=None):
        self.identifiant = identifiant
        self.gps = gps
        if volume is None:
            self.volume = 10
        else:
            self.volume = volume
        if state is None:
            self.state = 0
        else:
            self.state = state

    #Method : getGPS
    #Goal   : obtain gps information
    def getGPS(self):
        return self.gps

    #Method : getId
    #Goal   : obtain id information
    def getId(self):
        return self.identifiant


    #Method : volumeUp
    #Goal   : switch up the volume
    def volumeUp(self):
        if self.volume < 20:
            self.volume +=1
            return 1
        return 0


    #Method : volumeDown
    #Goal   : switch down the volume
    def volumeDown(self):
        if self.volume > 1:
            self.volume -=1
            return 1
        return 0


    #Method      : changeMusicTo
    #Goal        : Change the music
    #Parameter 1 : The music to play
    def changeMusicTo(self,nameMusic):
        self.music = nameMusic

    #Method : play
    #Goal   : switch music to play
    def play(self):
        self.state = 1

    #Method : pause
    #Goal   : switch music to pause
    def pause(self):
        self.state = 0

    def serialize(self):
        ob = dict()
        ob["id"]     = self.identifiant
        ob["gps"]    = self.gps
        ob["volume"] = self.volume
        ob["music"]  = self.state
