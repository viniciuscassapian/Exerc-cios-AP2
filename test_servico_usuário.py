from unittest.mock import Mock

class ServicoUsuario:
    def __init__(self, api):
        self.api = api

    def pegar_nome(self, user_id: int):
        user = self.api.buscar(user_id)
        return user["nome"]

class ApiStub:
    def buscar(self, user_id):
        return {"id": user_id, "nome": "Vinícius"}
    
def test_com_stub():
    api = ApiStub()
    service = ServicoUsuario(api)
    resultado = service.pegar_nome(1)
    assert resultado == "Vinícius"

def test_com_mock():
    api = Mock()
    api.buscar.return_value = {"id": 1, "nome": "Vinícius Cassapian"}
    service = ServicoUsuario(api)
    resultado = service.pegar_nome(1)
    api.buscar.assert_called_once_with(1)
    assert resultado == "Vinícius Cassapian"
