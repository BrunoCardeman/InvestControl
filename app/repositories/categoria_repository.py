from app.models.categoria import Categoria


class CategoriaRepository:
    def __init__(self, session):
        self.session = session

    def listar_todos(self):
        return self.session.query(Categoria).all()
        
    def buscar_por_id(self, id_categoria):
        return self.session.get(Categoria, id_categoria)
    
    def adicionar_Categoria(self, categoria):
        self.session.add(categoria)
        self.session.flush()
        return categoria

    def remover_Categoria(self, id_categoria):
        obj_Categoria = self.buscar_por_id(id_categoria)
        if obj_Categoria is None:
            return False
        self.session.delete(obj_Categoria)
        self.session.flush()

  