streamlitでデプロイする用  
https://bgrerollsim.streamlit.app/  
  
  
ローカルで使う場合はこのリポジトリをgit cloneして  
requirements.txtからstreamlitとpandasをインストールして   
コマンドラインから  
~~~実行コマンド
streamllit run BGSim.py
~~~
を実行するだけ  
  
data_jis.csvを編集すれば新しい環境でも対応可能  
ローカルで使う場合はcsv欄の'name'.pngという名前の画像を  
imgフォルダに保存すると画像が表示される  
  
existが1である場合にのみ計算対象となる。  
一時的な削除の場合等、データ自体は残しておきたい場合はexistを0にしておく
