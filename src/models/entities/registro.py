class Registro():

    def __init__(self, id_registro, id_paciente, id_medico, resul_tb, result_no_tb, result_normal) :
        self.id_registro = id_registro
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.result_tb = resul_tb
        self.result_no_tb = result_no_tb
        self.result_normal = result_normal


    def to_JSON(self):
        return {
            'id_registro': self.id_registro,
            'id_paciente': self.id_paciente,
            'id_medico': self.id_medico,
            'result_tb': self.result_tb,
            'result_no_tb': self.result_no_tb,
            'result_normal': self.result_normal
        }
