# Cuenta un chiste
[[MIT License](https://github.com/jvt1963/contar-chistes/blob/master/LICENSE)

Esto es una acción de Snips programada en Python y es compatible con `snips-skill-server`.

## Instalación
### Prerrequisitos

Debes añadir la skill "cuenta un chiste" en tu asistente. Está disponible en [la consola de Snips](https://console.snips.ai)

### SAM
Para instalar la acción en tu dispositivo, puedes usar [Sam](https://snips.gitbook.io/getting-started/installation)

`sam install action -g https://github.com/jvt1963/contar-chistes.git`

### Manualmente

Copia este repositorio manualmente en tu dispostivo, en la carpeta `/var/lib/snips/skills/`
Se necesita `snips-skill-server` instalado en la pi

`sudo apt-get install snips-skill-server`

Parar snips-skill-server & generar el entorno virtual
```
sudo systemctl stop snips-skill-server
cd /var/lib/snips/skills/contar-chistes/
sh setup.sh
sudo systemctl start snips-skill-server
```

## Cómo usar la acción

`Hey Snips`

`Cuenta un chiste`
`Di una gracia`
`Cuenta algo gracioso`
`Quiero reír`
`Cuenta algo para reír`

## Logs
Muestra los logs de snips-skill-server con sam:

`sam service log snips-skill-server`

O en el dispositivo:

`journalctl -f -u snips-skill-server`

Comprueba los logs generales de la plataforma:

`sam watch`

O en el dispositivo:

`snips-watch`
