def find_hair(dna):
    if(dna.find('GCCAGTGCCG') != -1):
        print 'Hair Color is Black.'
    elif(dna.find('CCAGCAATCGC') != -1):
        print 'Hair Color is Brown.'
    elif(dna.find('TTAGCTATCGC') != -1):
        print 'Hair Color is BLonde'

dna_file = open('dna.txt', 'r')
dna = dna_file.read()

find_hair(dna)
