---
title: "History"
layout: default
parent: About
---

# Before 2017

For years Catherine Good (Baruch College) and Steve Stroessner (Barnard College) maintained www.reducingstereotypethreat.org. It consisted of an annotated bibliography of research on stereotype threat, along with discussions of various aspects of stereotype threat (e.g. vulnerable groups, situations, mechanisms, ...). This made it an indispensable resource for learning about stereotype threat and then teaching it to others. When training teaching assistants, I would send them to the site to explore specific questions. This research would prime them for discussion at training sessions.

# Mid 2017

Sometime in May 2017 the site went down. I searched for reports about why this might have happened, but couldn't find anything. Inquiries to the authors went unanswered. This happened just as I was gearing up for another training. Luckily it had been captured by Internet Archive and I directed students to use the Wayback Machine, but page loads were pretty slow.

# Archive project

In 2018 I began a quick project to recover this knowledge from the Internet Archive and make it available again for training and other study. The website overall had a reasonable high-level structure, divided between topics and bibliography. A lot of the challenge arose from the text itself. Not every paragraph fell into a `<p>` node, and around any inline element (span, a, formatting) was a veritable alphabet soup of various white-space characters. Unfortunately there was no clear pattern to the number or sequence of these characters, so I couldn't use them to infer paragraph breaks. (My best guess is that the text was originally written in some word processor like MS Word, and then copied and pasted into a CMS interface, which translated invisible formatting codes into these excess characters.) I developed a deep appreciation for Xpath and regular expressions during this time. More details, and the recovered data, are at [this GitHub repo](https://github.com/garcias/rst-archive).
