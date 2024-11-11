class Fila:
    """Abstração de qualquer tipo de fila
    - supermercado
    - processos
      etc"""
    
    c_fila = []

    @classmethod
    def c_entrar(cls, obj):
        cls.c_fila.append(obj
                          )

    def __init__(self):
        self.s_fila = []