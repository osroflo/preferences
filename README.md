# Preferences
Personal preferences, scripts and more to make manual tasks or fresh installations easier to manage.

### Scripts 
This folder contains python scripts to automate manual tasks, like virtual host creation.

### Dependency management
This folder contains my personal composer management script to install the most common dependencies in my projects.

### Code editor
This folder contains the most common settings for my personale preferences. For example, sublime text.
 
### OS
This folder contains settings to trick the OS.


### Setup Dev Env
```
sudo apt-get install git git-core


```


## Terminal

### Oh My Zshell

```bash
# install zshell
sudo apt-get instsall zsh

wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh

chsh -s `which zsh`

sudo shutdown -r 0

# references:
# - https://www.computersnyou.com/3145/setup-zsh-oh-zsh-linux-mint-quick-guide/
# - https://gist.github.com/tsabat/1498393
```



### Tilix

```bash
# fedora
sudo apt-get install tilix

# setup config
mkdir -p ~/.config/tilix/themes


# install themes
git clone https://github.com/storm119/Tilix-Themes

# copy
cp Tilix-Themes/Themes-2/*  ~/.config/tilix/themes/
cp Tilix-Themes/Themes/*  ~/.config/tilix/themes/


# prefered themes
Elemental
Later This Evening
Expresso Libre
Earthsong
Dimmed Monokai
```