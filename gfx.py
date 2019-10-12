
import pyxel
import random

# アプリケーションクラス
class App:
    # コンストラクタ
    def __init__(self):
        # ウィンドウ初期化
        pyxel.init(160, 120, caption="Hello Pyxel")

        # イメージ 0 番を定義
        self.cat = {
            'width' : 16,
            'height' : 16,
            'path' : 'assets/cat_16x16.png',
        }

        # 画像の読み込み
        self.cat['image'] = pyxel.image(0).load(0, 0, self.cat['path'])

        # エンジン起動
        pyxel.run(self.update, self.draw)

    # 更新関数
    def update(self):
        # ボタン押下
        if pyxel.btnp(pyxel.KEY_Q):
            # 終了
            pyxel.quit()

    # 描画関数
    def draw(self):
        # 画面のクリア
        pyxel.cls(1)

        # 描画テスト
        for i in range(10):
            # 矩形
            pyxel.rectb(
                random.randrange(0, pyxel.width),
                random.randrange(0, pyxel.height),
                random.randrange(0, pyxel.width),
                random.randrange(0, pyxel.height),
                random.randrange(0, 16))

            # 線
            pyxel.line(
                random.randrange(0, pyxel.width),
                random.randrange(0, pyxel.height),
                random.randrange(0, pyxel.width),
                random.randrange(0, pyxel.height),
                random.randrange(0, 16))

            # 点
            pyxel.pix(
                random.randrange(0, pyxel.width),
                random.randrange(0, pyxel.height),
                random.randrange(0, 16))

            # 円
            pyxel.circb(
                random.randrange(0, pyxel.width),
                random.randrange(0, pyxel.height),
                random.randrange(0, 16),
                random.randrange(0, 16))

            # パレットの入れ替え
            pyxel.pal(random.randrange(0, 16), random.randrange(0, 16))

        # 画像の描画
        pyxel.blt((pyxel.width - self.cat['width']) / 2, (pyxel.height - self.cat['height']) / 2, 0, 0, 0, self.cat['width'], self.cat['height'])

        # パレットを戻す
        pyxel.pal()

# アプリケーションクラスのインスタンス化
# コンストラクタ内で Pyxel が起動し、終了するまで戻ってこない
App()
