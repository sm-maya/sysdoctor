import psutil
import platform

def get_temperatures():
    system = platform.system().lower()

    # Only Linux supports this via psutil
    if system != "linux":
        return []

    if not hasattr(psutil, "sensors_temperatures"):
        return []

    temps = psutil.sensors_temperatures()
    results = []

    if not temps:
        return results

    for sensor, entries in temps.items():
        for e in entries:
            results.append({
                "sensor": sensor,
                "label": e.label or "N/A",
                "current": e.current,
                "high": e.high,
                "critical": e.critical
            })

    return results
