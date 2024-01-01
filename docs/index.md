# django-greeking

Django template tools for printing filler, a technique from the days of hot type known as greeking

```{contents} Sections
:local:
:depth: 2
```

## Features

Greeking can:

* Generate filler images from [placehold.it](http://placehold.it), [placekitten.com](http://www.placekitten.com) and [Fill Murray](http://www.fillmurray.com/).
* Print pangrams in a variety of languages. A pangram is a phrase that includes every letter of an alphabet.
* Create ``Story``, ``Image``, ``RelatedItem`` and ``Quote`` objects with boilerplate text, URLs and a set of the attributes common to news.
* Print snippets from Lewis Carroll's poem [Jabberwocky](http://en.wikipedia.org/wiki/Jabberwocky).
* Import an list of filler comments for use in greeking [Django's 'contrib' comments app](http://docs.djangoproject.com/en/dev/ref/contrib/comments/).


## Installation

```bash
pip install greeking
```


## Getting started

Before you can use any of the template tags, you have to add the app to the
``INSTALLED_APPS`` your settings.py file, like so:

```python
INSTALLED_APPS = [
    "greeking",
]
```

And then import the library into your template.

```html+django
{% load greeking_tags %}
```

Then you just need to call out the tag you want to use.


## Templatetags

### Placeholder images

All placeholder providers expect a width and height to be provided.

One provider  is [placekitten.com](https://placekitten.com/)

```html+django
{% placekitten 200 200 %}
```

<img src="https://placekitten.com/200/200">


### Pangrams

A pangram is a phrase that includes every letter of an alphabet. It is useful when testing font implementations.

By default, an English pangram is returned.

```html+django
{% pangram %}
```

> The quick brown fox jumps over the lazy dog.

A set of other language are available, including Japanese, Spanish, French and German. They can be called by providing
the language code like so:

```html+django
{% pangram 'de' %}
```

> Falsches Üben von Xylophonmusik quält jeden größeren Zwerg.

Here is the complete list of available languages.

|Code|Language|
|:---|:-------|
|en|English|
|da|Danish|
|de|German|
|el|Greek|
|es|Spanish|
|fr|French|
|ga|Irish|
|he|Hebrew|
|hu|Hungarian|
|is|Icelandic|
|jp|Japanese|
|pl|Polish|
|ru|Russian|
|tr|Turkish|


### L.A. Times ipsum

A set of objects with boilerplate text, URLs and other attributes common to news.

The library can generate ``Story``, ``Image``, ``RelatedItem`` and ``Quote`` objects.

They should be assigned to variables in the template and then printed out as needed.

#### Story objects

```html+django
{% latimes_story as obj %}

<h1>{{ obj.headline }}</h1>
<div>{{ obj.byline }}</div>
```

Which would print out as:

> <h1>This is not a headline</h1>
<div>This is not a byline</div>

Here are all the attributes on a ``Story`` object:

|Name|
|:---|
|slug|
|headline|
|byline|
|pub_date|
|canonical_url|
|kicker|
|description|
|sources|
|credits|
|content|


#### Quote objects

```html+django
{% latimes_quote as obj %}

<q>{{ obj.quote }}</q>
<p> — {{ obj.source }}</p>
```

Which would print out as:

> <q>This is not a quote</q>
<p> — This is not a source</p>


Here are all the attributes on a ``Quote`` object:

|Name|
|:---|
|quote|
|source|


### Jabberwocky

["Jabberywocky"](https://en.wikipedia.org/wiki/Jabberwocky) is a 1871 poem by Lewis Carroll, the author of "Alice in Wonderland." Selections can be printed by using the tag below.
The number of paragraphs can be optionally provided to limit its length. The poem has seven paragraphs in total.

```html+django
{% jabberwocky 3 %}
```

> 'Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.

> "Beware the Jabberwock, my son!
The jaws that bite, the claws that catch!
Beware the Jubjub bird, and shun
The frumious Bandersnatch!"

> He took his vorpal sword in hand:
Long time the manxome foe he sought-
So rested he by the Tumtum tree,
And stood awhile in thought.


### Comments

An object_list of filler comments for use in greeking content for Django's [popular comments application](https://github.com/django/django-contrib-comments).

```html+django
{% greek_comment_list as comment_list %}
{% for comment in comment_list %}
    <div id="c{{ comment.id }}">
            <p>{{ comment.comment }}</p>
            <p>{{ comment.user_name }}</p>
            <p>{{ comment.submit_date|date:"F j, Y" }}</p>
            <p><a href="mailto:{{ comment.user_email }}">{{ comment.user_email }}</a></p>
            <p><a href="{{ comment.user_url }}">{{ comment.user_url }}</a></p>
    </div>
{% endfor %}
```


## Credits

* Pangrams are drawn from [Markus Kuhn](http://www.cl.cam.ac.uk/~mgk25/ucs/examples/quickbrown.txt).
* Comments drawn from the work of giants of our time.


## Other resources

* Repo: [https://github.com/palewire/django-greeking](https://github.com/palewire/django-greeking)
* Issues: [github.com/palewire/django-greeking/issues](https://github.com/palewire/django-greeking/issues)
* Packaging: [pypi.python.org/pypi/django-greeking](https://pypi.python.org/pypi/django-greeking)
* Testing: [github.com/palewire/django-greeking/actions](https://github.com/palewire/django-greeking/actions)

Here is the complete list of available languages.

|Code|Language|
|:---|:-------|
|en|English|
|da|Danish|
|de|German|
|el|Greek|
|es|Spanish|
|fr|French|
|ga|Irish|
|he|Hebrew|
|hu|Hungarian|
|is|Icelandic|
|jp|Japanese|
|pl|Polish|
|ru|Russian|
|tr|Turkish|


```{eval-rst}
.. autofunction:: atcf_data_parser.get_dataframe
.. autofunction:: atcf_data_parser.get_gzipped_url
``````

## Installation

The library can be installed from the Python Package Index with any of the standard Python installation tools.

```bash
pipenv install cpi
```

## Working with Python

Adjusting for inflation is as simple as providing a dollar value followed by the year it is from to  the `inflate` method. By default it is adjusted to its value in the most recent year available using "CPI-U" index recommended as a default by the Bureau of Labor Statistics.

```python
import cpi

cpi.inflate(100, 1950)
1017.0954356846472
```

If you'd like to adjust to a different year, submit it as an integer to the optional `to` keyword argument.

```python
cpi.inflate(100, 1950, to=1960)
122.82157676348547
```

You can also adjust month to month. You should submit the months as `datetime.date` objects.

```python
from datetime import date

cpi.inflate(100, date(1950, 1, 1), to=date(2018, 1, 1))
1072.2936170212768
```

You can adjust values using any of the other series published by the BLS as part of its "All Urban Consumers (CU)" survey. They offer more precise measures for different regions and items.

Submit one of the 60 areas tracked by the agency to inflate dollars in that region. You can find a complete list in [the repository](https://github.com/palewire/cpi/blob/main/data/areas.csv).

```python
cpi.inflate(100, 1950, area="Los Angeles-Long Beach-Anaheim, CA")
1081.054852320675
```

You can do the same to inflate the price of 400 specific items lumped into the basket of goods that make up the overall index.  You can find a complete list in [the repository](https://github.com/palewire/cpi/blob/main/data/items.csv).

```python
cpi.inflate(100, 1980, items="Housing")
309.77681874229353
```

And you can do both together.

```python
cpi.inflate(100, 1980, items="Housing", area="Los Angeles-Long Beach-Anaheim, CA")
344.5364396654719
```

Each of the 7,800 variations on the CU survey has a unique identifier. If you know which one you want, you can submit it directly.

```python
cpi.inflate(100, 2000, series_id="CUUSS12ASETB01")
165.15176374077112
```

If you'd like to retrieve the CPI value itself for any year, use the `get` method.

```python
cpi.get(1950)
24.1
```

You can also do that by month.

```python
cpi.get(date(1950, 1, 1))
23.5
```

The same keyword arguments are available.

```python
cpi.get(1980, items="Housing", area="Los Angeles-Long Beach-Anaheim, CA")
83.7
```

If you'd like to retrieve a particular CPI series for inspection, use the `series` attribute's `get` method. No configuration returns the default series.

```python
cpi.series.get()
```

Alter the configuration options to retrieve variations based on item, area and other metadata.

```python
cpi.series.get(items="Housing", area="Los Angeles-Long Beach-Anaheim, CA")
```

If you know a series's identifier code, you can submit that directly to `get_by_id`.

```python
cpi.series.get_by_id("CUURS49ASAH")
```

Once retrieved, the complete set of index values for a series is accessible via the `indexes` property.

```python
series = cpi.series.get(items="Housing", area="Los Angeles-Long Beach-Anaheim, CA")
series.indexes
```

That's it!

## Working with the command line

The Python package also installs a command-line interface for `inflate` that is available on the terminal.

It works the same as the Python library. First give it a value. Then a source year. By default it is adjusted to its value in the most recent year available.

```bash
inflate 100 1950
1017.09543568
```

If you'd like to adjust to a different year, submit it as an integer to the `--to` option.

```bash
inflate 100 1950 --to=1960
122.821576763
```

You can also adjust month to month. You should submit the months as parseable date strings.

```bash
inflate 100 1950-01-01 --to=2018-01-01
1054.75319149
```

Here are all its options.

```bash
inflate --help
Usage: inflate [OPTIONS] VALUE YEAR_OR_MONTH

  Returns a dollar value adjusted for inflation.

Options:
  --to TEXT      The year or month to adjust the value to.
  --series_id TEXT  The CPI data series used for the conversion. The default is the CPI-U.
  --help         Show this message and exit.
```

## Working with pandas

An inflation-adjusted column can quickly be added to a pandas DataFrame using the `apply` method. Here is an example using data tracking the median household income in the United States from [The Federal Reserve Bank of St. Louis](https://fred.stlouisfed.org/series/MEHOINUSA646N).

```python
import cpi
import pandas as pd

df = pd.read("test.csv")
df["ADJUSTED"] = df.apply(
    lambda x: cpi.inflate(x.MEDIAN_HOUSEHOLD_INCOME, x.YEAR), axis=1
)
```

The lists of CPI series and each's index values can be converted to a DataFrame using the `to_dataframe` method.

Here's how to get the series list:

```python
series_df = cpi.series.to_dataframe()
```

Here's how to get a series's index values:

```python
series_obj = cpi.series.get(items="Housing", area="Los Angeles-Long Beach-Anaheim, CA")
index_df = series_obj.to_dataframe()
```

## Source

The adjustment is made using data provided by [The Bureau of Labor Statistics](https://www.bls.gov/cpi/home.htm) at the U.S. Department of Labor.

Currently the library only supports inflation adjustments using series from the "All Urban Consumers (CU)" survey. The so-called "CPI-U" survey is the default, which is an average of all prices paid by all urban consumers. It is available from 1913 to the present. It is not seasonally adjusted. The dataset is identified by the BLS as "CUUR0000SA0." It is used as the default for most basic inflation calculations.

Other series measuring all urban consumers are available by taking advantage of the library's options. The alternative survey of "Urban Wage Earners and Clerical Workers" is not yet available.

## Updating the CPI

Since the BLS routinely releases new CPI new values, this library must periodically download the latest data. This library *does not* do this automatically. You must update the BLS dataset stored alongside the code yourself by running the following method:

```python
cpi.update()
```

## Links

* Docs: [palewi.re/docs/cpi/](https://palewi.re/docs/cpi/)
* Code: [github.com/datadesk/cpi](https://github.com/datadesk/cpi/)
* Issues: [github.com/datadesk/cpi/issues](https://github.com/datadesk/cpi/issues)
* Packaging: [pypi.python.org/pypi/cpi](https://pypi.python.org/pypi/cpi)
* Testing: [github.com/datadesk/cpi/actions](https://github.com/datadesk/cpi/actions)
