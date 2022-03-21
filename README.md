# OnScreen-Ticker-and-Promotions
A Linux Program for On-Screen Advertisements and promotions like shown in News Channels.

## Dependencies are mentioned below. ##

### OS related Dependency ###
1. Linux OS (recommended Ubuntu)
2. Desktop Environment Like `Ubuntu(Gnome/Mate/Lite/etc) - with hidden decorators`, `OpenBOX - with hidden decorators`
3. [![Supported Python Version 3.6+](https://img.shields.io/badge/Python-v3.6+-blue.svg?style=flat-square&logo=python)](https://github.com/AmoghSaxena/OnScreen-Ticker-and-Promotions)

### Tools for Proper working of Ticker ###
* virtualenv 
* pkg-config 
* libcairo2-dev 
* python3-dev 
* gcc 
* libgirepository1.0-dev 
* python3-gi 
* gobject-introspection 
* gir1.2-gtk-3.0

For Ubuntu you can install them with following command:
```shell
sudo apt install -y virtualenv pkg-config libcairo2-dev python3-dev gcc libgirepository1.0-dev python3-gi gobject-introspection gir1.2-gtk-3.0
```
For Other distribution other than Ubuntu can install dependencies with similar commands found. You can refer Internet for same.

## Installation ##

### Procedure to Install this code ###
#### 1. Clone the Repo ####
```shell
$ git clone https://github.com/AmoghSaxena/OnScreen-Ticker-and-Promotions.git ticker
```

#### 2. Change the working directory to cloned directory
```shell
$ cd ticker
```

#### 3. Run `Installation.sh` file ####
If `installation.sh` is already executable then you can directly run it with
```shell
 $ ./installation.sh
```
OR

If `installation.sh` is not executable then you can make it executable and run it with
```shell
$ chmod +x ./installation.sh
$ ./installation.sh
```
> This will create Virtual Environment in the parent directory & Install following pip modules which are required. 
> 
> > ![d](https://img.shields.io/badge/pip-latest-blue.svg?style=flat-square&logo=python)
> > ![d](https://img.shields.io/badge/pygame-2.1.0-blue.svg?style=flat-square&logo=python)
> > ![d](https://img.shields.io/badge/moviepy-1.0.3-blue.svg?style=flat-square&logo=python)
> > ![d](https://img.shields.io/badge/colorama-0.4.4-blue.svg?style=flat-square&logo=python)
> > ![d](https://img.shields.io/badge/PyGObject-3.42.0-blue.svg?style=flat-square&logo=python)

#### 4. Change `config.json` according to your needs
```json
{
   "static_ticker_condition": true,
   "position_static_ticker": "top-left",
   "static_ticker_bgcolor": [
      0,
      0,
      0
   ],
   "static_ticker_logo": true,
   "static_ticker_message": "Yeah!",
   "static_ticker_font_color": "#ffffff",
   "static_ticker_font_size": 40,
   "static_ticker_font": "Ubuntu",
   "main_ticker_condition": true,
   "main_ticker_message": "Multiple commands can be specified a the same time and there\u2019s also a delay that sleeps a certain amount of milliseconds before next command is executed. Here\u2019s an example where select is pressed, followed by left after waiting a second:",
   "main_ticker_logo": true,
   "main_ticker_logo_position": "left",
   "main_ticker_font": "MyriadProFont",
   "main_ticker_bgcolor": [
      255,
      0,
      0
   ],
   "main_ticker_font_color": [
      255,
      255,
      255
   ],
   "main_ticker_speed": "fast",
   "main_ticker_motion": "right-left",
   "optional_ticker_condition": true,
   "optional_ticker_message": "Multiple commands can be specified a the same time and there\u2019s also a delay that sleeps a certain amount of milliseconds before next command is executed. Here\u2019s an example where select is pressed, followed by left after waiting a second:",
   "optional_ticker_font": "MyriadProFont",
   "optional_ticker_bgcolor": [
      255,
      162,
      5
   ],
   "optional_ticker_font_color": [
      0,
      0,
      0
   ],
   "optional_ticker_speed": "fast",
   "optinal_ticker_motion": "left-right",
   "moving_ticker_condition": true,
   "moving_ticker_localtion": "center",
   "moving_ticker_center_size": "small",
   "time_interval": 197
}
```

#### 5. Run the program with ```start_ticker``` file ####
If `start_ticker` is already executable then you can directly run it with
```shell
 $ ./start_ticker
```
OR

If `start_ticker` is already executable then you can directly run it with
```shell
$ chmod +x .start_ticker
$ ./start_ticker
```
> This will create start the ticker and will run till the `"time_interval"` seconds in `config.json`
>
> Example: 
> > "time_interval": 197

> If In Emergency you need to stop the ticker then you can run `stop_ticker`
> 
> <h4 align="center">If `stop_ticker` is already executable then you can directly run it with </h4>
> ```shell
> $ ./stop_ticker
> ```
> <h4 align="center">OR</h4>
> <h4 align="center">If `stop_ticker` is already executable then you can directly run it with </h4>
> ```shell
> $ chmod +x .stop_ticker
> $ ./stop_ticker
> ```