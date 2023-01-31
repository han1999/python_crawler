import matplotlib.pyplot as plt

if __name__ == '__main__':
    squares = [value ** 2 for value in range(1, 11)]
    input_values= list(range(1,11))
    plt.rcParams["font.sans-serif"]=['SimHei'] # 不加会乱码
    # plt.style.use('seaborn')

    fig, ax = plt.subplots()
    ax.plot(input_values, squares, linewidth=3)

    ax.set_title('平方数', fontsize=24)
    ax.set_xlabel('值', fontsize=14)
    ax.set_ylabel('值的平方', fontsize=14)
    ax.tick_params(axis='both', labelsize=14)

    plt.show()
