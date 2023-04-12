# Instalación del plugin de ZSH
La instalación del plugin de Docker en Zsh puede variar dependiendo del método que se utilice para instalar Zsh en tu sistema operativo. A continuación, se describe el proceso de instalación en sistemas operativos basados en Linux:

1. Abre una terminal y asegúrate de tener instalado Zsh en tu sistema y el gestor de paquetes Oh My Zsh. 
2. Ahora, abre el archivo de configuración de Zsh en un editor de texto. Puedes hacerlo ejecutando el siguiente comando en la terminal:

   ```
   vim ~/.zshrc
   ```

3. Busca la línea que comienza con `plugins=` y agrega `docker` al final de la lista de plugins separados por espacios. Debe quedar algo como esto:

   ```
   plugins=(git docker)
   ```

4. Guarda los cambios y cierra el archivo.

5. Ahora, reinicia Zsh para que los cambios tengan efecto:

   ```
   source ~/.zshrc
   ```

Una vez completados estos pasos, el plugin de Docker debería estar instalado y listo para usarse en Zsh. Puedes probarlo ejecutando un comando de Docker en la terminal.

## Otros plugins
Aparte del plugin oficial de Docker, hay varios otros plugins que puedes instalar en Zsh para trabajar con Docker. Algunos de los plugins más populares son:

- **zsh-autosuggestions-docker**: Este plugin agrega sugerencias automáticas para comandos de Docker en Zsh. Puedes instalarlo utilizando el siguiente comando:

   ```
   git clone https://github.com/hlissner/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
   ```

- **zsh-completion-docker**: Este plugin agrega completado de tabulación para comandos de Docker en Zsh. Puedes instalarlo utilizando el siguiente comando:

   ```
   git clone https://github.com/docker/cli.git ~/.oh-my-zsh/custom/plugins/zsh-completion-docker
   ```

- **zsh-syntax-highlighting-docker**: Este plugin agrega resaltado de sintaxis para comandos de Docker en Zsh. Puedes instalarlo utilizando el siguiente comando:

   ```
   git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting-docker
   ```

Para utilizar estos plugins, debes agregarlos a la lista de plugins en el archivo de configuración de Zsh (`~/.zshrc`) de la misma manera que se agregó el plugin de Docker. Por ejemplo:

```
plugins=(git docker zsh-autosuggestions zsh-completion-docker zsh-syntax-highlighting-docker)
```

Igual que antes y una vez que hayas agregado estos plugins, reinicia `zsh` para que los cambios tengan efecto. Luego, podrás utilizar las funciones adicionales que ofrecen estos plugins para trabajar con `docker` en `zsh`.