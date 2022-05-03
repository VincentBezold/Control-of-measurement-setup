import qcodes as qc
from ANC300 import ANC300
# https://qcodes.github.io/Qcodes_contrib_drivers/examples/Attocube_ANC300.html
ANC = ANC300( name='ANC300', address='ASRL9::INSTR' )
axis1 = ANC.submodules['axis1']
print( "FREQ ", axis1.frequency())
