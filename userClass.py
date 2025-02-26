import requests
import json

class UserProfile:    
    
    username = ""
    games = []
    genreComp = {}

    # constructor
    def __init__(self):
        pass

    # __str__ -> str
    # human readable string interpretation of object
    def __str__(self):
        return self.username #TODO implement user readable format

    # __eq__ -> Boolean
    # comparison between self and other object value
    def __eq__(self, value):
        if type(self) != type (value):
            return False
        else:
            return (self.username == value.username and
                    self.games == value.games and
                    self.genreComp == value.genreComp
                )
    
    # __eq__ -> int
    # hash self object. must be implemented to implement __eq__
    def __hash__(self):
        return hash((self.username, self.games, self.genreComp))

    # importUserApps -> void
    # assign given userApps to self
    def importUserApps(self, listOfApps):
        self.games = listOfApps

    # getTopGenres -> tuple
    # returns the top three genres of the user
    def createGenreComposition(self):
        #TODO 
        pass
    
    # loadUserProfile -> void
    # loads known user profile into working memory
    def loadUserProfile(self):
        #TODO
        pass