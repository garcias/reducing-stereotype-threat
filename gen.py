
import subprocess
import re
import json

# Create individual bibliography pages

with open('data/bibliography.json', 'r') as f:
    bib = json.load(f)

subprocess.call('rm -rf content/bibliography/', shell=True)

for entry in bib:
    if entry['href']:
        slug = entry['href']
        slug = re.sub('bibliography_', '', slug)
        slug = re.sub('%20', '_', slug)
        slug = re.sub('[\(\)\']', '', slug)
        slug = re.sub('\.html', '', slug)
        entry['md'] = 'bibliography/{}.md'.format(slug)
        entry['slug'] = '../../bibliography/{}'.format(slug)
        subprocess.call('hugo new --quiet {}'.format(entry['md']), shell=True)

        with open('content/{}'.format(entry['md']), 'r') as f:
            content = f.read()

        with open('content/{}'.format(entry['md']), 'w') as f:
            pattern = '(?<=draft\:)\ *?true'
            content = re.sub(pattern, ' false', content, count=1)
            pattern = '(?<=title\:)\ *?\".*?\"'
            content = re.sub(pattern, ' {}'.format(entry['title'].encode("UTF-8")), content, count=1)
            citation = re.sub(
                re.escape(entry['journal']),
                '*{}*'.format(entry['journal']),
                entry['citation'].encode("UTF-8")
            )
            citation = re.sub('\"', '\xe2\x80\x9c', citation, count=1)
            citation = re.sub('\"', '\xe2\x80\x9d', citation, count=1)
            pattern = '(?<=description\:)\ *?\".*?\"'
            content = re.sub(pattern, ' "{}"'.format(citation), content, count=1)
            f.write(content)

        with open('content/{}'.format(entry['md']), 'a') as f:
            f.write(entry['annotation'].encode("UTF-8"))
            f.write('\n')


# Replace link urls in topics text to match hugo structure

with open('data/topics.json', 'r') as f:
    topics_json = f.read()

for entry in bib:
    if entry['href']:
        pattern = '\]\({}\)'.format( re.escape(entry['href']) )
        replace = ']({})'.format(entry['slug'])
        topics_json = re.sub(pattern, replace, topics_json)

# Clean out unreplaced links
for ref in re.findall('\(bibliography_.*?\)', topics_json):
    topics_json = re.sub(re.escape(ref), '(#)', topics_json )


# Replace links to topic pages with appropriate slugs

topics = json.loads(topics_json)

for topic in topics:
    if topic['href']:
        slug = topic['href']
        slug = re.sub('\.html', '', slug)
        topic['md'] = 'topics/{}.md'.format(slug)
        topic['slug'] = '../../topics/{}'.format(slug)

        pattern = '\]\({}\)'.format( re.escape(topic['href']) )
        replace = ']({})'.format( topic['slug'] )
        topics_json = re.sub(pattern, replace, topics_json)


# Create topic pages

topics = json.loads(topics_json)

weight = {
    "stereotype threat" : 1,
    "consequences" : 4 ,
    "vulnerable" : 2,
    "situations" : 3,
    "mechanisms" : 5,
    "reduce" : 6,
    "criticisms" : 7,
    "unresolved issues" : 8,
}
subprocess.call('rm -rf content/topics/', shell=True)

for topic in topics:
    if topic['href']:
        slug = topic['href']
        slug = re.sub('\.html', '', slug)
        topic['md'] = 'topics/{}.md'.format(slug)
        topic['slug'] = '../../topics/{}'.format(slug)
        
        subprocess.call('hugo new --quiet {}'.format(topic['md']), shell=True)

        with open('content/{}'.format(topic['md']), 'r') as f:
            content = f.read()

        with open('content/{}'.format(topic['md']), 'w') as f:
            pattern = '(?<=weight\:)\ *?0'
            content = re.sub(pattern, ' {}'.format(weight[topic['topic']]), content, count=1)
            pattern = '(?<=draft\:)\ *?true'
            content = re.sub(pattern, ' false', content, count=1)
            pattern = '(?<=description\:)\ *?\"\"'
            content = re.sub(pattern, ' "{}"'.format(topic['question']), content, count=1)
            f.write(content)
        
        with open('content/{}'.format(topic['md']), 'a') as f:
            # f.write('# {}'.format(topic['question'].encode("UTF-8")) )
            # f.write('\n\n')
            f.write(topic['text'].encode("UTF-8"))
            f.write('\n\n')

            for subtopic in topic['subtopics']:
                f.write( '## {}'.format(subtopic['title']) )
                f.write('\n\n')
                f.write(subtopic['text'].encode("UTF-8"))
                f.write('\n\n')



# for name in ["a", "b"]:
#     new_file = 'posts/{}.md'.format(name)
#     subprocess.call('hugo new {}'.format(new_file), shell=True)
    
#     with open('content/{}'.format(new_file), 'r') as f:
#         content = f.read()
#         pattern = '(?<=title)\ *\:\ *\".*\"' 
#         title_value = re.findall(pattern, content)[0]  # matches ': "the page title"'
#         old_title = re.findall('(?<=\").*(?=\")', title_value)[0] # matches text without quotes
#         new_title = old_title + "_2"
    
#     with open('content/{}'.format(new_file), 'w') as f:
#         f.write(re.sub(re.escape(old_title), new_title, content))

