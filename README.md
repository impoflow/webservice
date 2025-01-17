# Webservice

Este repositorio contiene una aplicación web que proporciona servicios específicos a través de una arquitectura cliente-servidor.

## Estructura del Proyecto

- **client/**: Contiene el código fuente del cliente que interactúa con el servidor para consumir los servicios ofrecidos.
- **server/**: Incluye el código fuente del servidor que maneja las solicitudes entrantes y proporciona las respuestas adecuadas.
- **.github/workflows/**: Contiene configuraciones para la integración y despliegue continuo utilizando GitHub Actions.
- **docker-compose.yml**: Archivo de configuración para orquestar los servicios del cliente y servidor utilizando Docker Compose.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal utilizado para el desarrollo del servidor.
- **JavaScript**: Utilizado en el lado del cliente para la interacción y dinamismo de la aplicación.
- **Docker**: Facilita la contenedorización y despliegue de la aplicación.
- **GitHub Actions**: Implementado para la integración y despliegue continuo.

## Requisitos Previos

- **Docker**: Asegúrese de tener Docker instalado en su sistema para ejecutar la aplicación en contenedores.
- **Docker Compose**: Necesario para orquestar múltiples contenedores de Docker.

## Cómo Empezar

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/impoflow/webservice.git
   cd webservice
   ```

2. **Iniciar los servicios con Docker Compose**:

   ```bash
   docker-compose up --build
   ```

   Este comando construirá y levantará los contenedores definidos en `docker-compose.yml`.

3. **Acceder a la aplicación**:

   Una vez que los contenedores estén en funcionamiento, puede acceder a la aplicación cliente en `http://localhost:3000` y al servidor en `http://localhost:8000`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, siga los siguientes pasos:

1. **Fork** el repositorio.
2. Cree una nueva rama para su función o corrección de errores: `git checkout -b feature/nueva-funcionalidad`.
3. Realice sus cambios y haga commit: `git commit -m 'Agrega nueva funcionalidad'`.
4. Haga push a la rama: `git push origin feature/nueva-funcionalidad`.
5. Cree un **Pull Request** detallando sus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo `LICENSE` para más detalles.

---

*Nota*: Asegúrese de revisar y modificar las configuraciones según sus necesidades específicas antes de desplegar la aplicación en un entorno de producción. 
