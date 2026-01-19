import psutil

def get_memory_status():
    vm = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return vm, swap
