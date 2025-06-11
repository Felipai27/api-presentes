# API de Presentes

Este projeto fornece uma API REST simples para gerenciar uma lista de presentes, documentada com OpenAPI/Swagger e disponível tanto localmente quanto em ambiente de nuvem (Render).

---

## Visão Geral

* **Nome:** API de Presentes
* **Versão:** 1.0.0
* **Descrição:** CRUD de presentes (criar, listar, buscar, atualizar e remover) em memória.
* **Documentação interativa:** `/docs` (Swagger UI)

---

## Endpoints

### 1. Status da API

* **URL:** `/`
* **Método:** GET
* **Descrição:** Redireciona para a documentação Swagger.

**Exemplo de requisição:**

```bash
curl -i http://<host>/
```

### 2. Listar todos os presentes

* **URL:** `/presentes`
* **Método:** GET
* **Descrição:** Retorna um array com todos os presentes.

**Resposta de Sucesso (200):**

```json
[
  { "id": 1, "nome": "Bicicleta", "preco": 350.0 }
]
```

### 3. Adicionar um novo presente

* **URL:** `/presentes`
* **Método:** POST
* **Descrição:** Cria um novo presente em memória.
* **Request Body:**

  ```json
  {
    "nome": "Livro",
    "preco": 45.0
  }
  ```

**Resposta de Sucesso (201):**

```json
{ "id": 2, "nome": "Livro", "preco": 45.0 }
```

### 4. Buscar presente por ID

* **URL:** `/presentes/{id}`
* **Método:** GET
* **Parâmetros de Rota:**

  * `id` (integer) — Identificador do presente.

**Resposta de Sucesso (200):**

```json
{ "id": 1, "nome": "Bicicleta", "preco": 350.0 }
```

**Resposta de Erro (404):**

```json
{ "erro": "Presente não encontrado" }
```

### 5. Atualizar presente

* **URL:** `/presentes/{id}`
* **Método:** PUT
* **Parâmetros de Rota:**

  * `id` (integer)
* **Request Body:**

  ```json
  {
    "nome": "Bicicleta Aro 26",
    "preco": 400.0
  }
  ```

**Resposta de Sucesso (200):**

```json
{ "id": 1, "nome": "Bicicleta Aro 26", "preco": 400.0 }
```

### 6. Remover presente

* **URL:** `/presentes/{id}`
* **Método:** DELETE
* **Parâmetros de Rota:**

  * `id` (integer)

**Resposta de Sucesso (200):**

```json
{ "mensagem": "Presente removido com sucesso" }
```

---

## Instalação e Execução Local

1. Clone o repositório:

   ```bash
   git clone https://github.com/Felipai27/api-presentes.git
   cd api-presentes
   ```
2. Crie e ative o ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate    # Linux/macOS
   .\.venv\Scripts\activate   # Windows
   ```
3. Instale as dependências:

   ```bash
   pip install --upgrade pip setuptools wheel
   pip install -r requirements.txt
   ```
4. Execute a aplicação:

   ```bash
   python app.py
   ```
5. Acesse no navegador:

   * API root: `http://127.0.0.1:5000/` (redireciona para docs)
   * Documentação: `http://127.0.0.1:5000/docs`

---

## Deploy em Produção (Render)

1. Push no GitHub: sua branch `main` contém o código atualizado.
2. Crie um **Web Service** no Render:

   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`
3. Aguarde o deploy e teste:

   ```
   https://api-presentes-1.onrender.com
   ```

---

