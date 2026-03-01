# uopanel (Fase 0)

Base inicial de um painel web Django para gerenciamento de shard ServUO.

## Pré-requisitos
- Python 3.10+
- PowerShell (Windows)

## Setup (Windows PowerShell)

### 1) Criar e ativar virtualenv
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Instalar dependências
```powershell
pip install -r requirements.txt
```

### 3) Configurar variáveis de ambiente
```powershell
Copy-Item .env.example .env
```
Edite `.env` para ajustar `SECRET_KEY`, `DEBUG` e `ALLOWED_HOSTS`.

### 4) Migrar banco e criar superusuário
```powershell
python manage.py migrate
python manage.py createsuperuser
```

### 5) Configurar RBAC inicial
```powershell
python manage.py setup_rbac
```

### 6) Rodar servidor local
```powershell
python manage.py runserver 127.0.0.1:8000
```

Acesse:
- Dashboard: `http://127.0.0.1:8000/` (protegido por login)
- Admin: `http://127.0.0.1:8000/admin/`

## Apps criados
- `accounts`
- `telemetry`
- `actions`
- `agents`
- `llm`
- `ui`

## Comando de RBAC
O comando `setup_rbac` cria os grupos:
- Owner
- Admin
- GM
- ReadOnly

Execute:
```powershell
python manage.py setup_rbac
```
