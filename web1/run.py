import pandas as pd
from flask import Flask, render_template, redirect
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline,Map


app = Flask(__name__)

def read_csv(name):
    datas = []
    if name == 'Changes.csv':
        df = pd.read_csv(name, encoding='gbk')
    else:
        df = pd.read_csv(name, encoding='utf-8')
    df.fillna(0)
    for index, row in df.iterrows():
        datas.append(list(row))
    return datas
@app.route('/')
def index():
    datas1 = read_csv('hurun.csv')
    datas2 = read_csv('histogram.csv')
    datas3 = read_csv('Changes.csv')
    flag = 3
    return render_template('index.html', datas1=datas1, datas2=datas2, datas3=datas3)




# def make_his_bar():
#     df = pd.read_csv("histogram.csv", encoding='utf-8')
#
#     for index, row in df.iterrows():



def timeline_bar() -> Timeline:
    dff = pd.read_csv('Changes.csv', encoding='gbk')
    dl = list(dff['行业大类'].unique())
    time = list(dff['年份'].unique())
    x = dl
    tl = Timeline()
    for i in time:
        values = []
        dff1 = dff[dff.年份 == i]
        for d in dl:
            dff2 = dff1[dff1.行业大类 == d]
            values.append(sum(dff2['占比']))
        bar = (
            Bar()
            .add_xaxis(dl)
            .add_yaxis("占比数量", values)

            .set_global_opts(title_opts=opts.TitleOpts("中国{}行业大类分布".format(i)))
        )
        tl.add(bar, "{}年".format(i))
    return tl


def map_visualmap() -> Map:
    df = pd.read_csv(r"hurun.csv", encoding='utf-8')
    dff = df['地区'].value_counts()
    dffc = list(dff)
    # df["地区"].unique()
    dfff = list(dff.index)
    c = (
        Map()
        .add("分省胡润百富榜分布",
             [list(z) for z in zip(list(dfff),list(dffc))])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="分省胡润百富榜分布"),
            visualmap_opts=opts.VisualMapOpts(max_=50),
        )
    )
    return c



if __name__ == '__main__':
    app.run()