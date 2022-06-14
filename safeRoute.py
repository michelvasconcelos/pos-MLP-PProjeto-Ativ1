from routes import IRoute

class SafeRoute(IRoute):
    def __init__(self):
        self.risk = 'safe'
        self.distance = 'medium distance'

    def path(self):
        print(f'You took the {self.distance} route but got home {self.risk}! :-)')

#SafeRoute().path()