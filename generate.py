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

source_template = Template("""\
### ${title}

${annotation}
""")

with open( 'data/sources.json', 'r' ) as f:
    sources = json.loads( f.read() )

for source in sources[0:2]:
    filename = f"sources/{source['href']}.md"
    title = source['title']
    annotation = source['annotation']
    content = source_template.substitute( title=title, annotation=annotation )
    front_matter = { 'title': title, 'layout': "default", 'parent': "Sources", 'has_children': "false" }
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
