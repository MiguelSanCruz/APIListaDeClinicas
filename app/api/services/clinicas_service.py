lista_clinicas = {
    1 :{"clinica":"São José","especialidade":"Cardiologia","endereco":"Rua A, 123"},
    2 :{"clinica":"Saude+","especialidade":"Ortopedia","endereco":"Avenida B, 456"},
    3 :{"clinica":"Silveira","especialidade":"Pediatria","endereco":"Travessa C, 789"}
}
tamanho_lista = len(lista_clinicas)+1

class ClinicasService:
    def get_all(self):
        return list(lista_clinicas.values())

    def update(self, id, dados):
        if id not in lista_clinicas:
            return None
        
        item = lista_clinicas[id]

        for campo, valor in dados.items():
            if valor is not None:
                item[campo] = valor    

        return item


    def post(self, novo):
        global tamanho_lista
        criado = {"id": tamanho_lista, **novo}
        lista_clinicas[tamanho_lista] = criado
        tamanho_lista += 1
        return criado


    def delete(self, id):
        if id not in lista_clinicas:
            return None

        removido = lista_clinicas[id]
        del lista_clinicas[id]
        return removido
        