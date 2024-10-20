# Derckards image reader

A image reader voice controller for feh image reader that try to replicate
Blade Runner Derckard Reader. 

>[!WARNING]
> This is an Alpha, please report issues on the 
> Issues page.


| Dependencies |
|----------------|
| [feh](https://feh.finalrewind.org/) |
| [poetry](https://python-poetry.org/) |

Now you are good to go! 

## How to use it? 

```
git clone git@github.com:dg2003gh/derckards-image-reader.git 
cd derckards-image-reader 
poetry update 
poetry shell 
python src/main.py
```


## Commands 

> [!TIP]
> Say one command after the other to go by laterals, just like "right up".

Here are the current available commands:
| Command list | Description |
|--------------|-------------|
| open [Image] | Opens a image|
| close  | Closes the image |
| zoom in | Zoom in the image |
| left, right, up, down| Directionals for the image |
| next, previous | Go to next and previous image |
| exit | exits the program |



