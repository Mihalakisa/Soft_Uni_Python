from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
papers = [int(x) for x in input().split(', ')]

box = 50
result = 0
box_count = 0
swap_paper = 0

while eggs and papers:
    current_egg = eggs[0]
    current_paper = papers[-1]

    if current_egg <= 0:
        eggs.popleft()
        continue

    if current_egg == 13:
        eggs.popleft()
        swap_paper = papers[0]
        papers[0] = papers[-1]
        papers.pop()
        papers.append(swap_paper)
        continue

    result = current_egg + current_paper

    if result <= box:
        box_count += 1
        eggs.popleft()
        papers.pop()
    else:
        eggs.popleft()
        papers.pop()

if box_count != 0:
    print(f"Great! You filled {box_count} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(str(egg) for egg in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(paper) for paper in papers)}")