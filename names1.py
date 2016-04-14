class Monster:
    def __init__(self, **kwargs):
        self.hit_points = kwargs.get('hit_points', 10)
