import matplotlib.pyplot as plt
from random_walk import RandomWalk

if __name__ == '__main__':
    while True:
        rw = RandomWalk(30_000)
        rw.fill_walk()

        fig, ax = plt.subplots(figsize=(15,9))

        ax.scatter(rw.x[0], rw.y[0], c='green',s=50)
        ax.scatter(rw.x[-1], rw.y[-1], c='red',s=50)
        ax.scatter(rw.x, rw.y, c=range(rw.num_points),
                   cmap=plt.cm.Blues, s=1)

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)


        plt.show()
        keep_running=input('continue? press n to quit: ')
        if keep_running=='n':
            break