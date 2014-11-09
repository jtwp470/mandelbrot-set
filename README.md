# マンデルブロ集合

## Requirements

* Python 3.4
* Numpy
* Pygame

各位自分の環境に適当にインストールしてください.

## セットアップ方法の例

```
$ git clone https://github.com/jtwp470/mandelbrot-set.git
$ cd mandelbrot-set
$ virtualenv ./ --python=/usr/local/bin/python3
$ source ./bin/activate
$ pip install -r requirements.txt
$ python3 src/mandel.py
```

しかしPygameをインストール出来ない場合は次のようにしてください.

```
$ pip3 install hg+http://bitbucket.org/pygame/pygame
```

## 使い方, キーボードショートカット
起動時にオプションの指定により高さと幅をそれぞれ指定できます.

例:1920 x 1080

```
$ python3 mandel.py --width 1920 --height 1080
```

なおこの引数は省略可能で省略した場合は720x480の大きさで描画されます.


キーボードショートカット:

|キーボードショートカット|機能の説明|
|------------------------|----------|
|<kbd>i</kbd>|拡大|
|<kbd>o</kbd>|縮小|
|<kbd>l</kbd>|右へ移動|
|<kbd>h</kbd>|左へ移動|
|<kbd>k</kbd>|上へ移動|
|<kbd>j</kbd>|下へ移動|
|<kbd>s</kbd>|画面を保存|
|<kbd>q</kbd>|プログラムを終了|
