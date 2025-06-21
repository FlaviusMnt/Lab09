from dataclasses import dataclass


@dataclass
class Airport:
    ID : int
    IATA_CODE : str
    AIRPORT : str
    CITY : str
    STATE :str
    COUNTRY : str
    LATITUDE : float
    LONGITUDE : float
    TIMEZONE_OFFSET : float


    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, value):
        self._ID = value

    @property
    def IATA_CODE(self):
        return self._IATA_CODE

    @IATA_CODE.setter
    def IATA_CODE(self, value):
        self._IATA_CODE = value

    @property
    def AIRPORT(self):
        return self._AIRPORT

    @AIRPORT.setter
    def AIRPORT(self, value):
        self._AIRPORT = value

    @property
    def CITY(self):
        return self._CITY

    @CITY.setter
    def CITY(self, value):
        self._CITY = value

    @property
    def STATE(self):
        return self._STATE

    @STATE.setter
    def STATE(self, value):
        self._STATE = value

    @property
    def COUNTRY(self):
        return self._COUNTRY

    @COUNTRY.setter
    def COUNTRY(self, value):
        self._COUNTRY = value

    @property
    def LATITUDE(self):
        return self._LATITUDE

    @LATITUDE.setter
    def LATITUDE(self, value):
        self._LATITUDE = value

    @property
    def LONGITUDE(self):
        return self._LONGITUDE

    @LONGITUDE.setter
    def LONGITUDE(self, value):
        self._LONGITUDE = value

    @property
    def TIMEZONE_OFFSET(self):
        return self._TIMEZONE_OFFSET

    @TIMEZONE_OFFSET.setter
    def TIMEZONE_OFFSET(self, value):
        self._TIMEZONE_OFFSET = value

    def __eq__(self, other):
        return self.ID == other.ID

    def __hash__(self):
        return hash(self.ID)

    #Serve quando vuoi stampare l’oggetto in modo leggibile per un utente.
    def __str__(self):
        return f"{self.AIRPORT}"

    #__repr__(self): rappresentazione tecnica, per il debug
    #Serve a fornire una rappresentazione ufficiale, non ambigua.
    def __repr__(self):
        return self.AIRPORT

