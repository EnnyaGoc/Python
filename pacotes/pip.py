#Pip o um gerenciador de pacodes do python, q permite instalar, atualizar e remover pacotes facilmente

#pip install numpy
#pip uninstall numpy
#pip list - mostra todos os pacotes instalados

#------------------------
#ambiente virtual

#python3 -m venv nomedoproj
#source nomedoproj/bin/activate    para ativar

#deactivate para desativar

#------------------------------
#principais comandos do pip


#pip install numpy

#pip uninstall numpy

#pip list

#pip list --upgrade nomePacote - para atualizar

#pip search termo_de_busca


#--------------------------------------------------------
#pipenv - ferramenta para gerenciar pacotes q combina gestao de dependencias cm criaçao de amb virtual

#pip install pipenv
#pipenv install numpy
#pipenv uninstall numpy
#pipenv lock 
#pipenv graph - lista todas as dependencias


#-------------------------------------------------------------

#poetry - outra q permite declarar bibliotecas q seu proj depende e gerencia elas p vc

#pip install poetry
#poetry new myproject
#cd myproject
#poetry add numpy
#poetry remove numpy
