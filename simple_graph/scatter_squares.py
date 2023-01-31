import matplotlib.pyplot as plt
if __name__ == '__main__':
    x=list(range(1,101))
    y=[v**2 for v in range(1,101)]

    plt.rcParams["font.sans-serif"] = ['SimHei']  # 不加会乱码
    fig, ax=plt.subplots()

    ax.scatter(x,y,c=y, cmap=plt.cm.Blues)

    ax.set_title('平方数')
    ax.set_xlabel('数')
    ax.set_ylabel('平方')
    # ax.tick_params(axis='both')
    plt.show()
