import psutil
import socket
import time
import random
import speedtest
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.layout import Layout
from rich.table import Table

console = Console()

def get_system_info():
    """Fetches system stats (CPU, RAM, Disk, IP)."""
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "Unknown"

    return cpu_usage, ram_usage, disk_usage, ip_address

def get_network_speed():
    """Fetches internet speed (Download/Upload)."""
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = round(st.download() / 1_000_000, 2)
        upload_speed = round(st.upload() / 1_000_000, 2)
        return download_speed, upload_speed
    except:
        return "N/A", "N/A"

def glitch_text(text):
    """Adds random glitch effects to text."""
    glitched = list(text)
    for _ in range(random.randint(1, 3)):  # Randomly glitch 1-3 characters
        index = random.randint(0, len(glitched) - 1)
        glitched[index] = random.choice(["@", "#", "$", "!", "%", "&", "*"])
    return "".join(glitched)

def render_ui():
    """Creates the cyberpunk-styled UI."""
    cpu, ram, disk, ip = get_system_info()
    download_speed, upload_speed = get_network_speed()

    # Create Panels for System Info
    cpu_panel = Panel(Text(f"CPU: {cpu}%", style="bold green"), title="💻 CPU Usage", border_style="bright_green")
    ram_panel = Panel(Text(f"RAM: {ram}%", style="bold cyan"), title="🧠 RAM Usage", border_style="cyan")
    disk_panel = Panel(Text(f"Disk: {disk}%", style="bold magenta"), title="📀 Disk Usage", border_style="magenta")
    network_panel = Panel(Text(f"IP: {glitch_text(ip)}\n⬇ {download_speed} Mbps | ⬆ {upload_speed} Mbps", style="bold yellow"), title="🌐 Network", border_style="yellow")

    # Create the UI Layout
    layout = Layout()
    layout.split_column(
        Layout(cpu_panel, size=3),
        Layout(ram_panel, size=3),
        Layout(disk_panel, size=3),
        Layout(network_panel, size=5),
    )
    return layout

# Live Refresh Loop
with Live(render_ui(), console=console, refresh_per_second=1):
    while True:
        time.sleep(1)
