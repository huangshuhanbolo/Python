# Python期末项目技术文档描述
姓名：黄舒涵 <br>
学号：181013125

## URL链接
Github代码URL展示链接：https://github.com/huangshuhanbolo/Python/tree/master/web1  <br>
pythonanywhere的URL展示链接：http://Sharkpineapple.pythonanywhere.com

---

#### 1.HTML档描述
   * HTML文件放置在templates文件夹中。
   * static文件夹中添加了少量css样式，使用<table>标签实现数据的呈现，再改变了字体样式，使得页面美观性更高。
   * 点开链接的首页是一项集“分省百富排行榜”、“各年各行业占比”、“分省各行业占比”的合成总表格。
   * 首页的左上角有一个下拉框选择器有“查看图表”“分省百富排行榜”、“各年各行业占比”、“分省各行业占比”四个选项，点击其中一个选项并且点击下拉框选择器的下方的“Do it”即可跳转到其他三个图表页面。

---

#### 2.Python档描述
   * 由run.py文件进行文件运行的最终结果。
   * 利用flask框架完成Python的web开发，实现前后端的交互，安装并导入pandas、pyecharts等模块，实现数据可视化，展示三个图表。
   * Flask框架中运用@app.route('/')，在Python语法中运用if、else。
   * 能实现python文档与html文档的数据交互。
   
   ***
   
#### 3.webapp档描述
* 主页面的左上方有一个下拉框选择器，选择不同的选项然后点击下拉框右边的“Do it”即可跳转到三个有图表的页面。
* 有图表的页面用户可使用鼠标滚动实现图表的放大缩小，也可用鼠标点击图表实现数据跳转。
