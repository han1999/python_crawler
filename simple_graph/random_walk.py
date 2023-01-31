from random import choice
class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points=num_points
        self.x=[0]
        self.y=[0]

    def fill_walk(self):
        while len(self.x)<self.num_points:
            x_dir=choice([1,-1])
            x_dis=choice([1,2,3,4,5])
            x_step=x_dir*x_dis

            y_dir=choice([1,-1])
            y_dis=choice([1,2,3,4,5])
            y_step=y_dir*y_dis

            if x_step==0 and y_step==0:
                continue

            self.x.append(self.x[-1]+x_step)
            self.y.append(self.y[-1]+y_step)
