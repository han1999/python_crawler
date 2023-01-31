from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

if __name__ == '__main__':

    die=Die()
    die2=Die(10)
    res=[]
    for roll_num in range(10000):
        dig=die.roll()+die2.roll()
        res.append(dig)
    # print(res)

    freq=[]
    for value in range(2, die.sides+die2.sides+1):
        freq.append(res.count(value))
    # print(freq)

    data=[Bar(x=list(range(2, die.sides+die2.sides+1)), y=freq)]
    layout=Layout(title='投两个骰子10000次(d6.d10)', xaxis={'title':'点数', 'dtick':1}, yaxis={'title':'次数'})
    offline.plot(figure_or_data={'data':data, 'layout':layout}, filename='d6_d10.html')


