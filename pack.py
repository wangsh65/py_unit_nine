from dog import Dog

class Pack:

    def __init__(self,leader):
        self.members = [leader]
        self. leader_index = 0

    def get_leader_name(self):
        return self.members[self.leader_index].get_name()


    def add_numbers(self,new_member):
        self.members.append(new_member)

    def print_pack(self):
        print("The pack contains:")
        for member in self.members:
            print(f"\t{member.get_name(dog1)}")

    def get_leader(self,new_leader_index):
        if 0 <= new_leader_index < len(self.members) and new_leader_index != self.leader_index:
            old_leader_name = self.get_leader_name()
            self.leader_index = new_leader_index
            new_leader_name = self.get_leader_name()
            print(new_leader_name + "Rover deposes",old_leader_name,"as the leader of the pack.")

        else:
            print( "That is not a valid dog." )

    def all_trick(self,trick_name):
        print(f"The pack performs the {trick_name} trick:")
        for member in self.members:
            member.trick(trick_name)

    def all_print_tricks(self,):
        print("Tricks performed by the pack members:")
        for member in self.members:
            print(f"{member.get_name()}: {', '.join(member.get_tricks())}")




dog1 = Dog("Fido")
dog2 = Dog("Spot")
dog3 = Dog("Rover")
pack = Pack(dog1)
pack.add_numbers(dog2)
pack.add_numbers(dog3)
leader_name = pack.get_leader_name()

print(f"The leader of the pack is {leader_name}.")

pack.get_leader(1)




