from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene is not yet configured.  Subclass!"
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            # be sure to print out the last scene pls
            return current_scene.enter()

class Death(Scene):

    quips = [
      "Your friend got arrested and the others are mad."
      "You are the worst navigator ever. Sad!"
      "Congratulations, you walking WorldStar highlight reel."
      "You deserve to be dabbed on."
      "Gain skill and git gud."
        ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralClub(Scene):

    def enter(self):
        print "So, you decided to go to a birthday party"
        print "You, the antisocial one.  AND YOU ARE IN MIAMI"
        print "\n"
        print "As if this club full of walking memes"
        print "isn't enough, the birthday boy just got"
        print "lost and that would be fine IF YOU WERENT"
        print "in FREAKING SOUTH BEACH YOU DUMB TOURIST."
        print "Now that you have vented enough, it is now"
        print "time for you to get your friend back to the"
        print "hotel."
        print "\n"
        print "You're trying to remap the possible areas that your"
        print "ridiculous friend may be at. Knowing how hungry he"
        print "gets, and knowing that he would gamble on snail races,"
        print "he is most likely at Miami Subs, betting on the fights"
        print "outside while eating."
        print "\n"
        print "But since he leaves a wave of destruction in every place that"
        print "he goes, you need to check all of the clubs to be sure that he"
        print "didn't cause too much damage or sleep with a diplomat's wife"
        print "again, which is a story for another time, but not now."
        print "Now where could Captain Wingus be?????"
        print "Before you can even go look, some bad duudes want to fight you."
        print "This is most likely because earlier in the night.."
        print "You can either try to punch this person or dodge skilfully!"


        action = raw_input("> ")


        if action == "punch":
            print "This bad dude comes at you with an empty vodka bottle, and you"
            print "try to punch him in the nose. He is unmoved."
            print "You try to do a standing armbar. He is unmoved."
            print "He gets annoyed, puts the bottle down, and throws you from the balcony"
            print "floor to the first floor. Looking down on you,"
            print "he shakes his head and walks off."
            return 'death'


        elif action == "dodge":
            print "With your years of parry training from 3rd Strike, you bob, weave, and dodge like"
            print "a certain British boxer who has a love for horticulture.  The bottle misses and hits"
            print "Pitbull's bodyguard, because why not. Why not defy conventional logic and have this?"
            print "Anyways, apparently he doesn't take kindly to being hit by anything.  This dude looks"
            print "like he wrestles tanks and slapboxes bears.  Anyways, he picks up both of you"
            print "with one hand each, walks you outside, and throws you into a parked car, which happens"
            print "to belong to a mobster who looks like Zangief.  Suffice to say, they riverdance on both of you, hit the dab, and"
            print "walk back into the club."
            return 'death'

        elif action == "reasoning":
            print "You tell the menacing man that your friend went through a very bad breakup and he's"
            print "not dealing with this as well as you would think.  He compartmentalizes his behavior"
            print "and never truly confronts it.  He doesn't see wrong or right in this situation, but he"
            print "sees nothing but pain.  Moved by your description, he nods in understanding and lets you go."
            return 'MiamiSubs'

        else:
            print "bruh"
            return 'CentralClub'


class MiamiSubs(Scene):
    def enter(self):
        print "You have just arrived at the apex of Miami Beach"
        print "and you know that people are hungry and angry."
        print "Hence, your friend is here, if not being a nuisance."
        print "This place moonlights as an FGC hangout on weekdays"
        print "so he of course money-matched and lost a round of 10 games."
        print "Being as cheap as he is, he decided not to pay."
        print "Luckily, you make a wager with the people here that"
        print "if you successfully beat them with a particular damage count"
        print "the bets made by your dumb friend are voided. Guess wrong and"
        print "they get triple.  The amount of damage is three digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
          print "WRONG COUNT FAM"
          guesses += 1
          guess = raw_input("[keypad]> ")

        if guess == code:
            print "You are too good for this stuff.  You saved the day!"
            print "Also, your friend is happily passed out at a booth with"
            print "fries in hand.  Time to get this fool back home."
            return 'EscapeCar'

        else:
          print "Not only did you fail to make your prediction true, you"
          print "managed to pay triple. You need to git gud."
          return 'death'


class EscapeCar(Scene):
    def enter(self):
        print "We just escaped the wildest night in at least the past few weeks"
        print "and now it's time to go home before we bring more havoc and unwanted"
        print "guests to the hotel.  But the car isn't starting.  WHAT THE HECK"
        print "like THIS ISNT COOL TOASTY OR ANYTHING FUN YOU JUST FIXED THIS CRAP"
        print "Now that you had your YE moment, it's time to fix it YE style."

        action = raw_input("> ")

        if action == "punch the car":
            print "The power of Yeezy started the car."
            print "Sadly, it died about two blocks further down and"
            print "you got pulled over after Drunky called the cop a mark. Sad!"
            return 'finished'

        elif action == "apologize to the car":
            print "The car starts and keeps going to your destination. Glad!"
            return 'Beachstrip'
        else:
            print "bruh"
            return 'Escapecar'

class Finished(Scene):
    def enter(self):
        print "Finally, we go home with less money and ridiculous experiences."
        print "This was a wonderful time, wasn't it?"
        return 'finished'


class Map(object):

  scenes = {
    'CentralClub': CentralClub(),
    'MiamiSubs': MiamiSubs(),
    'EscapeCar': EscapeCar(),
    'Death': Death(),
    'Finished': Finished()
  }

  def __init__(self, start_scene):
      self.start_scene = start_scene


  def next_scene(self, scene_name):
      val = Map.scenes.get(scene_name)
      return val

  def opening_scene(self):
      return self.next_scene(self.start_scene)




a_map = Map('CentralClub')
a_game = Engine(a_map)
a_game.play()
