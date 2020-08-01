# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import streamlit as st

with st.echo():
    st.title('My first test case for streamlit')

# 上下文管理代码展示
with st.echo():
    # Markdown效果
    st.markdown("# Hello")
    st.markdown("## 第一个")
    st.markdown("## 第二个")
    st.markdown("### 第2.1个")
    st.markdown("### 第2.3个")
    st.markdown("+ hhh")


# 数学公式也有专门的语法支持

def name():
    """
    名称说明
    Returns:

    """


st.markdown("## 万能Write方法展示")
with st.echo():
    # 万能的Write方法
    # Magic Commands    Any Type will be ok
    st.write("Here's our first attempt at using data to create a table:")
    # 1.DataFrame to Table
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))
    # 2.优雅打印异常(异常对象)
    st.write(Exception("出错啦"))

    # 3.打印函数内部的详细说明(函数变量)
    st.write(name)

    # 4.优雅打印json字符串
    st.write({"name": "nb", "sex": "female", "age": 15})
    st.write([1, 2, 3])

    # 5.打印对象:默认打印对象内部的__str__方法
    # 6.Keras 的model打印.  graphviz图打印等可视化呈现方式

st.markdown("## 媒体信息展示")
with st.echo():
    # 图片展示,可以展示多张图片,附加说明文字,调整宽度,可以输入url,二进制流,ndarray等信息展示图片
    st.image("aaa.png", caption="决策树", use_column_width=True)

with st.echo():
    # 音频信息展示,可以调整播放时间
    st.audio("钢琴.ogg")

with st.echo():
    # 视频信息展示
    st.video("视频.mp4")

st.markdown("## 交互组件:优雅采集用户输入信息")
with st.echo():
    # 按钮,点击后触发对应的操作
    if st.button('Say hello'):
        st.write("Say hello")
    else:
        st.write("Goodbye")

with st.echo():
    # checkbox:仅仅点击了按钮才会触发if 内部内容的执行:但是程序会重新执行并且刷新一遍
    if st.checkbox('Show dataframe'):
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])

        st.line_chart(chart_data)

with st.echo():
    # radio,会重复执行应用
    genre = st.radio(
        "最喜欢哪个?",
        ["fish", "meat", "milk"]
    )
    if genre == "fish":
        st.write("In The Sea")
    elif genre == "milk":
        st.write("Cow")
    elif genre == "meat":
        st.write("Pork")

with st.echo():
    # selectbox,会重复执行应用
    option = st.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone'))
    st.write('You selected:', option)

with st.echo():
    # multiselect
    options = st.multiselect(
        'What are your favorite colors',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])
    st.write('You selected:', options)

with st.echo():
    # Slider:数值(整数,小数类型数据),时间(datetime类型数据),每次移动的跨度可以指定
    age = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", age, 'years old')

with st.echo():
    # 时间类型
    from datetime import datetime

    start_time = st.slider(
        "When do you start?",
        value=datetime(2020, 1, 1, 9, 30),
        format="MM/DD/YY - hh:mm")
    st.write("Start time:", start_time)

with st.echo():
    # 文本输入,最大字符长度限制,password信息
    title = st.text_input('Movie title', 'Life of Brian')
    st.write('The current movie title is', title)

with st.echo():
    # 数值输入,最大最小值,默认值,step
    number = st.number_input('Insert a number')
    st.write('The current number is ', number)

with st.echo():
    # text_area:长文本输入
    txt = st.text_area("Text To Analyze")
    st.write(txt)

with st.echo():
    # 日期输入,日历展示
    d = st.date_input(
        "When's your birthday",
        datetime(2019, 7, 6))
    st.write('Your birthday is:', d)

with st.echo():
    # 时间类型输入
    from datetime import time

    t = st.time_input('Set an alarm for', time(8, 45, 45))
    st.write('Alarm is set for', t)

with st.echo():
    # 文件上传,返回二进制文件,可以限制文件上传
    st.set_option('deprecation.showfileUploaderEncoding', False)
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv", encoding="utf8")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)

st.markdown("## 导航栏支持所有交互组件,相当于一块新的空间,不支持write")
with st.echo():
    # Slide Bar 导航栏,支持所有上述组件
    new = st.sidebar.selectbox(
        'Chose',
        [1, 2, 3, 4, 5])
    st.write(new)

st.markdown("## 展示状态的组件")
with st.echo():
    # 进度条展示
    my_bar = st.progress(0)
    # for percent_complete in range(100):
    #     time.sleep(0.1)
    #     my_bar.progress(percent_complete + 1)

with st.echo():
    # 执行某段代码的时候临时展示对应的消息,等代码执行完成后消失

    with st.spinner('Wait for it...'):
        import time

        time.sleep(0.1)
    st.success('Done!')
    st.balloons()

with st.echo():
    # 各种信息提示
    st.error('This is an error')
    st.warning('This is a warning')
    st.info('This is a purely informational message')
    st.success('This is a success message!')
    e = RuntimeError('This is an exception of type RuntimeError')
    st.exception(e)

with st.echo():
    # 占位符的意义:在页面上先占领一块地方,然后通过事件的方式进行填充内容
    # 使用方式,可以动态展示文字,图片
    my_placeholder = st.empty()
    if st.button('Say hello1'):
        # Now replace the placeholder with some text:
        my_placeholder.text("Hello world!")

    # And replace the text with an image:
    # my_placeholder.image("aaa.png")

with st.echo():
    # modify the data within an existing element (chart, table, dataframe).
    # >> > df1 = pd.DataFrame(
    #     ...
    # np.random.randn(50, 20),
    # ...
    # columns = ('col %d' % i for i in range(20)))
    # ...
    # >> > my_table = st.table(df1)
    # >> >
    # >> > df2 = pd.DataFrame(
    #     ...
    # np.random.randn(50, 20),
    # ...
    # columns = ('col %d' % i for i in range(20)))
    # ...
    # >> > my_table.add_rows(df2)
    # >> >  # Now the table shown in the Streamlit app contains the data for
    # >> >  # df1 followed by the data for df2.
    pass

st.markdown("## 方法缓存")
with st.echo():
    # 重点1:缓存装饰器进行函数级别的缓存操作,
    # 浏览器会提示需要缓存的内容:可以设置参数:suppress_st_warning去除提醒

    def inner_func(a, b):
        st.write("inner_func(", a, ",", b, ") ran")
        return a ** b  # 👈 Changed the * to ** here


    @st.cache(persist=True)  # 👈 Added this   # 根据:1.入参 2.函数体(递归寻找内置函数体) 进行hash加密判断唯一性
    # 唯一hash值一直存在内存中
    def expensive_computation(a, b):
        inner_func(a, b)  # 重点4:即使内置的函数体发生了变化,缓存也会失效
        time.sleep(1)  # 👈 This makes the function take 2s to run
        return a * b  # 重点3:如果函数的body变化了缓存也会失效


    a = 2
    # 重点5 : 21==>22 然后再变回21   参数21 的缓存仍然存在
    b = 21  # 重点2:如果输入函数的参数变化了 streamlit 会自动监控到变化,函数缓存失效

    res = expensive_computation(a, b)
    st.write(res)


    @st.cache(suppress_st_warning=True, allow_output_mutation=True)
    def expensive_computation(a, b):
        st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
        time.sleep(2)  # This makes the function take 2s to run
        return {"output": a * b}  # 👈 Mutable object
        # #重点6:如果返回可变数据类型,在函数方法外部又改变了可变类型的值,会抛异常,可以在外部使用deepcopy解决此类问题


    a = 2
    b = 21
    res = expensive_computation(a, b)  # 可以在此处使用deepcopy来改进此类缓存问题
    st.write("Result:", res)
    # res["output"] = "result was manually mutated"  # 👈 Mutated cached value
    st.write("Mutated result:", res)


    # 重点7:缓存进阶:自定制hash缓存方法
    class FileReference:
        def __init__(self, filename):
            self.filename = filename

        def read(self):
            with open(self.filename, "r", encoding="utf8") as f:
                return f.read()


    def hash_file_reference(file_reference):  # 返回的内容就是需要hash的内容
        import os
        filename = file_reference.filename
        return (filename, os.path.getmtime(filename))  # 对文件以及修改时间进行联合缓存


    @st.cache(hash_funcs={FileReference: hash_file_reference}, persist=True)
    def func(
            file_reference):  # file_reference 就是 FileReference 类的实例化对象   hash_file_reference 是对应的hash算法,可以直接使用python内部的hash算法
        import time
        time.sleep(1)
        return file_reference.read()[0:10]


    st.write(func(FileReference("机器学习图书.csv")))


with st.echo():
    # Html 以及 iframe展示
    import streamlit.components.v1 as components
    components.iframe("https://docs.streamlit.io/en/latest")
    components.html(
        """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <div id="accordion">
          <div class="card">
            <div class="card-header" id="headingOne">
              <h5 class="mb-0">
                <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                Collapsible Group Item #1
                </button>
              </h5>
            </div>
            <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
              <div class="card-body">
                Collapsible Group Item #1 content
              </div>
            </div>
          </div>
          <div class="card">
            <div class="card-header" id="headingTwo">
              <h5 class="mb-0">
                <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                Collapsible Group Item #2
                </button>
              </h5>
            </div>
            <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
              <div class="card-body">
                Collapsible Group Item #2 content
              </div>
            </div>
          </div>
        </div>
        """,
        height=600,
    )