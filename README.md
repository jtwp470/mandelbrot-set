# マンデルブロ集合

![](./img/top.png)
## Requirements

* Python 3.4
* Numpy
* Pygame
* Cython

各位自分の環境に適当にインストールしてください.

## セットアップ方法の例

```
$ git clone https://github.com/jtwp470/mandelbrot-set.git
$ cd mandelbrot-set
$ virtualenv ./ --python=/usr/local/bin/python3
$ source ./bin/activate
$ pip install -r requirements.txt
$ cd src
$ python3 setup.py build_ext --inplace
$ python3 mandel.py
```

しかしPygameをインストール出来ない場合は次のようにしてください.

```
$ pip3 install hg+http://bitbucket.org/pygame/pygame
```

またOSXではvirtualenv環境で使おうとすると何故か上手く動かないので面倒ですが普通にpipで入れてください.

さらに1回目の描画の時だけ画像が出力されませんがGUI上でSPCキーを押すと問題なく表示されますのでそれでお使い下さい.

## 使い方, キーボードショートカット

### 高さと幅の設定
起動時にオプションの指定により高さと幅をそれぞれ指定できます.

例:1920 x 1080

```
$ python3 mandel.py --width 1920 --height 1080
```

なおこの引数は省略可能で省略した場合は720x480の大きさで描画されます.

### 描画範囲の設定
オプションに```--minx, --maxx, --miny, --maxy```というものがあり各描画範囲をx, yの範囲で設定することができます.

使用例:
```$ python3 mandel.py --minx -2 --maxx 1 --miny -1.5 --maxy 1.5```

### その他のオプション
その他のオプションに関しては
```
$ python3 mandel.py -h
usage: mandel.py [-h] [--width WIDTH] [--height HEIGHT] [--minx MINX]
[--maxx MAXX] [--miny MINY] [--maxy MAXY] [--iters ITERS]

This program is plotting mandelbrot set using Pygame and Numpy

optional arguments:
-h, --help       show this help message and exit
--width WIDTH    スクリーンの幅 デフォルト値:720
--height HEIGHT  スクリーンの高さ デフォルト値:480
--minx MINX      xの最小値 デフォルト値:2.0
--maxx MAXX      xの最大値 デフォルト値:1.0
--miny MINY      yの最小値 デフォルト値:-1.5
--maxy MAXY      yの最大値 デフォルト値:1.5
--iters ITERS    反復回数 デフォルト値:30回
```
とでてくるのでこれらを参考にして下さい

### キーボードショートカット
|キーボードショートカット|機能の説明|
|:----------------------:|----------|
|<kbd>i</kbd>|拡大|
|<kbd>o</kbd>|縮小|
|<kbd>l</kbd>|右へ移動|
|<kbd>h</kbd>|左へ移動|
|<kbd>k</kbd>|上へ移動|
|<kbd>j</kbd>|下へ移動|
|<kbd>s</kbd>|画面を保存|
|<kbd>q</kbd>|プログラムを終了|

## さらなる高速描画のために
さらなる高速描画を求めてついにCythonに手を出してしまいました.

例はCython Wikiの[Optimizing Cython for Mandelbrot fractal calculations](https://github.com/cython/cython/wiki/examples-mandelbrot)
のコードを参考にしました.

主にマンデルブロ集合に属しているかどうかを判定する部分で時間がかかるのでそこをCythonで書きなおしてみました.少し早くなったと思います.

## 実行例
最大反復回数は1000回か10000回で描画しています.
![](./img/0765074.png)
![](./img/0740747.png)
![](./img/0749307487.png)
![](./img/0749107491.png)
## 参考

* [A NumbaPro Mandelbrot Example](http://nbviewer.ipython.org/gist/harrism/f5707335f40af9463c43)
* [Optimizing Cython for Mandelbrot fractal calculations](https://github.com/cython/cython/wiki/examples-mandelbrot)
