class Track:
    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.list = []

    def add_track(self, tr):
        self.list.append(tr)

    def get_tracks(self):
        return tuple(self.list)

    def __len__(self):
        x, y, dist = self.start_x, self.start_y, 0
        for obj in self.list:
            dist += ((((obj.to_x - x) ** 2) + ((obj.to_y - y) ** 2)) ** 0.5)
            x, y = obj.to_x, obj.to_y
        return int(dist)

    def __eq__(self, other):
        return len(self) == len(other)

    def __gt__(self, other):
        return len(self) > len(other)

class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed

track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2




print(len(track1))
print(len(track2))

print(track1 == track2)  # маршруты равны, если равны их длины
print(track1 != track2)  # маршруты не равны, если не равны их длины
print(track1 > track2)  # True, если длина пути для track1 больше, чем для track2
print(track1 < track2)  # True, если длина пути для track1 меньше, чем для track2