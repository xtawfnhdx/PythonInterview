import pyecharts

print(pyecharts.__version__)


def drawImage1():
    bar = pyecharts.charts.Bar()
    bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    bar.add_yaxis('商家A', [23, 45, 21, 67, 34])
    bar.add_yaxis('商家B', [54, 56, 43, 23, 76])
    return bar
    bar


def drawImage2():
    bar = (
        # 可以使用默认主题
        pyecharts.charts.Bar(init_opts=pyecharts.options.InitOpts(theme=pyecharts.globals.ThemeType.LIGHT))
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis('商家A', [23, 45, 21, 67, 34])
            .add_yaxis('商家B', [54, 56, 43, 23, 76])
            .set_global_opts(title_opts=pyecharts.options.TitleOpts(title='主标题', subtitle='副标题'))
    )
    return bar


if __name__ == '__main__':
    page = pyecharts.charts.Page()
    page.add(
        drawImage1(),
        drawImage2()
    )
    page.render('package_pyecharts.html')
