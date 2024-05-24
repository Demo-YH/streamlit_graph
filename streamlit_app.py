import streamlit as st                  #web用パッケージ
import matplotlib as mlp                #グラフ描画
import matplotlib.pyplot as plt         #matplotlibパッケージ内のモジュール
from mpl_toolkits.mplot3d import Axes3D
import numpy as np                      #ベクトルや行列の計算を高速に処理するためのライブラリ
import csv                              #CSV
import pandas as pd                     #データの統計量を表示したり、グラフ化するなど、データ分析や機械学習で必要となる作業を簡単に行うことができる
import sympy as sym                     #式をそのままグラフにしてくれる
from sympy.plotting import plot         #式をそのままグラフにしてくれる
import time
import japanize_matplotlib              #font

# ページ情報、基本的なレイアウト
st.set_page_config(
    page_title="test streamlit",
    page_icon="☃",
    initial_sidebar_state="expanded",
)

#CSV読み込み
def w_graph():
        #データフレーム作成し、データの先頭から読み込み
        df=pd.read_csv('data.csv',encoding='shift_jis', parse_dates=True, index_col=0)

        #レイアウト別表示
        col1, col2, col3 = st.columns([7,1,4])
        with col1:
            col1.subheader("2024年4月日別気温")
            col1.line_chart(df) # type: ignore

        with col2:
            col2.subheader("")
            
        with col3:
            col3.subheader("気温データ")
            #データフレーム表示
            col3.dataframe(df)
            #雪が降る
            col3.snow()

#リアルタイムで正弦波
def sin_g():

    # 折れ線グラフ (初期状態)
    x = np.arange(0, np.pi*4, 0.1)
    line_chart = st.line_chart(x)

    for i in range(10):
        y = np.sin(x)
        # 折れ線グラフに 0.5 秒間隔で 10 回データを追加する
        additional_data = y
        line_chart.add_rows(additional_data)
        time.sleep(0.5)

#正接
def tan_g():
        with st.sidebar: 
            num = st.slider("スライダー", 1, 10, 1)

        with st.expander("押して！"):
            st.write("スライダーでグラフ表示変化。")

            #グラフ描画
            x = np.linspace(0, 10, 100)
            y = np.tan(x*num)

            fig, ax = plt.subplots()
            plt.plot(x, y)
            st.pyplot(fig)

#数式をグラフ表示
def f_g():

    #数式の作成
    #変数定義
    x = sym.Symbol('x')
    #size = 5

    #xの二乗＋5x＋4
    expr = x**2 + 5*x + 4
 
    #グラフ表示
    plot(expr, (x, -10, 10), title='X', xlabel='x', ylabel='x**2+5x+4')
    st.pyplot()

#散布図
def s_graph():
        #標準正規分布に従った乱数を100個生成
        x = np.random.randn(100)*0.5
        y = np.random.randn(100)
        x1 = np.random.randn(100)*0.5+0.5
        y1 = np.random.randn(100)

        #x軸とy軸にラベル付け
        plt.grid()
        plt.legend()
        plt.xlabel("xの乱数")
        plt.ylabel("yの乱数")

        #散布図を作成
        plt.scatter(x, y,s=100, c='blue',  marker='*', alpha=0.5,label="star")
        plt.scatter(x1, y1,s=100, c='orange',  marker='*', alpha=0.5,label="star2")
        plt.title("標準正規分布に従った乱数を100個生成")
        plt.legend()

        #colorbarを表示 
        plt.colorbar()

        #散布図を表示
        st.pyplot()

#3次元等高線
def contour():
        # Figureと3DAxeS
        fig = plt.figure(figsize = (6, 6))
        ax = fig.add_subplot(111, projection="3d")

        # 軸ラベルを設定
        ax.set_xlabel("x", size = 16)
        ax.set_ylabel("y", size = 16)
        ax.set_zlabel("z", size = 16)

        # 円周率の定義
        pi = np.pi

        # (x,y)データを作成
        x = np.linspace(-3*pi, 3*pi, 256)
        y = np.linspace(-3*pi, 3*pi, 256)

        # 格子点を作成
        X, Y = np.meshgrid(x, y)

        # 高度の計算式
        Z = np.cos(X/pi) * np.sin(Y/pi)

        # 曲面を描画
        ax.plot_surface(X, Y, Z, cmap = "summer")

        # 底面に等高線を描画
        ax.contour(X, Y, Z, colors = "black", offset = -1)
        st.pyplot()

#コンボボックス内選択肢作成
with st.sidebar:
    st.write("Streamlit表示確認")
st.set_option('deprecation.showPyplotGlobalUse', False)
option = st.sidebar.selectbox(
    "グラフ選択", 
    ['CSV読み込み', '正弦波', '正接', '数式をグラフ表示', '散布図','3次元等高線']
)

#選択内容による分岐
if option == "CSV読み込み":         #CSV読み込み選択
    w_graph()
elif option == "正弦波":            #正弦波選択
    sin_g()
elif option == "正接":              #正接選択
    tan_g()
elif option == "数式をグラフ表示":  #数式選択
    f_g()
elif option == "散布図":            #散布図選択
    s_graph()
elif option == "3次元等高線":       #3次元等高線
    contour()
else:
    print("エラー")                 #error