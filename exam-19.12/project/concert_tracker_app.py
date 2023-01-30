from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):

        if any(i.name == name for i in self.musicians):
            raise Exception(f"{name} is already a musician!")

        musician = None
        if musician_type == "Guitarist":
            musician = Guitarist(name, age)
        elif musician_type == "Drummer":
            musician = Drummer(name, age)
        elif musician_type == "Singer":
            musician = Singer(name, age)
        elif musician_type != "Singer" or musician_type != "Drummer" or musician_type != "Guitarist":
            return "Invalid musician type!"

        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if any(i.name == name for i in self.bands):
            raise Exception(f"{name} is already a musician!")
        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if any(i.name == place for i in self.concerts):
            raise Exception(f"{place} is already registered for {genre} concert!")
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)

    def find_musician_by_name(self,musician_name):
        for name in self.musicians:
            if name.name == musician_name:
                return name
        return None

    def find_band_by_name(self, band_name):
        for name in self.bands:
            if name.name == band_name:
                return name
        return None

    def add_musician_to_band(self, musician_name: str, band_name: str):

        musician= self.find_musician_by_name(musician_name)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self.find_band_by_name(band_name)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.find_band_by_name(band_name)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        musician= self.find_musician_by_name(musician_name)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."



    def start_concert(self, concert_place: str, band_name: str):
        band = self.find_band_by_name(band_name)









