class Practice:
    #class Game
    def __ini__(self, username, password, server, playing = False):
        self.username = username
        self.password = password
        self.playing = playing
        self.server = server
    
    @property
    def username(self):
        self.username = self._username
        return self._username
    
    @username.setter
    def username(self):
        self._username = "2"
    

    
    