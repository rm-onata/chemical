import pyfiglet
from listt import all
import os
import platform
from colorama import Fore, init
init()



syst = platform.uname()[0]
if syst == "Linux":
    os.system("clear")
else:
    os.system("cls")




txt = pyfiglet.figlet_format("Chemical tanavoby", font="slant")
print(txt)

print(Fore.LIGHTMAGENTA_EX+" github : https://github.com/rm-onata \n ")








def help():
        if "help" in name:
            print(Fore.BLUE+"""type:
            H
            He
            Li
            Be
            B
            C
            N
            O
            F
            Ne
            Na
            Mg
            Al
            Si
            P
            S
            Cl
            Ar
            K
            Ca
            Sc
            Ti
            V
            Cr
            Mn
            Fe
            Co
            Ni
            Cu
            Zn
            Ga
            Ge
            As
            Se
            Br
            Kr
            Rb
            Sr
            Y
            Zr
            Nb
            Mo
            Tc
            Ru
            Rh
            Pd
            Ag
            Cd
            In
            Sn
            Sb
            Te
            I
            Xe
            Cs
            Ba
            La
            Ce
            Pr
            Nd
            Pm
            Sm
            Eu
            Gd
            Tb
            Dy
            Ho
            Er
            Tm
            Yb
            Lu
            Hf
            Ta
            W
            Re
            Os
            Ir
            Pt
            Au
            Hg
            Tl
            Pb
            Bi
            Po
            At
            Rn
            Fr
            Ra
            Ac
            Th
            Pa
            U
            Np
            Pu
            Am
            Cm
            Bk
            Cf
            Es
            Fm
            Md
            No
            Lr
            Rf
            Db
            Sg
            Bh
            Hs
            Mt
            Ds
            Rg
            Cn
            Fl
            Lv
            """)
    






while True:
    print(Fore.LIGHTCYAN_EX+"enter "+Fore.BLUE+"exit"+Fore.LIGHTCYAN_EX+" for close ")
    print(Fore.LIGHTCYAN_EX+"See the output of "+Fore.BLUE+"help"+Fore.LIGHTCYAN_EX+" for a summary of options. ")
    name = input(Fore.WHITE+" \n enter a symbol ==>  ")
    print("\n\n")

    if "exit" == name:
        break
    else:
        for i in all.keys():
            if i == name:
                print(Fore.GREEN+all[i])

        print(Fore.WHITE+" \n ---------------------\n")

