from string import Template
import json

header_template = Template("""\
---
title: ${title}
parent: ${parent}
layout: ${layout}
has_children: ${has_children}
nav_order: ${nav_order}
nav_exclude: ${nav_exclude}
---
""")

def write_page( filename, content, **metadata):
    with open( filename, 'w' ) as f:
        front_matter = header_template.substitute( **metadata )
        f.write( front_matter )
        f.write( content )

source_template = Template("""
# ${title}

### ${citation}

${annotation}
""")

with open( 'data/sources.json', 'r' ) as f:
    sources = json.loads( f.read() )

with open( 'data/reviews.json', 'r' ) as f:
    reviews = json.loads( f.read() )

for source in sources:
    filename = f"sources/{source['href']}.md"
    try:
        front_matter = { 
            'title': source['title'], 'layout': "default", 'parent': "Sources", 'has_children': "false",
            'nav_order': "", 'nav_exclude': "true",
        }
        content = source_template.substitute( **source )
        write_page( filename, content, **front_matter )
    except KeyError:
        pass


review_template = Template("""
# ${question}
{: .no_toc }

${text}

#### Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

""")

subtopic_template = Template("""
## ${title}

${text}
""")

# Use this to determine the correct nav_order for each review page
review_order = {
    'definition': 1, 'vulnerable': 2, 'situations': 3, 'consequences': 4, 
    'mechanisms': 5, 'reduce': 6, 'criticisms': 7, 'unresolved': 8
}

for review in reviews:
    filename = f"reviews/{review['href']}.md"
    front_matter = {
        'title': review['href'], 'layout': "default", 'parent': "Reviews", 'has_children': "false",
        'nav_order': review_order[ review['href'] ], 'nav_exclude': "false",
    }
    content = review_template.substitute( **review )
    for subtopic in review['subtopics']:
        content += subtopic_template.substitute( **subtopic )
    write_page( filename, content, **front_matter )
