# Sistema de Gerenciamento de Clínicas

Trabalho da disciplina INE5605 - Desenvolvimento de Sistemas Orientados a Objetos I

Curso de Sistemas de Informação - UFSC

**Autores:** Guilherme Ricci Machado Villela e Lucas Keller da Silva

---

## Sobre o sistema

Sistema orientado a objetos em Python para gerenciamento de clínicas de saúde, desenvolvido seguindo o padrão arquitetural MVC (Model-View-Controller) e utilizando o padrão DAO para persistência de dados em arquivos (`.pkl`).

O sistema possui interface gráfica construída com `FreeSimpleGUI` e permite:
- Cadastro de clínicas, pacientes, profissionais de saúde e tipos de atendimento.
- Registro de atendimentos (consultas, exames, retornos), procedimentos realizados e pagamentos.
- Emissão de relatórios gerenciais.
- Salvamento automático de todos os registros e relacionamentos (Persistência em Arquivo).

---

## Requisitos

- Python 3.8 ou superior
- `FreeSimpleGUI` (interface gráfica)

Para usuários de Linux (Ubuntu/Debian/Mint), é necessário instalar o pacote `python3-tk` no sistema para que a interface gráfica funcione:
```bash
sudo apt update
sudo apt install -y python3-tk python3-venv
```

---

## Como configurar e executar

Siga os passos abaixo para rodar o projeto na sua máquina local de forma segura utilizando um ambiente virtual (venv):

1. **Clone o repositório e acesse a pasta do projeto**:
```bash
git clone <URL_DO_REPOSITORIO>
cd clinica-oop
```

2. **Crie um ambiente virtual (venv)**:
```bash
python3 -m venv .venv
```

3. **Ative o ambiente virtual**:
- No Linux/macOS:
  ```bash
  source .venv/bin/activate
  ```
- No Windows:
  ```cmd
  .venv\Scripts\activate
  ```

4. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

5. **Execute o sistema**:
```bash
python main.py
```
