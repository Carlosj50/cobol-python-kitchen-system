# Versión 1.0 — Sistema de Gestión de Cocina (COBOL + Python + FastAPI)

## 1. Objetivo general

La versión 1.0 establece una base funcional del sistema de gestión de cocina, utilizando COBOL como motor principal de datos y Python/FastAPI como interfaz de comunicación. Esta versión se centra en:

- Registrar productos.
- Guardar movimientos de entrada y salida.
- Consultar el stock actual.
- Exponer una API REST básica para registrar movimientos desde otros dispositivos.

El objetivo principal es construir un sistema mínimo pero completo que demuestre la integración real entre COBOL y Python, manteniendo una arquitectura clara, organizada y ampliable.

---

## 2. Alcance funcional

### 2.1. Maestro de productos (COBOL)

Incluye un programa COBOL para gestionar el catálogo de productos en un archivo indexado (`PRODUCTOS.DAT`). Las funciones básicas son:

- Alta de producto.
- Modificación de datos.
- Consulta interna.

Campos incluidos:

- Código de producto.
- Nombre.
- Categoría.
- Unidad (unidad, pack, kg, etc.).

---

### 2.2. Movimientos de stock (COBOL)

Los movimientos representan entradas (compras) y salidas (consumos). Se guardan en `MOVIMIENTOS.DAT`.

Campos:

- Código de producto.
- Tipo de movimiento: `E` (entrada) o `S` (salida).
- Cantidad.
- Fecha (opcional en V1).

Reglas:

- Solo se acepta un movimiento si el producto existe.
- El stock no se almacena directamente; se calcula a partir de los movimientos.

---

### 2.3. Cálculo de stock (COBOL)

El stock se determina mediante:

Stock = SUMA(entradas) - SUMA(salidas)

Incluye un programa COBOL (`LISTAR_STOCK.cbl`) que:

- Recorre `PRODUCTOS.DAT`.
- Calcula stock consultando `MOVIMIENTOS.DAT`.
- Genera un informe por pantalla o archivo.

---

### 2.4. API REST básica (Python + FastAPI)

La API permite registrar movimientos desde dispositivos externos.

Endpoints incluidos:

#### **GET /status**
Devuelve el estado básico del servidor:

```json
{
  "status": "ok",
  "version": "1.0"
}

POST /movimientos

Registra un movimiento de entrada o salida.

Ejemplo de entrada:
{
  "codigo_producto": "ABC123",
  "tipo": "E",
  "cantidad": 3
}
Flujo:

FastAPI recibe la petición.

Python ejecuta un programa COBOL (mediante subprocess o archivo temporal).

COBOL valida y registra el movimiento.

FastAPI devuelve la respuesta en JSON.

En esta versión, la API no genera informes ni cálculos de stock.

2.5. Frontend mínimo

Incluye una página HTML simple para enviar movimientos a la API REST. No se incorpora en esta versión:

Escáner de códigos de barras.

Diseño avanzado.

Funciones específicas para móvil/tablet.

3. Exclusiones de la versión 1.0

Las siguientes funciones se posponen para versiones posteriores:

Escaneo de códigos de barras.

Interfaz móvil/tablet avanzada.

Sistema de recetas.

Alertas de caducidad.

Productos habituales y lista automática de compra.

Módulo de consumo en tablet.

OCR o visión artificial.

Base de datos SQL.

4. Arquitectura técnica
4.1. Componentes principales

COBOL

ALTA_PRODUCTO.cbl

MOVIMIENTO_STOCK.cbl

LISTAR_STOCK.cbl

Archivos de datos:

PRODUCTOS.DAT

MOVIMIENTOS.DAT

Python

FastAPI para exposición de la API REST.

Módulos auxiliares para ejecutar programas COBOL y procesar respuestas.

Estructura de carpetas

backend/
  api/
    main.py
  cobol/
    ALTA_PRODUCTO.cbl
    MOVIMIENTO_STOCK.cbl
    LISTAR_STOCK.cbl
  python_services/
    cobol_bridge.py

data/
  PRODUCTOS.DAT
  MOVIMIENTOS.DAT

mobile_app/
  index.html

docs/
  VERSION_1.0.md

5. Flujos principales
5.1. Alta de producto (COBOL)

Ejecutar ALTA_PRODUCTO.

Introducir datos del producto.

Guardar en PRODUCTOS.DAT.

5.2. Registro de movimiento (API REST)

Enviar JSON a /movimientos.

FastAPI procesa la petición.

Python solicita a COBOL que registre el movimiento.

COBOL actualiza MOVIMIENTOS.DAT.

FastAPI envía la respuesta.

5.3. Consulta de stock (COBOL)

Ejecutar LISTAR_STOCK.

Calcular stock dinámicamente.

Mostrar o guardar el informe.

6. Objetivos de aprendizaje

La versión 1.0 permite practicar:

Programación COBOL con archivos indexados.

Integración COBOL ↔ Python mediante procesos externos.

Desarrollo de APIs modernas con FastAPI.

Separación de responsabilidades en una arquitectura modular.

Estructuración profesional de un proyecto para su publicación en GitHub.

7. Próximas versiones (V2+)

Escaneo de código de barras.

Interfaz PWA para móvil/tablet.

Gestión de caducidades.

Lista automática de compra.

Recetas inteligentes.

Módulo de salida específico para tablet.

Informes avanzados en COBOL.