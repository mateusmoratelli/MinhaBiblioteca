from argparse import Action
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

import screen.generated.screen_cadastro_temas as uiTemas
import database.crud.tema as crud_temas
 



class CadastrarTemas(uiTemas.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.editar = False
        self.inicializar_tela()
        self.definir_acoes_botoes()
        self.carregar_lista_temas()
        self.valores_iniciais()
    


    def inicializar_tela(self):
        self.ui = uiTemas.Ui_Form()
        self.ui.setupUi(self)
    


    def definir_acoes_botoes(self):
        self.ui.btExcluirTema.clicked.connect(self.acao_excluir_tema)
        self.ui.btSalvarTema.clicked.connect(self.acao_salvar_tema)
        self.ui.lstTemas.clicked.connect(self.acao_pegar_item_selecionado)



    def valores_iniciais(self):
        self.ui.lbStatus.setText("")



    def carregar_lista_temas(self):
        self.texto_item = "" # para não encontrar nada na pesquisa
        self.ui.txtTema.setText("")
        self.ui.lstTemas.clear()
        self.ui.itemSelected = False
        # busca na base de dados
        lst = crud_temas.get_all_tema(0, 999999)
        # print(lst)
        for i in lst:
            self.ui.lstTemas.addItem(i.tema)



    def acao_pegar_item_selecionado(self):
        item = self.ui.lstTemas.currentItem()
        if item is not None:
            # Pega o texto do item selecionado
            self.texto_item = item.text()
            self.ui.txtTema.setText(self.texto_item)
            self.ui.itemSelected = True
        else:
            self.texto_item = ""
        self.ui.lbStatus.setText(f"Item selecionado: {self.texto_item}")



    def acao_excluir_tema(self):
        self.ui.lbStatus.setText("")
        if self.ui.itemSelected:
            # Exibe uma mensagem de confirmação
            resposta = QtWidgets.QMessageBox.question(
                self,
                "Confirmar Exclusão",
                f"Tem certeza de que deseja excluir '{self.texto_item}'?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )

            # Verifica a resposta do usuário
            if resposta == QtWidgets.QMessageBox.Yes:
                # Remove o item selecionado
                id = crud_temas.search_tema_by_name(self.texto_item)[0].id
                deleted = crud_temas.delete_tema(id)
                print(f"\nItem {deleted} deletado com sucesso.\n")
                self.carregar_lista_temas()
                self.ui.lbStatus.setText(f"O Tema '{deleted.tema}' foi excluído.")



    def acao_salvar_tema(self):
        nome_novo_tema = str(self.ui.txtTema.text())
        self.ui.lbStatus.setText("")
        db_tema = crud_temas.get_tema_by_name(self.texto_item)
 
        if nome_novo_tema != "": 
            if db_tema.__len__() == 0:
                lista_salva = crud_temas.create_tema(nome_novo_tema)
            else:
                lista_salva = crud_temas.update_tema(db_tema[0].id,  nome_novo_tema )
            self.carregar_lista_temas()
            self.ui.lbStatus.setText(f"O tema foi salvo com sucesso. ID: {lista_salva.id}")
        else:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Não permitido campo em branco. ")

        
