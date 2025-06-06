import psutil

cpu = psutil.cpu_freq()
cpu_current_ghz = round(cpu.current / 1000, 2)
print(f"cpu 속도: {cpu_current_ghz}GHz\n")

cpu_core = psutil.cpu_count(logical=False)
print(f"cpu 코어수: {cpu_core} 개\n"  )

memory = psutil.virtual_memory()
memory_total = round(memory.total / 1024**3)
print( f'메모리: {memory_total}GB\n' )

disk = psutil.disk_partitions()
for p in disk:
    print(p.mountpoint, p.fstype, end=' ')
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024**3)
    print(f'디스크 용량: {disk_total}GB\n' )

net = psutil.net_io_counters()
sent = round(net.bytes_sent/1024**2, 1)
recv = round(net.bytes_recv/1024**2, 1)
print(f'패킷 내보내기: {sent}MB   패킷 받기: {recv}MB\n')