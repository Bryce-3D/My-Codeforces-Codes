l = []
for i in range(10):
    l.append( int(input()) )
names = ['ITIM','PUTI','PULA','BUGHAW','DILAW','LUNTIAN','TSOKOLATE','LILA']
names.append('DALANDAN')
names.append('LUNTIAN PERO MEDYO DILAW')

beeg = max(l)
ind = l.index(beeg)

print('SI ' + names[ind] + ' AY SINIPA PALABAS.')
