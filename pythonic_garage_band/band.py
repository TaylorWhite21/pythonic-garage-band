class Band:
    list_of_bands = []
    
    # Creates the band name and members that were given, then adds the band name to list of bands array
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.list_of_bands.append(self.name)

    # Returns user facing string
    def __str__(self):
        return f"The band {self.name}"
    
    # Returns string that only dev can see
    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"
    
    # Creates an array, then for each member in the array that matches the instrument, append their solo to the array
    def play_solos(self):
        solos = []
        for i in range(len(self.members)):
            if self.members[i].instrument == "guitar":
                solos.append(self.members[i].solo)
            elif self.members[i].instrument == "bass":
                solos.append(self.members[i].solo)
            elif self.members[i].instrument == "drums":
                solos.append(self.members[i].solo)
        return solos
            
    # Return the list of band members
    @classmethod
    def to_list(cls):
        return cls.list_of_bands
    # This test only passes if it runs by itself.
    # I spoke with TA Brandon and they said that it's ok
        
        


class Musician(Band):
    def __init__():
        return "I don't know how I made this work without using musician"
    

class Guitarist(Musician):
    
    # Initializes all needed data for a guitarist
    def __init__(self, name="A guitarist", instrument="guitar"):
        self.name = name
        self.instrument = instrument
        self.solo = 'face melting guitar solo'
        
    # Returns string that only dev can see
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    
    # Returns user facing string
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
    # Returns the intrument that is used.
    def get_instrument(self):
        return self.instrument
    
    # Returns solo
    def play_solo(cls):
        return cls.solo

class Bassist(Musician):
    
    def __init__(self, name="A bassist", instrument="bass"):
        self.name = name
        self.instrument = instrument
        self.solo = 'bom bom buh bom'
        
    # Returns user facing string
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    
    # Returns string that only dev can see
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    
    # Returns the intrument that is used.
    def get_instrument(self):
        return "bass"
    
    # Returns solo
    def play_solo(cls):
        return cls.solo
    

class Drummer(Musician):
    def __init__(self, name="A bassist", instrument="drums"):
        self.name = name
        self.instrument = instrument
        self.solo = "rattle boom crash"
    
    # Returns user facing string
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    
    # Returns string that only dev can see
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    
    # Returns the intrument that is used.
    def get_instrument(self):
        return "drums"

    # Returns solo
    def play_solo(cls):
        return cls.solo
