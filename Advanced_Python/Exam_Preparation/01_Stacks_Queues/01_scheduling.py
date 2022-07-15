jobs = [int(job) for job in input().split(', ')]
target_index = int(input())

target_job = jobs[target_index]
cycles = 0

for i in range(len(jobs)):
    current_job = jobs[i]
    if current_job < target_job or current_job == target_job and target_index >= i:
        cycles += current_job

print(cycles)

# jobs = [int(job) for job in input().split(', ')]
# index = int(input())
# cycles = 0
# current_index = -1
#
# while current_index != index:
#     current_index = jobs.index(min(jobs))  # first occurrence of the min amount of clock cycles
#     current_job = min(jobs)  # take the amount of min clock cycles
#     jobs[current_index] = max(jobs) + 1  # set element on current index to max + 1 to not get processed again
#     cycles += current_job  # add the clock cycles
# print(cycles)