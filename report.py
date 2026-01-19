from rich.console import Console
from rich.table import Table

from cpu import get_top_cpu_processes
from memory import get_memory_status
from temperature import get_temperatures

console = Console()

def run_scan():
    console.print("\n🩺 Linux System Doctor Scan\n", style="bold green")

    # CPU
    procs = get_top_cpu_processes()

    table = Table(title="Top CPU Processes")
    table.add_column("PID")
    table.add_column("Name")
    table.add_column("CPU %")

    for p in procs:
        table.add_row(str(p["pid"]), p["name"] or "?", f"{p['cpu_percent']}")

    console.print(table)

    # Memory
    vm, swap = get_memory_status()

    console.print(f"\n💾 Memory used: {vm.percent}%")
    console.print(f"🌀 Swap used: {swap.percent}%")

    if swap.percent > 50:
        console.print("⚠ High swap usage detected", style="bold yellow")

    # Temperature
    temps = get_temperatures()

    if temps:
        console.print("\n🌡 Temperatures:", style="bold cyan")
        for t in temps:
            line = f"{t['sensor']} {t['label']}: {t['current']}°C"
            if t["high"] and t["current"] >= t["high"]:
                console.print("  " + line + "  ⚠ HOT", style="bold red")
            else:
                console.print("  " + line)
    else:
        console.print("\n🌡 Temperatures: Not available")

    console.print("\n✅ Scan complete\n", style="bold green")
