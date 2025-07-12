# Sistema de Suscripciones a Cuentas Públicas y Listado de Eventos

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Frontend WebApp](#frontend-webApp)
- [Backend](#backend)

## Frontend WebApp
### Parte pública (/)
- Landing page explicando:
    - Qué hace la app.
    - Cómo se seleccionan cuentas.
- Privacidad: “No accedemos a tu cuenta de Instagram”.
- Botón para login con Google.

### 🔐 Parte privada (/dashboard)
- Buscador de cuentas públicas → agregar a favoritos
- Lista de cuentas favoritas del usuario.
- Mostrar eventos detectados:
    - Feed ordenado por fecha próxima.
    - Mostrar: título estimado, fecha, link al post, cuenta origen.

## 🔧 Backend
### ✅ Autenticación
- Login con Google (OAuth).
- Guardar en base de datos: user_id, email, name, picture.
### Busquedas
- Google Programmable Search Engine en conjunto con API Custom JSON para obtener resultados. Se configuró unicamente para instagram.com y se aplican distintos filtros para evitar obtener posts y reels.
### ✅ Scraper (ejecutado 1x por día, tipo cronjob)
### 🧠 Procesamiento de eventos (NLP)
#### 🔍 Qué buscar en los captions:
- Fechas futuras: “15 de julio”, “este sábado”, “viernes 12”, etc.
- Palabras clave: “show”, “evento”, “entradas”, “tocamos en”, “charla”, etc.