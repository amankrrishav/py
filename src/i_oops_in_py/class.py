class emp :
    company = "Ark"

    def get_sal(self): #self is referenced to object itself
        return 35000

akr = emp() #object
print(akr.get_sal())
