import platform
import psutil
import subprocess
import os
import winreg  # Apenas para Windows
import json
import socket

def get_system_info():
    return {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Architecture": platform.architecture()[0],
    }

def get_memory_info():
    memory = psutil.virtual_memory()
    return {
        "Total Memory": f"{memory.total / 1e9:.2f} GB",
        "Available Memory": f"{memory.available / 1e9:.2f} GB",
        "Used Memory": f"{memory.used / 1e9:.2f} GB",
        "Memory Percentage": f"{memory.percent}%",
    }

def get_disk_info():
    disks = []
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        disks.append({
            "Device": partition.device,
            "Mountpoint": partition.mountpoint,
            "File System Type": partition.fstype,
            "Total Space": f"{usage.total / 1e9:.2f} GB",
            "Used Space": f"{usage.used / 1e9:.2f} GB",
            "Free Space": f"{usage.free / 1e9:.2f} GB",
            "Percentage Used": f"{usage.percent}%",
        })
    return disks

def get_driver_info():
    drivers = []
    if os.name == 'nt':  # Windows
        result = subprocess.run(["driverquery"], capture_output=True, text=True)
        drivers = result.stdout.splitlines()
    elif os.name == 'posix':  # Linux/Mac
        try:
            result = subprocess.run(["lsmod"], capture_output=True, text=True)
            drivers = result.stdout.splitlines()
        except FileNotFoundError:
            drivers = ["lsmod command not available. Install it using: sudo apt install kmod (for Linux)"]
    return drivers

def get_network_info():
    network_info = []
    for interface, addrs in psutil.net_if_addrs().items():
        iface_info = {"Interface": interface}
        for addr in addrs:
            if addr.family == socket.AF_LINK:
                iface_info["MAC Address"] = addr.address
            elif addr.family == socket.AF_INET:
                iface_info["IPv4 Address"] = addr.address
            elif addr.family == socket.AF_INET6:
                iface_info["IPv6 Address"] = addr.address
        network_info.append(iface_info)
    return network_info

def get_installed_programs():
    programs = []
    if os.name == 'nt':  # Windows
        try:
            reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as reg_key:
                for i in range(winreg.QueryInfoKey(reg_key)[0]):
                    try:
                        subkey = winreg.EnumKey(reg_key, i)
                        with winreg.OpenKey(reg_key, subkey) as program_key:
                            program_name = winreg.QueryValueEx(program_key, "DisplayName")[0]
                            programs.append(program_name)
                    except EnvironmentError:
                        continue
        except Exception as e:
            programs.append(f"Error retrieving installed programs: {e}")
    elif os.name == 'posix':  # Linux/macOS
        result = subprocess.run(["dpkg-query", "-W"], capture_output=True, text=True) if platform.system() == 'Linux' else []
        programs = result.stdout.splitlines() if result else ["Command not available for macOS."]
    return programs

def get_running_processes():
    processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'status']):
        try:
            processes.append({
                "PID": proc.info['pid'],
                "Name": proc.info['name'],
                "Status": proc.info['status'],
            })
        except psutil.NoSuchProcess:
            continue
    return processes

def save_to_json(data, filename="system_info.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"\nOs resultados foram salvos em {filename}")
    except Exception as e:
        print(f"Erro ao salvar os dados no arquivo JSON: {e}")

if __name__ == "__main__":
    data = {
        "System Information": get_system_info(),
        "Memory Information": get_memory_info(),
        "Disk Information": get_disk_info(),
        "Network Information": get_network_info(),
        "Driver Information": get_driver_info(),
        "Installed Programs": get_installed_programs(),
        "Running Processes": get_running_processes(),
    }

    # Exibe os dados no console
    for section, info in data.items():
        print(f"\n{section}:")
        if isinstance(info, list):
            for item in info:
                print(item)
        else:
            for key, value in info.items():
                print(f"{key}: {value}")

    # Salva os dados no arquivo JSON
    save_to_json(data)

    input("\nPressione Enter para sair...")
