import psutil

def get_cpu_count():
    return str(psutil.cpu_count(logical=False))

def get_cpu_usage_percent():
    cpu_usage = psutil.cpu_percent(interval=1, percpu=False)
    return str(cpu_usage)

def get_ram_total():
    total_ram = psutil.virtual_memory().total
    return f"{round(total_ram)}"

def get_ram_used():
    used_ram = psutil.virtual_memory().used
    return f"{round(used_ram)}"

def generate_report():
    return {
        "CPU Count": get_cpu_count(),
        "CPU Usage": get_cpu_usage_percent(),
        "Total Ram": get_ram_total(),
        "Used Ram": get_ram_used()
    }

def main():
    print(f"CPU Count: {get_cpu_count()}")
    print(f"CPU Usage: {get_cpu_usage_percent()}%")
    print(f"Total Ram: {get_ram_total()}")
    print(f"Used Ram: {get_ram_used()}")

if __name__ == "__main__":
    main()
