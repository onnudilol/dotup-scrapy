# About
dotup-scrapy is the next generation of dotup scrapers

# Usage
Start the scraper by running:

```python

scrapy crawl {dotup, dotup_light} -o foo.json

```

Output the URLs in the json to a txt file by running dl_links.py:

````sh
usage: dl_links.py [-h] [--input-json INPUT_JSON] [--output OUTPUT]
                   [--mode {default,light}]

Output txt file from json to download with wget.

optional arguments:
  -h, --help            show this help message and exit
  --input-json INPUT_JSON, -i INPUT_JSON
                        The json file input.
  --output OUTPUT, -o OUTPUT
                        The txt file output.
  --mode {default,light}, -m {default,light}
                        The function mode.
```