cpu = float(input())
gpu = float(input())
ram = float(input())
number_ram = int(input())
percent_discount = float(input())

cpu_in_leva = cpu * 1.57
gpu_in_leva = gpu * 1.57
total_ram = (ram * 1.57) * number_ram
discount_cpu = cpu_in_leva - (cpu_in_leva * percent_discount)
discount_gpu = gpu_in_leva - (gpu_in_leva * percent_discount)
total_price = discount_cpu + discount_gpu + total_ram
print(f"Money needed - {total_price:.2f} leva.")