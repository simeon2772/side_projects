from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ("Guitarist", "Drummer", "Singer"):
            raise ValueError("Invalid musician type!")
        for musician in self.musicians:
            if name == musician.name:
                raise Exception(f"{name} is already a musician!")
        m = None
        if musician_type == "Singer":
            m = Singer(name, age)
        elif musician_type == "Guitarist":
            m = Guitarist(name, age)
        elif musician_type == "Drummer":
            m = Drummer(name, age)
        self.musicians.append(m)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band_name = [b.name for b in self.bands]
        if band_name in self.bands:
            raise Exception(f"{name} band is already created!")
        b = Band(name)
        self.bands.append(b)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert_place = [c.place for c in self.concerts]
        concert_genre = [c.genre for c in self.concerts]
        if place == concert_place:
            raise Exception(f"{concert_place} is already registered for {concert_genre} concert!")
        c = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(c)
        return f"{genre} concert in {place} was added."

    def check_if_musician_valid(self, name):
        for musician in self.musicians:
            if musician.name == name:
                return musician
        else:
            raise Exception(f"{name} isn't a musician!")

    def check_if_band_valid(self, name):
        for band in self.bands:
            if band.name == name:
                return band
            raise Exception(f"{name} isn't a band!")

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.check_if_musician_valid(musician_name)
        band = self.check_if_band_valid(band_name)
        band.add_member(musician)
        return f"{musician_name} was added to {band_name}."

    @staticmethod
    def check_if_musician_in_band(band, name):
        for musician in band.members:
            if musician.name == name:
                return musician
        else:
            raise Exception(f"{name} isn't a member of {band}!")

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.check_if_band_valid(band_name)
        musician = self.check_if_musician_in_band(band, musician_name)
        band.remove_member(musician)
        return f"{musician_name} was removed from {band_name}."

    @staticmethod
    def check_if_enough_members_in_band(band, name):
        for members in band.members:
            if not isinstance(members, (Singer, Drummer, Guitarist)):
                raise Exception(f"{name} can't start the concert because it doesn't have enough members!")

    def locate_place(self, place_name):
        for concert in self.concerts:
            if concert.place == place_name:
                return concert

    def start_concert(self, concert_place: str, band_name: str):
        band = self.check_if_band_valid(band_name)
        concert = self.locate_place(concert_place)

        for musician_type in ["Drummer", "Singer", "Guitarist"]:
            if not any(
                    filter(
                        lambda x: x.__class__.__name__ == musician_type,
                        band.members
                    )
            ):
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and \
                        "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing high pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play rock" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Metal':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play metal" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Jazz':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' \
                        and "play the drums with drum brushes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' \
                        and ("sing low pitch notes" not in band_member.skills
                             or "sing high pitch notes" not in band_member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play jazz" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."


musician_types = ["Singer", "Drummer", "Guitarist"]
names = ["George", "Alex", "Lilly"]

app = ConcertTrackerApp()

for i in range(3):
    print(app.create_musician(musician_types[i], names[i], 20))

print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[2].learn_new_skill("play rock"))

print(app.create_band("RockName"))
for i in range(3):
    print(app.add_musician_to_band(names[i], "RockName"))

print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))

print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", "RockName"))