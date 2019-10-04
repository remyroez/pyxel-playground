
import pyxel

# アプリケーションクラス
class App:
    # コンストラクタ
    def __init__(self):
        # ウィンドウ初期化
        pyxel.init(160, 120, caption="Hello Pyxel")

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

        # Hello
        pyxel.text(pyxel.width / 2, pyxel.height / 2, "Hello, Pyxel!", pyxel.frame_count % 16)

        # フォントの横幅
        pyxel.text(0, 0, "AAAAA", 15)
        pyxel.text(4, 0, "AAAAA", 15)

        # フォントの縦幅
        pyxel.text(0, 50, "BBBBB\nBBBBB", 15)
        pyxel.text(0, 80, "BBBBB", 15)
        pyxel.text(0, 86, "BBBBB", 15)

        # カラー列挙
        for i in range(15):
            pyxel.text(4 * i, 30, 'X', i)

# アプリケーションクラスのインスタンス化
# コンストラクタ内で Pyxel が起動し、終了するまで戻ってこない
App()
