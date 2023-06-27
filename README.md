# reducing-stereotype-threat

This web site is intended as a study tool to learn more about the phenomenon of stereotype threat. It presents articles and an annotated bibliography recovered from the Wayback Machine's archive of the website `reducingstereotyperhreat.org`, through a simple and minimally distracting interface. Use it for self-study, training, workshops, and discussion groups.

[Try out the archive.](https://garcias.github.io/reducing-stereotype-threat)

Want the back story? Read [about/history.md](/about/history.md).

Wondering how the data were recovered? [See this GitHub repo for the story and the code.](https://github.com/garcias/rst-archive)

Design based on theme [Just-The-Docs](https://github.com/just-the-docs/just-the-docs).

## How to use the source

When setting up for the first time, make sure to clone or submodule the Hyde-Hyde repository to `themes/`.

The recovered data are in `data/bibliography.json` and `data/topics.json`. Run the scripts `convert.py` to generate `data/sources.json` and `data/reviews.json`; and `generate.py` to generate the corresponding markdown files in `sources/` and `reviews/`.

To build in a Jekyll devcontainer, create the following `Gemfile`:

```ruby
source "https://rubygems.org"
gem "jekyll-github-metadata", ">= 2.15"
gem "webrick", "~> 1.7"
gem "just-the-docs"
```

Then install with:

```bash
gem install bundler jekyll
bundle update
bundle exec jekyll serve
```
