# Registro de uso de IA: Parte A (configuración y seguridad)

Integrante: Angelo Vidal
Herramienta: Claude Code (modelo Claude Opus 5.5), usado en la terminal sobre el proyecto local.

## Qué hizo cada uno

- **Claude:** revisó el proyecto y las guías; editó `config/settings.py`, `config/urls.py`,
  `productos/api_urls.py`, `requirements.txt` y `README.md`; creó `.env`; aplicó
  migraciones; hizo pruebas automáticas; redactó los commits, el PR #3 y la revisión del PR #4.
- **Angelo:** instaló y configuró PostgreSQL con los comandos entregados; creó los
  usuarios de prueba; probó el token en Postman; decidió qué cambios aceptar, cuándo
  abrir el PR y qué correo usar; rehízo el commit del PR #3; publicó la revisión del PR #4.

## Iteración 1: la base de datos no arrancaba

- **Problema inicial:** el proyecto no conectaba porque no estaba instalado el servidor
  PostgreSQL y faltaba el archivo `.env`.
- **Prompt:** «comenzemos la etapa A».
- **Respuesta recibida:** revisión del proyecto y comandos para instalar y configurar PostgreSQL.
- **Decisión:** aceptado.
- **Verificación:** conexión a la base `tienda_hardware`, migraciones aplicadas, 10 productos
  cargados y el catálogo visible en el navegador.
- **Aprendizaje y riesgos:** Django no crea la base de datos ni instala el servidor: hay que tener PostgreSQL corriendo y la base creada antes de migrar. Riesgo: tras reiniciar el equipo, PostgreSQL no arranca solo y el sitio falla con un error de conexión que parece de código.

## Iteración 2: claves expuestas

- **Problema inicial:** al preguntar si la clave de la base de datos era pública, se comprobó que
  no estaba en GitHub, pero el repositorio público sí tenía la `SECRET_KEY` real en `settings.py`.
- **Prompt:** «lo de tu_clave esta expuesta a nivel publico? , quieres dejar todo publico en .env?».
- **Respuesta recibida:** explicó la diferencia entre ambos casos y recomendó leer `SECRET_KEY`,
  `DEBUG` y `DB_USER` desde `.env`.
- **Decisión:** aceptado («haz lo que mejor recomiendes»). Es un cambio adicional a la guía.
  También se cambió la contraseña de PostgreSQL.
- **Verificación:** las líneas añadidas al commit no contienen secretos. La clave antigua sigue
  en el historial de git, pero ya no se usa.
- **Aprendizaje y riesgos:** Un archivo `.env` solo protege lo que nunca se subió: una clave que ya está en el historial de un repositorio público debe considerarse comprometida y cambiarse. Riesgo: pegar contraseñas en el chat con la IA también las expone, aunque no lleguen a GitHub.

## Iteración 3: usuario sin contraseña

- **Problema inicial:** `usuario_normal` quedó sin contraseña utilizable después de crearlo en el Admin.
- **Detección:** una consulta a la base de datos hecha por Claude.
- **Solución:** `python manage.py changepassword usuario_normal`.
- **Verificación:** Postman respondió 200 al pedir el token con ese usuario.
- **Aprendizaje y riesgos:** Crear un usuario en el Admin no siempre deja una contraseña utilizable; hay que comprobar que puede pedir el token antes de usarlo en las pruebas. Riesgo: confundir un error de credenciales con un error de configuración de JWT.

## Iteración 4: los commits no aparecían a mi nombre

- **Problema inicial:** los commits usaban un correo no vinculado a la cuenta de GitHub.
- **Prompt:** «en github quiero salir como contributor».
- **Respuesta recibida:** cambiar el correo global de git y rehacer el commit del PR.
- **Corrección de la IA:** GitHub no tiene un rol de «asistente»; Claude figura como coautor
  mediante la línea `Co-Authored-By`.
- **Verificación:** la API de GitHub vincula el commit a la cuenta `Angelo-Vidal`.
- **Aprendizaje y riesgos:** GitHub atribuye los commits por el correo configurado en git, no por la sesión iniciada. Riesgo: la IA puede describir funciones que no existen (el rol de «asistente»), por eso hay que verificar lo que afirma.

## Iteración 5: revisión del PR #4 y README

- **Problema inicial:** había que revisar el CRUD de B y actualizar el README, que todavía
  describía la API como trabajo futuro.
- **Prompt:** «sí, escribe el comentario del PR #4 y adelanta el README».
- **Respuesta recibida:** un borrador de revisión que aprueba el serializer, el viewset y las rutas,
  y pide agregar `create()` para que el POST responda `{"mensaje": "Registro creado", ...}`
  como indica la pauta. También corrigió la instalación del README y agregó la sección «API REST».
- **Decisión:** aceptado. Angelo publicó la revisión pidiendo cambios.
- **Verificación:** se comparó el PR con el modelo `Producto` y con la guía de la Parte B. El
  código del PR no se ejecutó en local; los códigos 201 y 403 de la tabla se comprueban en las pruebas.
- **Aprendizaje y riesgos:** Revisar un PR no es solo leer el código: hay que contrastarlo con el modelo y con lo que pide la pauta. Riesgo: aprobar sin ejecutar el código deja errores sin detectar; por eso los códigos de respuesta se comprueban en las pruebas.

## Iteración 6: pruebas 3 a 7 y 403 en Postman

- **Problema inicial:** había que hacer las pruebas del CRUD con token y dejar evidencia en Admin y PostgreSQL.
- **Prompt:** «que paso quedamos en el 5» (para retomar la prueba 5 tras cambiar de sesión).
- **Respuesta recibida:** instrucciones paso a paso para cada petición en Postman y para las capturas.
- **Decisión:** aceptado. Angelo hizo cada petición y cada captura.
- **Verificación:** la IA consultó PostgreSQL en cada paso: el PATCH dejó precio 12990.00 y stock 5,
  el DELETE dejó 0 filas y el 403 no creó ningún producto (siguieron 10).
- **Aprendizaje y riesgos:** Un 404 en el PATCH no era un error de la API: el producto 12 ya no existía y la base mostró que el de prueba era el 13. Riesgo: una captura puede mostrar una contraseña (pasó con la de `usuario_normal`), así que se revisa cada una antes de subirla y se cambia la clave.

## Iteración 7: estilos e imágenes del sitio

- **Problema inicial:** el catálogo HTML se veía sin estilos.
- **Prompt:** «podemos agregarle un css mas bonito, por que esta feo» y luego «agregale imagenes de internet
  para ver visualmente que estoy viendo , la iamgen que sea hd».
- **Respuesta recibida:** CSS en `base.html` y un campo opcional `imagen_url` en `Producto`, con migración,
  fixture, formulario y catálogo. Angelo eligió el campo en el modelo y fotos del modelo exacto.
- **Decisión:** aceptado. No lo pide la guía; es un extra.
- **Verificación:** vista previa del catálogo, `manage.py check` sin errores y la API sin cambios, porque el
  serializer no incluye `imagen_url`.
- **Aprendizaje y riesgos:** Agregar un campo al modelo obliga a crear una migración y a actualizar el fixture para que otro integrante vea lo mismo al clonar. Riesgo: las imágenes se cargan desde otros sitios y pueden dejar de funcionar; una de LG no cargaba y hubo que cambiarla.

## Errores de la IA detectados

- Aconsejó guardar la petición en Postman y después lo corrigió, porque esa petición podía
  sincronizar la contraseña con la nube.
- Pidió cambiar la clave de ejemplo de la base de datos y luego la copió sin cambiar al `.env`;
  después la reemplazó por una aleatoria.
- Primero recomendó esperar a B para abrir el PR y luego recomendó abrirlo antes.
- Indicó ejecutar el comando de revisión en el chat con el prefijo `!`, pero se pegó en la terminal,
  fuera de la carpeta del proyecto, y falló. Se corrigió agregando `-R` con el repositorio.
- Al retomar en una sesión nueva dio un estado desactualizado (dijo que faltaban las pruebas ya
  empezadas) hasta revisar la sesión anterior.
- Usó una imagen de LG que no cargaba en el navegador; se reemplazó por otra.
