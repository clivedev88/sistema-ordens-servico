# Sistema de Ordens de Serviço

Este é um sistema de gestão de ordens de serviço desenvolvido com Django. O projeto inclui:

- Cadastro e login de usuários.
- Criação, edição e exclusão de ordens de serviço.
- Geração de relatórios em PDF.
- Interface responsiva utilizando Bootstrap.

## Tecnologias Utilizadas
- **Python** e **Django** para backend.
- **Bootstrap** para estilização.
- **ReportLab** para geração de relatórios.

## Como Executar o Projeto

### Pré-requisitos
- Python 3.10+
- Virtualenv
- Git

### Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-ordens-servico.git
   cd sistema-ordens-servico

2. Crie e ative o ambiente virtual:
 ```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Execute as migrações e inicie o servidor:
```bash
python manage.py migrate
python manage.py runserver
```


## Screenshots

![image](https://github.com/user-attachments/assets/f39297c9-7605-4590-bf27-2330e1b657d4)

![image](https://github.com/user-attachments/assets/f9be682b-a63c-4ea3-83b9-43ed4a0be586)

## Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests.
