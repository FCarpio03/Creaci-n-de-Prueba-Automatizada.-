# Pruebas Automatizadas de Login

Este proyecto contiene pruebas automatizadas para la funcionalidad de inicio de sesión de la página [The Internet Herokuapp](https://the-internet.herokuapp.com/login).

## Historias de Usuario

### Historia de Usuario 1: Inicio de Sesión Exitoso
Como usuario registrado, quiero poder iniciar sesión con credenciales válidas para acceder a mi área segura.
- **Criterio de aceptación:** El sistema debe permitir el acceso y mostrar un mensaje de éxito.
- **Criterio de rechazo:** El sistema no permite el acceso o no muestra el mensaje de éxito.

### Historia de Usuario 2: Validación de Usuario
Como sistema de seguridad, quiero validar las credenciales de los usuarios para evitar accesos no autorizados.
- **Criterio de aceptación:** El sistema debe rechazar el acceso con un nombre de usuario incorrecto y mostrar un mensaje de error.
- **Criterio de rechazo:** El sistema permite el acceso con un nombre de usuario incorrecto o no muestra un mensaje de error claro.

### Historia de Usuario 3: Validación de Contraseña
Como usuario registrado, quiero recibir retroalimentación clara cuando ingrese una contraseña incorrecta.
- **Criterio de aceptación:** El sistema debe mostrar un mensaje específico cuando la contraseña es incorrecta.
- **Criterio de rechazo:** El sistema no diferencia entre problemas de usuario y contraseña o muestra mensajes genéricos.

### Historia de Usuario 4: Validación de Campos Obligatorios
Como sistema de validación, quiero verificar que todos los campos obligatorios estén completos antes de procesar un inicio de sesión.
- **Criterio de aceptación:** El sistema debe mostrar un mensaje de error cuando no se completan los campos.
- **Criterio de rechazo:** El sistema procesa el formulario incompleto sin avisar al usuario.

### Historia de Usuario 5: Funcionalidad de Cierre de Sesión
Como usuario autenticado, quiero poder cerrar mi sesión para proteger mi cuenta cuando termine de usar el sistema.
- **Criterio de aceptación:** El sistema debe permitir cerrar sesión y mostrar un mensaje de confirmación.
- **Criterio de rechazo:** El sistema no proporciona una forma de cerrar sesión o no muestra confirmación.

## Configuración del Entorno

### Requisitos
- Python 3.7 o superior
- Chrome instalado en el sistema

### Instalación
1. Clonar este repositorio
2. Instalar las dependencias: