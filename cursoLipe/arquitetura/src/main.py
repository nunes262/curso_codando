# Service
class Banco:
    def criar_usuario(self, nome: str, senha: str, email: str) -> bool:
        raise NotImplementedError()

# Adapter
class BancoTxt(Banco):
    def criar_usuario(self, nome: str, senha: str, email: str) -> bool:
        salva_user = open(f"{nome}.txt", "w+")
        salva_user.write(f"{nome}\n")
        salva_user.write(f"{senha}.\n")
        salva_user.write(f"{email}.\n")

        return True

# Usecases
def salvar_usuario_interface(banco: Banco, nome: str, senha: str, email: str):
    banco.criar_usuario(nome, senha, email)

banco = BancoTxt()
salvar_usuario_interface(banco, 'usuario' , 'senha' , 'email')

