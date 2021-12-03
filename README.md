
### Informações para Teste

Para utilizar o projeto é necessário instalar as dependências, você pode apontar o `pip` para o arquivo `requirements.txt` e instalar as dependências do projeto:

Reslizar clone do projeto

### Criar venv (Ambiente virtual)
```
# python -m venv venv
```

### Ativar venv
```
# source venv/bin/activate
```

### Instalar dependências do projeto
```
# pip install -r requirements.txt
```

### Executar migrações
```
# python manage.py makemigrations
```
```
# python manage.py migrate
```
 
### Carregar Dados existentes (usuários, Publicações, Categorias e outros...)
```
# python manage.py loaddata db.json
```
 

