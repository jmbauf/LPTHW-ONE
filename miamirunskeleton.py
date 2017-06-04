class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralClub(Scene):

    def enter(self):
        pass

class VIP(Scene):

    def enter(self):
        pass

class MiamiSubs(Scene):

    def enter(self):
        pass

class EscapeCar(Scene):

    def enter(self):
        pass


class Beachstrip(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map =Beachstrip('CentralClub')
a_game = Engine(a_map)
a_game.play()
