from pycomm3 import SLCDriver

CLP_IRRIGACAO = '172.17.85.114'

with SLCDriver(CLP_IRRIGACAO) as plc:
    bit_ativar = 'B10:2/6'

    def ativarIrrigacao():
        plc.write((bit_ativar, True))

    def desativarIrrigacao():
        plc.write((bit_ativar, False))

    def statusIrrigacao():
        return plc.read(bit_ativar)

    status = statusIrrigacao()  # Retorna uma Tag
    print('Status Irrigação:', status)
    if status[1].value == True:
        desativarIrrigacao()
    else:
        ativarIrrigacao()
    status = statusIrrigacao()  # Retorna uma Tag
    print('Status Irrigação:', status)

    print(f'Tipo do Status: {type(status)}')



