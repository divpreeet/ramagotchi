from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Static


class Tamagotchi(App):
    CSS_PATH = "styles.css"

    def compose(self) -> ComposeResult:
        with open("faces/idle-face.txt", "r") as f:
            face = f.read()

        yield Container(Static(face, id="face"), id="center_container")


if __name__ == "__main__":
    Tamagotchi().run()
