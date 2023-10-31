# class Chapomoto:
#     def __init__(self, unga, sugar):
#         self.unga  = unga
#         self.sugar = sugar
#
#
# p1 = Chapomoto(200, 10)
# print(p1.unga)
# print(p1.sugar)


# class Monster:
#     def __int__(self):
#         self.name = ""
#         self.number_of_teeth = 0
#         self.colour = ""
#
#     def is_scary(self):
#         return self.number_of_teeth > 16 or self.colour == "red"
#
#     def __eq__(self, other):
#         print("eq method:)")
#         return self.name == other.name
#
#     def __ne__(self, other):
#         print("ne method :(")
#         return self.name != other.name
#
#
# # p1 = Monster("Mike", 0, "blue")
# # print(p1.name)
#
#
# def run_tests():
#     m_1 = Monster()
#     m_1.name = "Mike"
#     m_1.number_of_teeth = 128
#     m_2 = Monster()
#     m_2.number_of_teeth = 1
#     m_3 = Monster()
#     m_3.name = "Mike"
#     print(m_1.is_scary(), "expected: True")
#     assert m_1.is_scary()
#     assert not m_2.is_scary()
#     assert m_1 != m_2
#     assert m_1 == m_3
#
#
# run_tests()

class TacoReward:
    def __init__(self, name):
        self.name = name
        self.number_of_tacos = 5
        self.score = 0

    def give_taco(self, other_user):
        self.number_of_tacos -= 1
        other_user.number_of_tacos += 1

    def __str__(self):
        return f"{self.name},{self.score} points,{self.number_of_tacos} tacos left"


user1 = TacoReward("Ben")
print(user1.name)
print(user1.number_of_tacos)
print(user1.score)

user2 = TacoReward("Alice")
user1.give_taco(user2)
print(user1)
print(user2)