## `docs/estado_del_arte.md`
```markdown
# Estado del Arte


Los generadores de contraseñas y gestores de credenciales han evolucionado considerablemente en los últimos años. A continuación se resumen las ideas y herramientas más relevantes relacionadas con este proyecto:


- **Políticas de contraseñas y normativas:** Organizaciones y estándares recomiendan contraseñas largas y la utilización de gestores (por ejemplo, NIST en su guía de autenticación recomienda longitud y facilitar el uso de frases de paso en lugar de reglas arbitrarias de complejidad). Las políticas modernas priorizan longitud y la no reuso.


- **Generadores y managers populares:** Herramientas como LastPass, 1Password, KeePass y Bitwarden ofrecen generación automática de contraseñas con opciones de longitud y tipos de caracteres. Muchos de estos gestores también integran almacenamiento cifrado y sincronización.


- **Passphrases vs contraseñas aleatorias:** Está comprobado que las passphrases (frases compuestas por palabras) pueden ser más fáciles de memorizar y tan seguras como cadenas aleatorias, dependiendo de su entropía. Sin embargo, en entornos donde se requiere integración automática (APIs, scripts, dispositivos), siguen siendo útiles las contraseñas aleatorias con alta entropía.


- **Almacenamiento seguro:** El almacenamiento de contraseñas debe considerarse con extremo cuidado. Guardarlas en texto plano en un archivo es práctico para pruebas y uso local, pero para producción se recomienda cifrado (por ejemplo mediante libs como `cryptography` en Python) o el uso de gestores especializados.


- **Entropía y métricas:** La seguridad de una contraseña se mide por su entropía; contraseñas más largas y con más variedad de caracteres presentan mayor resistencia a ataques. Herramientas académicas y comerciales calculan estimaciones de entropía para evaluar robustez.


**Conclusión del estado del arte:** Este proyecto se ubica en la categoría de herramientas locales de generación de contraseñas. Para aumentar su utilidad y seguridad, se recomienda proporcionar opciones de cifrado para almacenamiento y recomendar integración con gestores de contraseñas cuando se use en producción.
