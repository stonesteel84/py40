import psutil

cpu = psutil.cpu_freq()
print("cpu =",cpu)

cpu_core = psutil.cpu_count(logical=False)
print("cpu_core =",cpu_core)

memory = psutil.virtual_memory()
print("memory =",memory)

disk = psutil.disk_partitions()
print("cdiskpu =",disk)

net = psutil.net_io_counters()
print("net =",net)
