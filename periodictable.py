# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 06:38:56 2021

@author: Don
"""
import csv, sys, re
elementsFile = open(r'C:\Users\user\Downloads\periodictable.csv', encoding='utf-8')
elementsCsvReader = csv.reader(elementsFile)
elements = list(elementsCsvReader)
elementsFile.close()

#atomic number, symbol, name, atomic mass in au or g/mol ,CPK color in RRGGBB hex format, electronic configuration, electronegativity in Pauling, atomic radius in pm, ion radius in pm, van der Waals radius in pm, IE-1 in kJ/mol, EA in kJ/mol, oxidation states, standard state, bonding type,melting point in K
#boiling point in K, density in g/mL, metal or nonmetal? year discovered
ALL_COLUMNS= ['atomic Number','symbol', 'name','atomic mass','CPK color','electronic config',
              'electronegativity','atomic radius','ion radius','van der Waals','IE-1',
              'EA','oxidation states','standard state','bonding type', 'melting point',
              'boiling point','density','metal','year discovered']
LONGEST_COLUMN =0
for key in ALL_COLUMNS:
    if len(key) > LONGEST_COLUMN:
        LONGEST_COLUMN = len(key)
        
        
ELEMENTS= {}
for line in elements:
    element = {'atomic Number': line[0],
               'symbol': line[1], 
               'name': line[2],
               'atomic mass': line[3] +'au',
               'CPK color': line[4],
               'electronic config': line[5],
               'electronegativity': line[6],
               'atomic radius': line[7],
               'ion radius': line[8],
               'van der Waals': line[9],
               'IE-1': line[10],
               'EA': line[11],
               'oxidation states': line[12],
               'standard state': line[13],
               'bonding type': line[14],
               'melting point': line[15],
               'boiling point': line[16],
               'density': line[17],
               'metal': line[18],
               'year discovered': line[19]
              }
    #or key, value in element.items():
    #    element[key] = re.sub(r'\[(I|V|X)+\]', '', value)
    ELEMENTS[line[0]] = element
    ELEMENTS[line[1]] = element
    
print('Periodic Talbe of Elements')
print()
while True:
    print('''        Periodic Table of Elements
            1   2  3  4  5  6  7  8  9  10 11 12  13  14  15  16  17 18
          1 H                                                         He
          2 Li Be                                  B   C   N   O  F   Ne
          3 Na Mg                                  Al  Si  P   S  Cl  Ar
          4 K  Ca Sc Ti  V Cr Mn Fe Co Ni Cu  Zn  Ga  Ge  As  Se  Br  Kr
          5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag  Cd  In  Sn  Sb  Te  I   Xe
          6 Cs Ba La Hf Ta W  Re Os Ir Pt Au  Hg  Tl  Pb  Bi  Po  At  Rn
          7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg  Cn  Nh  Fl  Mc  Lv  Ts  Og
          
                  Ce Pr Nd Pm Sm Eu Gd Tb Dy  Ho  Er  Tm  Yb  Lu
                  Th Pa U  Np Pu Am Cm Bk Cf  Es  Fm  Md  No  Lr
          ''')
    print('Enter a Symbol or atomic number to examine, or QUIT to quit')
    response = input('>').title()
    if response == 'Quit':
        sys.exit()

    if response in ELEMENTS:
        for key in ALL_COLUMNS:
            keyJustified = key.rjust(LONGEST_COLUMN)

            print(keyJustified +':' + str(ELEMENTS[response][key]))
        input('Press Enter to continue...')