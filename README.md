# Mangadex Downloader
a simple mangadex Downloader

## How to use it
```bash
python3 mangadx.py -u <url> -d <dir_name>
```
example: `python3 mangadx.py -u "https://mangadex.org/chapter/4278484c-d3aa-4b5a-9161-a522945c018d" -d "GTO ch200.1"`
## For Linux 
Clone this reop, 
```bash
cd mangadx
cp mangadx.py ~/.local/bin
```
create an alias `alias mangadx="python3 ~/.local/bin/mangadx.py"`
and run 
```bash
mangadx -u <url> -d <dir_path>
```
example: `mangadx -u "https://mangadex.org/chapter/4278484c-d3aa-4b5a-9161-a522945c018d" -d "GTO ch200.1"`

### Fot help 
```bash
mangadx.py -h 
```

