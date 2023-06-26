from dataclasses import dataclass
from string import Template
import json

header_template = Template("""\
---
title: ${title}
parent: ${parent}
layout: ${layout}
has_children: ${has_children}
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

review_template = Template("""
## ${title}

${text}
""")

with open( 'data/sources.json', 'r' ) as f:
    sources = json.loads( f.read() )

with open( 'data/reviews.json', 'r' ) as f:
    reviews = json.loads( f.read() )

for source in sources[0:2]:
    filename = f"sources/{source['href']}.md"
    try:
        front_matter = { 
            'title': source['title'], 'layout': "default", 'parent': "Sources", 'has_children': "false", 
        }
        # title = source['title']
        # annotation = source['annotation']
        content = source_template.substitute( **source )
        write_page( filename, content, **front_matter )
    except KeyError:
        pass

for review in reviews[0:2]:
    filename = f"reviews/{review['href']}.md"
    front_matter = {
        'title': review['question'], 'layout': "default", 'parent': "Reviews", 'has_children': "false",
    }
    content = f"# {review['title']}\n\n"
    content += review['text'] + "\n"
    for subtopic in review['subtopics']:
        content += review_template.substitute( **subtopic )
    write_page( filename, content, **front_matter )



# @dataclass
# class JekyllPage:
#     filename: str
#     title: str
#     parent: str = ""
#     layout: str = "default"
#     has_children: str = "false"

#     def write_page( self ):
#         front_matter = page_template.substitute(
#             title = self.title, parent = self.parent, 
#             layout = self.layout, has_children = self.has_children
#         )
#         print( front_matter )

# jp = JekyllPage("hello.md", "Hello!")
# jp.write_page()
