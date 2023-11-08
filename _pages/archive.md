---
layout: page
title: Blog entries by year
permalink: /archive/
---

{% for post in site.posts  %}
    {% capture this_year %}{{ post.date | date: "%Y" }}{% endcapture %}
    {% capture next_year %}{{ post.previous.date | date: "%Y" }}{% endcapture %}

    {% if forloop.first %}
    <h2 id="{{ this_year }}-ref">{{this_year}}</h2>
    <ul style="list-style-type:none">
    {% endif %}

    <li><class="author_title")>{{ post.date | date: "%m/%d" }}</class> <a href="{{ post.url }}">{{ post.title }}</a></li>

    {% if forloop.last %}
    </ul>
    {% else %}
        {% if this_year != next_year %}
        </ul>
        <h2 id="{{ next_year }}-ref">{{next_year}}</h2>
        <ul style="list-style-type:none">
        {% endif %}
    {% endif %}
{% endfor %}

<hr>

<h3 style="text-align:center">Blog entries by <a href="{{ site.baseurl }}/categories">categories</a></h3>
