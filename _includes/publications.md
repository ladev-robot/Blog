{% if include.show_heading != false %}
<h2 id="publications">Publications</h2>
{% endif %}

<div class="publications">
{% for link in site.data.publications.main %}
<div class="pub-row">
  <div class="pub-teaser">
    {% if link.image %}
    <img src="{{ link.image | relative_url }}" class="teaser" alt="">
    {% endif %}
  </div>
  <div class="pub-meta">
    <div class="title"><strong>{{ link.title }}</strong></div>
    <div class="author">{{ link.authors }}</div>
    {% if link.conference %}
    <div class="periodical"><em>{{ link.conference }}</em></div>
    {% endif %}
    <div class="links">
      {% assign sep = false %}
      {% if link.pdf %}
        {% if sep %}<span class="link-sep">|</span>{% endif %}
        <a href="{{ link.pdf | relative_url }}" target="_blank" rel="noopener">PDF</a>{% assign sep = true %}
      {% endif %}
      {% if link.arxiv %}
        {% if sep %}<span class="link-sep">|</span>{% endif %}
        <a href="{{ link.arxiv }}" target="_blank" rel="noopener">arXiv</a>{% assign sep = true %}
      {% endif %}
      {% if link.venue_link %}
        {% if sep %}<span class="link-sep">|</span>{% endif %}
        <a href="{{ link.venue_link }}" target="_blank" rel="noopener">{{ link.venue_label | default: "PDF" }}</a>{% assign sep = true %}
      {% endif %}
      {% if link.video %}
        {% if sep %}<span class="link-sep">|</span>{% endif %}
        <a href="{{ link.video }}" target="_blank" rel="noopener">video</a>{% assign sep = true %}
      {% endif %}
      {% if link.bilibili %}
        {% if sep %}<span class="link-sep">|</span>{% endif %}
        <a href="{{ link.bilibili }}" target="_blank" rel="noopener">bilibili</a>{% assign sep = true %}
      {% endif %}
      {% if link.page %}
        {% if sep %}<span class="link-sep">|</span>{% endif %}
        <a href="{{ link.page }}" target="_blank" rel="noopener">project</a>{% assign sep = true %}
      {% endif %}
      {% if link.code %}
        {% if sep %}<span class="link-sep">|</span>{% endif %}
        <a href="{{ link.code }}" target="_blank" rel="noopener">code</a>{% assign sep = true %}
      {% endif %}
      {% if link.bibtex %}
        {% if sep %}<span class="link-sep">|</span>{% endif %}
        <a href="{{ link.bibtex }}" target="_blank" rel="noopener">bibtex</a>{% assign sep = true %}
      {% endif %}
      {% if link.others %}
        {% if sep %}<span class="link-sep">|</span>{% endif %}
        {{ link.others }}
      {% endif %}
    </div>
  </div>
</div>
{% endfor %}
</div>
