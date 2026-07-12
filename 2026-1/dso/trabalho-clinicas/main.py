"""
main.py - ponto de entrada do sistema de clínicas.
Execute com: python main.py
"""

from control.controladorSistema import ControladorSistema

def main():
    sistema = ControladorSistema()
    sistema.iniciar()

if __name__ == "__main__":
    main()
