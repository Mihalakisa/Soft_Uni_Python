import matplotlib.pylab as p

percent = (70, 25, 2, 2, 1)
languages = ('Python', 'Java', 'C++', 'Go', 'JavaScript')
p.pie(percent, labels=languages)
p.show()