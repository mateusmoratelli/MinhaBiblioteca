from PyQt5 import QtWidgets
import screen.generated.screen_cadastro_usuarios as uiUser
# import database.db_setup as dbSetup
import database.crud.usuario as _crudUser


class CadastrarUsuario(uiUser.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.iniciarTela()
        self.defineAcoesBotoes()
        self.carregaListaUsuarios()



    def iniciarTela(self):
        self.ui = uiUser.Ui_Form()
        self.ui.setupUi(self)
        self.ui.lbStatus.setText("Selecione um item ou cadastre um novo.")
    


    def defineAcoesBotoes(self):
        self.ui.btExcluirUsuario.clicked.connect(self.acaoExcluirUsuario)
        self.ui.btSalvarUsuario.clicked.connect(self.acaoSalvarUsuario)
        self.ui.lstUsuarios.clicked.connect(self.acaoPegarItemSelcionado)
    


    def carregaListaUsuarios(self):
        self.textoItem = "" # para não encontrar nada na pesquisa
        self.ui.txtUsuario.setText("")
        self.ui.lstUsuarios.clear()
        self.itemSelected = False
        
        # busca na base de dados
        lst = _crudUser.get_users(0, 999999)
        print(lst)
        for i in lst:
            print(i)
            self.ui.lstUsuarios.addItem(i.nome)



    def acaoPegarItemSelcionado(self):
        item = self.ui.lstUsuarios.currentItem()
        if item is not None:
            # Pega o texto do item selecionado
            self.textoItem = item.text()
            self.ui.txtUsuario.setText(self.textoItem)
            self.itemSelected = True
        else:
            self.textoItem = ""
        self.ui.lbStatus.setText(f"Usuário selecionado: {self.textoItem}")


    def acaoExcluirUsuario(self):
        if self.itemSelected:
            # Exibe uma mensagem de confirmação
            resposta = QtWidgets.QMessageBox.question(
                self,
                "Confirmar Exclusão",
                f"Tem certeza de que deseja excluir '{self.textoItem}'?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )

            # Verifica a resposta do usuário
            if resposta == QtWidgets.QMessageBox.Yes:
                # Remove o item selecionado
                id_usuario = _crudUser.get_user_by_name(self.textoItem).id
                deleted = _crudUser.delete_user(id_usuario)
                print(f"\nItem {deleted} deletado com sucesso.\n")
                self.carregaListaUsuarios()
                self.ui.lbStatus.setText(f"Usuário {self.textoItem} deletado com sucesso.")



    def acaoSalvarUsuario(self):
        nome_novo_usuario = str(self.ui.txtUsuario.text())
        db_usuarios = _crudUser.get_user_by_name(self.textoItem)

        if nome_novo_usuario != "": 
            if db_usuarios == None:
                lista_salva = _crudUser.create_user(nome_novo_usuario)
            else:
                lista_salva = _crudUser.update_user(db_usuarios.id,  nome_novo_usuario )
            print(f"|\n")
            self.ui.lbStatus.setText(f"O Usuário foi salvo com sucesso no banco de dados:  {lista_salva.id}")
            self.carregaListaUsuarios()
        else:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Não permitido campo em branco. ")

        