# Sublime Text

### Themes
- install package installer https://packagecontrol.io/installation
- install theme https://github.com/equinusocio/material-theme
- install package > colorsublime
- install colorsublime:install theme > earthsong

Change left side color
- install package > Resource Viewer  (used to edit the them configuration files)
- Ctrl+Ship+P Extractk Package > Material Theme
- Open Preferences > Browse packages. 
- Edit the file material theme > Material-Theme.sublime-theme
- Use a color picker to get the RGB background color of the earthsong color. (GPick)
- Look for this section:
```
/* @EMPTY WINDOW
 * Style for empty (no tabs) window
========================================================================= */
"layer0.tint": [54, 49, 44],

```
Replace the rgb color with your own. (ALT+F3 to select all ocurrences).

- To update the TAB backgorund color, open the theme directory: Material Theme/assets/default.
- Edit all tab png with your own background color.

```
"keyframes":
            [
              "Material Theme/assets/default/tab_animation1.png",
              "Material Theme/assets/default/tab_animation2.png",
              "Material Theme/assets/default/tab_animation3.png",
              "Material Theme/assets/default/tab_animation4.png",
              "Material Theme/assets/default/tab_animation5.png",
              "Material Theme/assets/default/tab_animation6.png",
              "Material Theme/assets/default/tab_animation7.png",
              "Material Theme/assets/default/tab_animation8.png",
              "Material Theme/assets/default/tab_animation9.png",
              "Material Theme/assets/default/tab_animation10.png",
              "Material Theme/assets/default/tab_animation11.png",
              "Material Theme/assets/default/tab_animation12.png",
              "Material Theme/assets/default/tab_animation13.png"
            ]
```

### Coding standards
setup PHPCS
- https://github.com/benmatselby/sublime-phpcs

setup phpfmt
- https://github.com/phpfmt/sublime-phpfmt

### User settings
- Go tp preferences > Settings - User 
- Paste the user-settings content
