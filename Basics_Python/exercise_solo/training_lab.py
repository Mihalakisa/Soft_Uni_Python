w = float(input('weight in meters: '))
h = float(input('heigh in meters: '))

labWidth = int(h * 100) - 100
labHeight = int(w * 100)

descInOrder = labWidth // 70
seats = labHeight // 120

all_seats = descInOrder * seats - 3

print(all_seats)