v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

first_pipe_full = p1 * h
second_pipe_full = p2 * h
total_pipe_full = first_pipe_full + second_pipe_full

total_pipe_full_is = (total_pipe_full / v) * 100
first_pipe_is = (first_pipe_full / total_pipe_full) * 100
second_pipe_is = (second_pipe_full / total_pipe_full) * 100

if total_pipe_full <= v:
    print(f'The pool is {total_pipe_full_is:.2f}% full. Pipe 1: {first_pipe_is:.2f}%. Pipe 2: {second_pipe_is:.2f}%.')
else:
    overflow = total_pipe_full - v
    print(f'For {h:.2f} hours the pool overflows with {overflow:.2f} liters.')