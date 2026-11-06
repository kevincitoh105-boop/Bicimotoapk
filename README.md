# APK Cuba +53

Este repositorio adapta el prefijo telefónico de la aplicación de +86 a +53 y permite números cubanos de 8 dígitos que comienzan por 5. También elimina el teléfono chino precargado.

## Descargar e instalar

1. Abre **Releases**: https://github.com/kevincitoh105-boop/Bicimotoapk/releases/tag/cuba53-latest
2. Descarga directamente `app-release-cuba53.apk` (no el código fuente ni el ZIP del artefacto).
3. Instala el APK descargado. Si Android indica conflicto de firma al actualizar, desinstala primero la versión anterior y vuelve a instalar.

## Validaciones automáticas

Cada compilación comprueba la integridad ZIP del APK original y del resultado, la alineación con `zipalign` y la firma con `apksigner`. El APK se publica como archivo directo en Releases y, adicionalmente, como artefacto de Actions sin recomprimir el archivo interno.
