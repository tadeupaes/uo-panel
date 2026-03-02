# uopanel

Painel Django para gerenciamento de shard ServUO.

## Setup rápido (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py setup_rbac
python manage.py runserver 127.0.0.1:8000
```

## Rotas principais
- `/` dashboard (requer login; redireciona para `/admin/login/`)
- `/admin/` Django Admin
- `/api/telemetry/events/` ingest de eventos via API Key (`X-SERVER-KEY`)
- `/api/telemetry/events/recent/` últimos 200 eventos (somente admin humano)

## Telemetria (Fase 1)

### 1) Criar servidor e gerar chave
```powershell
python manage.py create_server ServUO-Prod
```

### 2) Enviar evento (PowerShell)
```powershell
$API_KEY = "COLE_A_CHAVE_AQUI"
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/api/telemetry/events/" `
  -Headers @{"X-SERVER-KEY"=$API_KEY} `
  -ContentType "application/json" `
  -Body '{"event_type":"player_login","severity":"info","payload":{"player":"Bob"}}'
```

### 3) Enviar evento (curl)
```bash
curl -X POST "http://127.0.0.1:8000/api/telemetry/events/" \
  -H "Content-Type: application/json" \
  -H "X-SERVER-KEY: COLE_A_CHAVE_AQUI" \
  -d '{"event_type":"player_login","severity":"info","payload":{"player":"Bob"}}'
```

### 4) Verificar no admin
- Abra `Telemetry -> Server events` no Django Admin.

## Apps
- accounts
- telemetry
- actions
- agents
- llm
- ui
