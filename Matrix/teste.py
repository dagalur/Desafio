n = ['7 3', 'Tsi','h%x','i #','sM','$a','#t%','ir!']

worda = ''
wordb = ''
wordc = ''
wordd = ''
m = 0

while m < 8:
    match m:
        case 1:
            worda = n[m].replace('si','')
            wordb = n[m].replace('T','')
        case 2:
            worda += n[m].replace('%x','') + wordb[::-1] + ' '
            wordc = n[m].replace('h%','')
        case 3:
            worda += n[m].replace(' #','')
        case 4:
            wordb = n[m].replace('s','')
            worda += n[m].replace('M','') + ' ' + wordb
        case 5:
            worda += n[m].replace('$','')
        case 6:
            worda += n[m].replace('#','').replace('%','')
            wordb = n[m].replace('t',' ')
        case 7:
            wordd = n[m].replace('ir', '')
            worda += (n[m])[::-1].replace('!','') + wordc + wordb + wordd
    m+=1

print('\n' + worda)