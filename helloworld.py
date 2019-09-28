
import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(1)
        pyxel.text(pyxel.width / 2, pyxel.height / 2, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.text(0, 0, "AAAAA", 15)
        pyxel.text(4, 0, "AAAAA", 15)
        pyxel.text(0, 50, "BBBBB\nBBBBB", 15)
        pyxel.text(0, 100, "BBBBB", 15)
        pyxel.text(0, 106, "BBBBB", 15)

App()
