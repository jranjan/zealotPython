class Metric:
    def __init__(self, name, produced_at, data=dict()):
        self.name = name
        self.produced_at = produced_at
        self.info = data

    def get(self):
        return self.data
