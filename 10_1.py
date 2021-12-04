#Ryan Okimoto Assignment 10.1

#imports the random module
import random

#creates the Champion class
class Champion:
    champ_type = ""
    def __init__(self, champ_name = "", ad = 0, ap = 0):
        self.champ_name = champ_name
        self.ad = float(ad)
        self.ap = float(ap)
    def get_champ_name(self):
        return self.champ_name
    def get_ad(self):
        return str(self.ad)
    def get_ap(self):
        return str(self.ap)
    def set_champ_name(self, new_name):
        self.champ_name = new_name
    def set_ad(self, new_ad):
        self.ad = new_ad
    def set_ap(self, new_ap):
        self.ap = new_ap
    def get_stats(self):
        print(self.champ_name + " ad:" + str(self.ad) + " ap:" + str(self.ap))
    def add_ad(self, more_ad):
        self.ad += float(more_ad)
    def add_ap(self, more_ap):
        self.ap += float(more_ap)
    def brawn_over_brain(self):
        self.ad += self.ap
        self.ap = 0
    def brain_over_brawn(self):
        self.ap += self.ad
        self.ad = 0
    def weaken(self):
        ad_or_ap = random.randint(0,1)
        if ad_or_ap == 0:
            self.ad -= random.randint(0,self.ad)
        else:
            self.ap -= random.randint(0,self.ap)
        

def main():
    champ_name = input("Input a champion name: ")
    ad = input("Input the physical damage of the champion: ")
    ap = input("Input the magic damage of the champion: ")
    myChamp = Champion(champ_name, ad, ap)
    myChamp.champ_type = input("Input your type of champion Ex: Melee, Mage, Ranged: ")
    while True:
        command = input("Input one of the following commands\nname, ad, ap, setname, setad, setap, addad, addap, stats, brawn_over_brain, brain_over_brawn, weaken, exit: ")
        if command == "name":
            print(myChamp.get_champ_name())
        if command == "ad":
            print(myChamp.get_ad())
        if command == "ap":
            print(myChamp.get_ap())
        if command == "setname":
            new_name = input("Input a new champion name: ")
            myChamp.set_champ_name(new_name)
        if command == "setad":
            new_ad = input("Input your champion's physical damage: ")
            myChamp.set_ad(new_ad)
        if command == "setap":
            new_ap = input("Input your champion's magical damage: ")
            myChamp.set_ad(new_ap)
        if command == "addad":
            new_ad = input("Input the increase in physical damage: ")
            myChamp.add_ad(new_ad)
        if command == "addap":
            new_ap = input("Input the increase in magical damage: ")
            myChamp.add_ad(new_ap)
        if command == "stats":
            myChamp.get_stats()
            print(myChamp.champ_type)
        if command == "brawn_over_brain":
            myChamp.brawn_over_brain()
        if command == "brain_over_brawn":
            myChamp.brain_over_brawn()
        if command == "weaken":
            myChamp.weaken()
        if command == "exit":
            print("Goodbye")
            exit()   
if __name__ == "__main__":
    main()
        