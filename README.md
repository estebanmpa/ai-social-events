# Sistema de Suscripciones a Cuentas Públicas y Listado de Eventos
## Frontend WebApp
### Parte pública (/)
- Landing page explicando:
    - Qué hace la app.
    - Cómo se seleccionan cuentas.
- Privacidad: “No accedemos a tu cuenta de Instagram”.
- Botón para login con Google.

### 🔐 Parte privada (/dashboard)
#### ✅ Funcionalidades
1. Buscador de cuentas públicas → agregar a favoritos
- Usar Google Programmable Search Engine (CSE) incrustado en tu app.
- O usar tu propia base con autocompletado (más adelante).

2. Lista de cuentas favoritas del usuario.
3. Mostrar eventos detectados:
- Feed ordenado por fecha próxima.
- Mostrar: título estimado, fecha, link al post, cuenta origen.

## 🔧 Backend
### ✅ Autenticación
- Login con Google (OAuth).
- Guardar en base de datos: user_id, email, name, picture.
### ✅ Scraper (ejecutado 1x por día, tipo cronjob)
### 🧠 Procesamiento de eventos (NLP)
#### 🔍 Qué buscar en los captions:
- Fechas futuras: “15 de julio”, “este sábado”, “viernes 12”, etc.
- Palabras clave: “show”, “evento”, “entradas”, “tocamos en”, “charla”, etc.