# class Monitor:
#     def __init__(self, model="", width=0, height=0):
#         self.model = model
#         self.width = width
#         self.height = height
#
#     def __add__(self, width, height):
#         """Add monitor width to height"""
#         return self.width + self.height
#     def get_total_pixels(self):
#         return self.width * self.height
#
#     def get_resolution(self):
#         """Return Monitor Resolution"""
#         return (self.width, self.height)
#
#
# Monitor1 = Monitor("Dell", 24, 10)
# resolution = Monitor1.get_resolution()
# print(Monitor1.width + Monitor1.height)
# print(resolution)

# 2 TACO REWARD PROGRAM

from prac_06.Demo import User


class Team:
    def __int__(self, Users=[]):
        self.Users = Users

    def __add__(self, user):
        return self.Users + user

    def get_leader(self, Users):
        return Users[-1]

    def get_total_tacos_to_give(self):
        return self.number_of_tacos

    def get_total_score(self, score):
        return User(score)


t1 = Team(['Patrick', "Will", "Make it"])

print(t1.get_total_score())
print(t1.get_leader())
