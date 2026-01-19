import psutil

def get_temperatures():
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
