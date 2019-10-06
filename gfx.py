
import pyxel

# アプリケーションクラス
class App:
    # コンストラクタ
    def __init__(self):
        # ウィンドウ初期化
        pyxel.init(160, 120, caption="Hello Pyxel")

        # イメージ 0 番を定義
        self.cat = pyxel.image(0)

        # 画像の読み込み
        self.cat.load(0, 0, 'assets/cat_16x16.png')

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

        # 画像の描画
        pyxel.blt(0, 0, 0, 0, 0, self.cat.width, self.cat.height)

# アプリケーションクラスのインスタンス化
# コンストラクタ内で Pyxel が起動し、終了するまで戻ってこない
App()
