# Sistema de Gestión de Cocina — COBOL + Python + FastAPI

Este proyecto implementa un sistema modular de gestión de cocina utilizando **COBOL** como motor principal de datos y **Python/FastAPI** como interfaz moderna de comunicación.  
El objetivo es demostrar una arquitectura realista que combine tecnologías tradicionales y actuales, manteniendo un diseño limpio, extensible y orientado al aprendizaje.

---

## 🚀 Funcionalidades incluidas en la Versión 1.0

La versión inicial del sistema proporciona:

### ✔ Gestión de productos (COBOL)
- Alta y modificación básica de productos.
- Archivo indexado (`PRODUCTOS.DAT`) como almacenamiento principal.

### ✔ Registro de movimientos (COBOL)
- Movimientos de entrada (compras) y salida (consumo).
- Registro en archivo (`MOVIMIENTOS.DAT`).
- Validación de existencia del producto.

### ✔ Cálculo de stock dinámico (COBOL)
- El stock se calcula sumando entradas y restando salidas.
- Programa de listado de stock con informe sencillo.

### ✔ API REST básica (FastAPI)
- `POST /movimientos`: Registro de movimientos desde otros dispositivos.
- `GET /status`: Comprobación del estado del servidor.
- Comunicación Python → COBOL mediante `subprocess` o archivos temporales.

### ✔ Frontend mínimo (HTML)
- Página simple para enviar movimientos a la API.

Estas funciones conforman la primera versión funcional del sistema y sirven de base para futuras ampliaciones.

---

## 🎯 Objetivo del proyecto

El proyecto está diseñado para:

- Practicar **COBOL moderno** mediante ficheros indexados y procesos independientes.
- Integrar COBOL con **Python** usando llamadas a programas externos.
- Implementar un backend ligero con **FastAPI**.
- Explorar arquitecturas híbridas entre tecnologías clásicas y actuales.
- Servir como proyecto demostrable en GitHub.

---

## 🧱 Arquitectura del sistema

### Tecnologías utilizadas
- **COBOL (GnuCOBOL)** → Gestión de datos e informes.
- **Python 3** → Lógica auxiliar.
- **FastAPI** → API REST.
- **HTML/CSS** → Interfaz visual mínima.
- **Archivos indexados** → Almacenamiento principal de datos (sin SQL).

### Estructura del repositorio

backend/
api/
main.py # API FastAPI
cobol/
ALTA_PRODUCTO.cbl # Alta y modificación de productos
MOVIMIENTO_STOCK.cbl # Registro de entradas/salidas
LISTAR_STOCK.cbl # Cálculo e informe de stock
python_services/
cobol_bridge.py # Comunicación Python ↔ COBOL

data/
PRODUCTOS.DAT # Archivo indexado de productos
MOVIMIENTOS.DAT # Archivo de movimientos

mobile_app/
index.html # Frontend mínimo para registrar movimientos

tablet_app/
(futuro uso)

docs/
VERSION_1.0.md # Documentación de la versión inicial
roadmap.md # Futuras versiones (opcional)


---

## 🔄 Flujo de funcionamiento

### 1. Alta de producto (COBOL)
El usuario ejecuta un programa COBOL que registra productos en `PRODUCTOS.DAT`.

### 2. Registro de movimiento (API REST)
1. Un cliente envía un JSON a `POST /movimientos`.
2. FastAPI procesa la petición.
3. Python invoca un programa COBOL para registrar el movimiento.
4. COBOL actualiza `MOVIMIENTOS.DAT`.
5. Se devuelve la respuesta en JSON.

### 3. Consulta de stock (COBOL)
Un programa independiente calcula el stock dinámico y genera un informe.

---

## 🛠 Próximas versiones (V2+)

Las versiones posteriores introducirán:

- Escaneo de códigos de barras.
- Interfaz móvil/tablet estilo aplicación (PWA).
- Alertas de caducidad.
- Productos habituales y lista automática de compra.
- Sistema de recetas inteligente.
- Módulo de salida específico para tablet.
- Informes avanzados.
- OCR para análisis de tickets de compra.

---

## 📄 Licencia

Pendiente de definir.

---

## 📌 Estado del proyecto

En desarrollo activo.  
La Versión 1.0 establece la base técnica y funcional para ampliar el sistema en fases posteriores.

