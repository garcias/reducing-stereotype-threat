# reducing-stereotype-threat

This web site is intended as a study tool to learn more about the phenomenon of stereotype threat. It presents articles and an annotated bibliography recovered from the Wayback Machine's archive of the website `reducingstereotyperhreat.org`, through a simple and minimally distracting interface. Use it for self-study, training, workshops, and discussion groups.

[Try out the archive.](https://garcias.github.io/reducing-stereotype-threat)

Want the back story? Read [content/about/history.md](content/about/history/md).

Want the original RST website (2018 and later)? It is back online at [www.reducingstereotypethreat.org](http://www.reducingstereotypethreat.org)! It can be a bit slow, is served over HTTP, and visually dense; if those are problems for you and you don't need the latest articles, [this archive](https://garcias.github.io/reducing-stereotype-threat) should be good enough. 

Wondering how the data were recovered? [See this GitHub repo for the story and the code.](https://github.com/garcias/rst-archive)

Design based on the Hyde-Hyde theme at [https://github.com/htr3n/hyde-hyde](https://github.com/htr3n/hyde-hyde). Add it to `/themes` using `git submodule add https://github.com/htr3n/hyde-hyde`.

## How to use the source

The recovered data are in `data/bibliography.json` and `data/topics.json`. Run the script `gen.py` to generate the corresponding Hugo markdown files in `content/`. To build, remove `docs/` and run `hugo` to regenerate static files; then push to GitHub, which is set to serve from `docs/`.

```bash
    python gen.py
    rm -rf docs/
    hugo
    git push origin master
```
