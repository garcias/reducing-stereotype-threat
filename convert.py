import json
import re

# convert text and hrefs in topics.json, save to reviews.json

with open( 'data/topics.json', 'r' ) as f:
    topics = json.loads( f.read() )

def reformat_links( text ):
    # changes any md links in text to match typical jekyll config

    # replace "](link)" with "](/reviews/link)" as long as link doesn't begin with "bibliography"
    text = re.sub( r'\]\(((?!bibliography).*?)\)', r"](../../reviews/\1)", text)
    # replace "bibliography_" with "/sources/"
    text = re.sub( r'(bibliography)_', r"../../sources/", text)
    # replace ".html" with "/"
    text = re.sub( r'\.html', r"/", text )

    return text

for topic in topics:
    text = reformat_links( topic['text'] )
    topic['text'] = text
    topic['href'] = topic['href'].replace( r'.html', r'' )

    for subtopic in topic['subtopics']:
        text = reformat_links( subtopic['text'] )
        subtopic['text'] = text

with open( 'data/reviews.json', 'w' ) as f:
    f.write( json.dumps(topics, indent=2) )


# convert hrefs in bibliography.json, save to sources.json

with open( 'data/bibliography.json', 'r' ) as f:
    sources = json.loads( f.read() )

for source in sources:
    text = source['href']
    text = text.replace( r'bibliography_', r'')
    text = text.replace( r'.html', r'' )
    source['href'] = text

with open( 'data/sources.json', 'w' ) as f:
    f.write( json.dumps(sources, indent=2) )
