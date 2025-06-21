class PointsForPlace:
    points = 0

    @staticmethod
    def get_points_for_place(place:int):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return PointsForPlace.points
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return PointsForPlace.points
        else: 
            PointsForPlace.points = 101 - place
            return PointsForPlace.points


class PointsForMeters():
    points = 0

    @staticmethod
    def get_points_for_meters(meters:int):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return PointsForMeters.points
        else:
            PointsForMeters.points = meters * 0.5
            return PointsForMeters.points
        

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        super().__init__()

    def get_total_points(self, meters, place):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))