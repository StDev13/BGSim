streamlitでデプロイする用  
https://bg-sim.streamlit.app/  
  
  
ローカルで使う場合はこのリポジトリをgit cloneして  
requirements.txtからstreamlitとpandasをインストールして   
コマンドラインから  
~~~実行コマンド
streamllit run BGSim.py
~~~
を実行するだけ  
  
data_jis.csvを編集すれば新しい環境でも対応可能  
新しいカードを追加する場合はcsvの'name'欄と同名の.png画像ファイルを  
imgフォルダに保存すると画像が表示される  
  
existが1である場合にのみ計算対象となる。  
一時的な削除の場合等、データ自体は残しておきたい場合はexistを0にしておく
