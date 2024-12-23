# Proyecto: Sistema de Autenticación Distribuido

Este proyecto implementa un sistema básico de autenticación distribuido utilizando tres tecnologías principales: .NET, FastAPI, y Vue.js. Cada componente tiene una función específica y se comunica con los demás para proporcionar un flujo seguro de autenticación.

---

## Estructura del Proyecto

1. **MS Usuarios (UserService/.NET 8 con gRPC):**

   - Microservicio que gestiona los usuarios.
   - Permite obtener uno o todos los usuarios.
   - Valida credenciales.
   - Expone sus endpoints mediante gRPC.

2. **MS Gestión de Acceso (AccessService/FastAPI):**

   - Valida las credenciales enviadas desde el frontend.
   - Se comunica con el MS Usuarios vía gRPC para verificar las credenciales.
   - Expone un endpoint REST para el frontend.

3. **Frontend (frontend-vue/Vue.js 3.4):**
   - Proporciona una interfaz simple para iniciar sesión.
   - Envía las credenciales al MS Gestión de Acceso vía REST.
   - Muestra mensajes de éxito o error según la respuesta recibida.

---

## Cómo Ejecutar el Proyecto

### 1. **MS Usuarios (UserService/.NET 8 con gRPC):**

- Requisitos:
  - .NET SDK 8.0 o superior.
- Pasos:
  1.  Navega al directorio `UserService`.
  2.  Restaura las dependencias:
      ```bash
      dotnet restore
      ```
  3.  Ejecuta el servicio:
      ```bash
      dotnet run
      ```
  4.  El servicio estará escuchando en `http://localhost:50051`.

### 2. **MS Gestión de Acceso (AccessService/FastAPI):**

- Requisitos:
  - Python 3.12 o superior.
  - Instalar dependencias con `pip`.
- Pasos:
  1.  Navega al directorio `AccessService`.
  2.  Instala las dependencias:
      ```bash
      pip install -r requirements.txt
      ```
  3.  Ejecuta el servicio:
      ```bash
      fastapi dev main.py
      ```
  4.  El servicio estará escuchando en `http://localhost:8000`.

### 3. **Frontend (front-vue/Vue.js 3.4):**

- Requisitos:
  - Node.js 16.x o superior.
  - npm o yarn.
- Pasos:
  1.  Navega al directorio `front-vue`.
  2.  Instala las dependencias:
      ```bash
      npm install
      ```
  3.  Ejecuta el servidor de desarrollo:
      ```bash
      npm run serve
      ```
  4.  La aplicación estará disponible en `http://localhost:5173`.

---

## Funcionalidad Básica

1. El usuario accede al formulario de login en el frontend.
2. El frontend envía las credenciales al MS de Gestión de Acceso vía REST.
3. El MS de Gestión de Acceso valida las credenciales con el MS de Usuarios usando gRPC.
4. Si las credenciales son correctas, se devuelve una respuesta exitosa al frontend; de lo contrario, un mensaje de error.

---

## Tecnologías Utilizadas

- **Backend:**

  - .NET 8 (gRPC para MS Usuarios)
  - FastAPI (Python 3.12 para Gestión de Acceso)

- **Frontend:**

  - Vue.js 3.4 (Composition API)

---

## Contribuciones

Si deseas contribuir, abre un Pull Request o crea un Issue. ¡Toda ayuda es bienvenida!

---
