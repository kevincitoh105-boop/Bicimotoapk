# APK Cuba +53

Este repositorio contiene el parche para adaptar el prefijo telefónico de la aplicación de +86 a +53 y generar una APK firmada mediante GitHub Actions.

## Compilación
1. Sube el archivo original `app-release-latest.apk` a la raíz del repositorio.
2. Abre **Actions** y ejecuta **APK Cuba +53** (o espera al siguiente push).
3. Descarga el artefacto `app-release-cuba53` cuando el trabajo termine correctamente.

La APK resultante se firma con una clave temporal de CI. Por eso puede ser necesario desinstalar la versión anterior antes de instalarla.
