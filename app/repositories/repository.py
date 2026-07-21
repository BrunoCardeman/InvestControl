from typing import TypeVar, Generic

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):

    def __init__(self,session,model):
        self.session = session
        self.model = model

    def listar_todos(self):
        return self.session.query(self.model).all()

    def buscar_por_id(self, id_tipo):
        return self.session.get(self.model, id_tipo)
    
    def adicionar(self, tipo):
        self.session.add(tipo)
        self.session.flush()
        return tipo

    def remover(self, id_tipo):
        obj_tipo = self.buscar_por_id(id_tipo)
        if obj_tipo is None:
            return False
        self.session.delete(obj_tipo)
        self.session.flush()
