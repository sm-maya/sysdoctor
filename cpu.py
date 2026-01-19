import psutil

def get_top_cpu_processes(limit=5):
    psutil.cpu_percent(interval=0.5)

    procs = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            procs.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    return sorted(procs, key=lambda x: x['cpu_percent'], reverse=True)[:limit]
