import os

class SessionStore:
    def __init__(self):
        #a dictionary of dictionaries, one per session
        self.sessions {}

    def createSession(self):
        #create a new session dictionary, add to self.sessions
        #assign new session to a new session ID
        sessionID = self.generateSessionID()
        self.sessions[sessionID] = {}
        return sessionID

    def generateSessionID(self):
        #return a new session ID that is:
        # 1. random
        # 2. unique
        # 3. unguessable
        rnum = os.urandom(32)
        rstr = base64.b64encode(rnum).decode("utf-8")
        return rstr


    def getSessionData(self,sessionID):
        #return the dictionary associated with the session ID,
        #if it exists
        if self.sessions[sessionID]:
            return self.sessions[sessionID]
        else:
            return None

"""
Psudocode Function Definition for loadSession:

def loadSession(self):
        #load the cookie data
        #check for existence of the session ID cookie
        if 'sessionID' = self.cookie: #if the session ID cookie exists:
            sessionID = self.cookie['sessionID'].value
            #load the session data for the session
            #if the session ID is not valid:
                #create a new session / sessionID
                #save the new sessionID into cookie
                self.cookie['sessionID']=sessionID
                #load the session data for the session
        #else:
            #create a new session / sessionID
            #save the new sessionID into cookie
            #load the session data for the session
"""