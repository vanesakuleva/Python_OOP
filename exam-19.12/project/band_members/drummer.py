from project.band_members.musician import Musician


class Drummer(Musician):

    def __init__(self, name: str, age):
        super().__init__(name,age)
        self.skills_available =["play the drums with drumsticks","play the drums with drum brushes","read sheet music"]

    def learn_new_skill(self, new_skill: str):

        for skill in self.skills_available:
            if skill == new_skill:
                self.skills.append(new_skill)
                return f"{self.name} learned to {new_skill}."

        for skill in self.skills:
            if new_skill == skill:
                raise Exception(f"{new_skill} is already learned!")

        raise ValueError(f"{new_skill} is not a needed skill!")
