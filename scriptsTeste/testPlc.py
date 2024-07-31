from pycomm3 import SLCDriver

plc = SLCDriver('172.17.85.114')

def ativarIrrigacao(plc, adress):
    plc.write((adress, True))

def desativarIrrigacao(plc, adress):
    plc.write((adress, False))

ativarIrrigacao(plc, 'B10:2/6')
