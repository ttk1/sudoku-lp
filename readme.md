# 数独を線形計画問題として解く

* Python+pulpで実装
* pulp
  * http://coin-or.github.io/pulp/index.html
  * Python用の線形計画問題ライブラリ

## pulpのインストール

```sh
# venvの作成
python -m venv venv

# venvに入る(Windowsの場合)
source ./venv/Scripts/activate

# venvにpulpをインストール
python -m pip install pulp

# venvから出る
deactivate
```

後はVSCodeが良しなにやってくれるハズ...
