import psutil
import time

def get_top_cpu_processes(limit=5):
    # First call initializes CPU tracking
    for p in psutil.process_iter():
        try:
            p.cpu_percent(None)
        except:
            pass

    # Wait a moment to measure real usage
    time.sleep(1)

    procs = []

    for p in psutil.process_iter(['pid', 'name']):
        try:
            cpu = p.cpu_percent(None)

            procs.append({
                'pid': p.pid,
                'name': p.info['name'],
                'cpu_percent': cpu
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    return sorted(procs, key=lambda x: x['cpu_percent'], reverse=True)[:limit]
