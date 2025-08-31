from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Static
import psutil
import platform
from datetime import datetime


# uptime
def uptime():
    boot = psutil.boot_time()
    now = datetime.now().timestamp()
    up_s = now - boot
    hrs = int(up_s // 3600)
    mins = int((up_s % 3600) // 60)
    return f"{hrs}h {mins}m"


# ram
def ram():
    ram = psutil.virtual_memory()
    # bytes to gb
    used = ram.used / (1024**3)
    total = ram.total / (1024**3)
    return f"{used:.1f} GB / {total:.1f} GB"


class Tamagotchi(App):
    CSS_PATH = "styles.tcss"

    def compose(self) -> ComposeResult:
        with open("faces/idle-face.txt", "r") as f:
            face = f.read()

        yield Container(Static(face, id="face"), id="center_container")

        with Horizontal(id="bottom_bar"):
            with Vertical(id="up_container"):
                yield Static("Uptime:", classes="title")
                yield Static(uptime(), id="uptime")
            with Vertical(id="ram_container"):
                yield Static("RAM:", classes="title")
                yield Static(ram(), id="ram")

    def on_mount(self):
        self.set_interval(1, self.update)

    async def update(self):
        self.query_one("#uptime", Static).update(uptime())
        self.query_one("#ram", Static).update(ram())


if __name__ == "__main__":
    Tamagotchi().run()
