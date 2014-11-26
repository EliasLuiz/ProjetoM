from PyQt4 import QtGui


'''
Modulo que gerencia janelas de arquivos
'''
        
def pickDirectory():
    #retorna o diretorio selecionado pelo usuario
    return QtGui.QFileDialog.getExistingDirectory(caption="Escolha o diretorio");
    
def pickFile(extensions=""):
    #retorna o arquivo selecionado pelo usuario
    #extensions = extensoes aceitaveis. Ex: Images (*.png *.xpm *.jpg);;Text files (*.txt)
    return QtGui.QFileDialog.getOpenFileName(caption="Escolha o arquivo", filter=extensions);
