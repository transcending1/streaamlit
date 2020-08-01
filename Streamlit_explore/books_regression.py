import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from sklearn import tree
from sklearn.preprocessing import LabelEncoder as LabelEncode
from sklearn.tree import DecisionTreeRegressor

st.title('机器学习图书销量特征重要性分析')
f = open('机器学习图书.csv', encoding="utf8")
data = pd.read_csv(f)
label = data["sales"]
features = data.drop(["sales"], 1)
st.write("数据清洗前样例:")
st.write(data.iloc[:10, :])
model = DecisionTreeRegressor(max_depth=5)
label_model = LabelEncode()
features["Author"] = label_model.fit_transform(features["Author"].astype(str))
features["Publisher"] = label_model.fit_transform(features["Publisher"].astype(str))
features["Name"] = label_model.fit_transform(features["Name"].astype(str))
date = pd.to_datetime(features["Date"].dropna())
features["Date"] = features["Date"].fillna("2013-07-01")
features["PublishedDays"] = (date.max() - pd.to_datetime(features["Date"])).dt.days
features["Date"] = label_model.fit_transform(features["Date"].astype(str))


def transform(item):
    try:
        return int(item)
    except:
        return 0


features["Comment"] = features["Comment"].apply(transform)
st.write("对数据进行清洗,类别编码,缺失值中值填充后的样例")
fill_value = features.median()
features.fillna(fill_value, inplace=True)
st.write(features.iloc[:10, :])
model.fit(features, label)
st.write("特征重要性:")
print(model.feature_importances_)
st.write(pd.DataFrame(
    model.feature_importances_.reshape(1, -1),
    columns=features.columns))
dot_data = tree.export_graphviz(
    model,
    out_file=None,
    feature_names=features.columns,
    filled=True,
    impurity=False,
    rounded=True
)
import pydotplus

graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png("aaa.png")

from PIL import Image

image = Image.open('aaa.png')
st.image(image, caption='Decision Tree Graph', use_column_width=True)

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(20, 8), dpi=80)
plt.figure(figsize=(20, 8), dpi=80)
y = model.feature_importances_
x = range(len(y))

plt.bar(
    x,
    y,
    width=0.5
)
plt.xticks(x, features.columns)
st.pyplot()
