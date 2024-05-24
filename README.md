# Draw_Graphをwxpythonからstreamlitに移行
## 環境  
<img alt="Static Badge" src="https://img.shields.io/badge/-%20?style=plastic&logo=Windows10&logoColor=%230078D6&label=Windows10&labelColor=%23000000&color=000000"> <img alt="Static Badge" src="https://img.shields.io/badge/-Visual%20Studio%20Code?style=plastic&logo=Visual%20Studio%20Code&logoColor=%23007ACC&label=Visual%20Studio%20Code&labelColor=000000&color=000000"> <img alt="Static Badge" src="https://img.shields.io/badge/streamlit-s?style=plastic&logo=streamlit&logoColor=%23FF4B4B&labelColor=000000&color=000000">
 <img alt="Static Badge" src="https://img.shields.io/badge/-Python?style=plastic&logo=Python&logoColor=%233776AB&label=Python&labelColor=000000&color=000000"> <img alt="Static Badge" src="https://img.shields.io/badge/-Python?style=plastic&logo=pandas&logoColor=%233776AB&label=Pandas&labelColor=000000&color=000000"><br><img alt="Static Badge" src="https://img.shields.io/badge/-NumPy?style=plastic&logo=NumPy&logoColor=%23013243&label=NumPy&labelColor=c1c1c1&color=c1c1c1"> <img alt="Static Badge" src="https://img.shields.io/badge/-Sympy%09?style=plastic&logo=sympy&logoColor=%233B5526&label=sympy&labelColor=c1c1c1&color=c1c1c1"> <img alt="Static Badge" src="https://img.shields.io/badge/-Matplotlib?style=plastic&logo=Matplotlib&logoColor=%23013243&label=Matplotlib&labelColor=c1c1c1&color=c1c1c1">  

## 構築手順  
#### 1. python3.11.4　インストール  
#### 2. python -m venv 環境名　コマンドにてTerminalから環境作成  
#### ※Anaconda環境だとgit連携ができなかったためvenvにて環境構築
#### 3. pip install モジュール名　で必要なモジュールをインストールし、処理実装 
#### ※正弦波グラフは原点がうまく設定できず検討中の為未完(開始位置が不適切)
#### 4. pip list --format=freeze > requirements.txt　コマンドにて　　
####　　デプロイ時にパッケージinstallの為のパッケージ一覧ファイル作成  
#### 5. [Streamlit Cloud](https://streamlit.io/cloud)でデプロイ  
[動作はこちらから見れます。](https://appgraph-yzmjv8fmlkn3klcz4spony.streamlit.app)

