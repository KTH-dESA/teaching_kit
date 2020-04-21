---
categories: course
layout: page
author: Lorenzo Sani
title: First Demo Course
---
<h1>{{ page.title }}</h1>

Authors: {{page.author}}

This course contains the lectures showing our capabilities of transforming PowerPoint presentations to markdown presentations

***Lectures contained in this course:***

<ul class="post-list">
{% assign lectures = site.posts | where: "categories","lecture" %}
{% for lecture in lectures %}
{% if lecture.course contains page.title%}
<p><a href="{{ lecture.url | relative_url }}">{{ lecture.title | escape }} </a></p>
{% endif %}{% endfor %}</ul>