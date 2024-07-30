import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import ( QApplication, QMainWindow, QLineEdit, QVBoxLayout,
                               QHBoxLayout, QPushButton, QWidget )


class calculadora (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        
        #Configuração do visor        
        self.visor = QLineEdit()
        self.visor.setReadOnly(True)
        self.visor.setAlignment(Qt.AlignRight)
        self.visor.setFixedHeight(35)

        #layout Principal
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.visor)
        
        #layout dos botões
        layout_botoes = QVBoxLayout()
        layout_linha_superior = QHBoxLayout()
        
        botao_limpar = QPushButton('C')
        botao_limpar.setFixedSize(50,50)
        #local para conectar o signal ao slot
        botao_limpar.clicked.connect(self.limpar_visor)
        layout_linha_superior.addWidget(botao_limpar)
        
        botao_parentese_abrir = QPushButton('(')
        botao_parentese_abrir.setFixedSize(50,50)
        #local para conectar o signal ao slot
        layout_linha_superior.addWidget(botao_parentese_abrir)
        
        botao_parentese_fechar = QPushButton(')')
        botao_parentese_fechar.setFixedSize(50,50)
        #local para conectar o signal ao slot
        layout_linha_superior.addWidget(botao_parentese_fechar)
        
        botao_x2 = QPushButton('X²')
        botao_x2.setFixedSize(50,50)
        #local para conectar o signal ao slot
        layout_linha_superior.addWidget(botao_x2)
        
        layout_botoes.addLayout(layout_linha_superior)
               
        #botões Principais
        botao = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['0','.','=','+']
        ]
        
        for linha in botao:
            layout_linha = QHBoxLayout()
            for texto in linha:
                botao = QPushButton(texto)
                botao.setFixedSize(50,50)
                #layout para conectar ao slot
                botao.clicked.connect(self.on_button_clicked)
                layout_linha.addWidget(botao)
            layout_botoes.addLayout(layout_linha)

        layout_principal.addLayout(layout_botoes)
        
        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)
        
        #Configurar o botão limpar
    def limpar_visor(self):
        self.visor.clear()
        
    def on_button_clicked(self):
        botao = self.sender()
        texto_botao = botao.text()
            
        if texto_botao == '=':
            try:
                expressao = self.visor.text()
                resultado = eval(expressao)
                self.visor.setText( str (resultado) )
            except Exception as e:
                self.visor.setText('Erro')
    
        elif texto_botao == 'x²':
            try:
                expressao = self.visor.text()
                resultado = eval(expressao)**2
                self.visor.setText( str (resultado) )
            except Exception as e:
                self.visor.setText('Erro')

        else:
            self.visor.setText(self.visor.text() + texto_botao)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    #Calculadora 1
    janela1 = calculadora()
    janela1.show()
        
    #Execultar o app calculadora
    sys.exit( app.exec() )