---
layout: homepage
title: Home
permalink: /
---

{% capture about_bio %}
<p>
I am a Navigation Algorithm Engineer at the
<a href="https://www.jhatc.cn/" target="_blank" rel="noopener">Jianghuai Laboratory</a>,
advised by
<a href="https://www.bnrist.tsinghua.edu.cn/info/1229/3909.htm" target="_blank" rel="noopener">Prof. Lu Weining</a>.
</p>
<p>
Before that, I received my Master's degree from
<a href="https://bigdata.ahu.edu.cn/" target="_blank" rel="noopener">CosineLab</a>
at Anhui University, supervised by 
<a href="https://cs.ahu.edu.cn/2021/1216/c20807a277191/page.htm" target="_blank" rel="noopener">Prof. Wang Qingren</a>.
</p>
<p>
My research interests lie in unmanned systems and autonomous navigation, with a focus on:
</p>
<ul class="about-interests">
  <li>End-to-end planning</li>
  <li>Trajectory optimization</li>
  <li>Vision-and-Language Navigation (VLN)</li>
</ul>
{% endcapture %}
{% include about.html bio=about_bio %}

{% include publications.md %}

{% include education.html %}

{% include honors.html %}

{% include experience.html %}
