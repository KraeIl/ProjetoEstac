from Login import *
from DBManager import *
import MenuPrincipal

#banco = DBManager()
#banco.popular_tabela("root", "m", 1, 1)
#login = Login()
banco = DBManager()
menu = MenuPrincipal.GUIMenuPrincipal('Cesar')
banco.close()


