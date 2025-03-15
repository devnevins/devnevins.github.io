---
title:  Porting to Pelican
date: 2025-03-14
---
By default, [GitHub pages](https://pages.github.com) uses [Jekyll](http://jekyllrb.com) as the static website generator. It worked fine but I wanted
to use tools based on one of my favorite languages, Python. I found the excellent tool
[Pelican](http://docs.getpelican.com/) so I decided to port my Jekyll site to Pelican.

The markdown files were the easiest things to port since I just had to add a bit of metadata. In
particular I liked Jekyll's way of using a filename to determine the date but Pelican didn't
seem to do that (I haven't looked at all of the [Pelican Plugins](https://github.com/pelican-plugins) 
though).

The biggest issue was that I had put my custom theme in the source tree with the site source files
and I didn't see an easy way to using that theme, especially once I setup the GitHub workflow. The
solution was simple enough in that you just have to create a separate public repo for your theme
but it did take some time to get it all sorted out.

There was excellent documentation on how to use [Pelican with GitHub pages using a custom workflow](https://docs.getpelican.com/en/latest/tips.html#publishing-to-github-pages-using-a-custom-github-actions-workflow) and I just followed the
directions and was successful. The workflow tools on GitHub are quite useful and can give you a lot
of feedback.

All in all it wasn't too bad to do the port and I'm a lot happier. I've already wanted to see how
something worked in Pelican and it was much easier for me to read the Python than knock the rust(ha!)
off of my Ruby knowledge.

I'm going to create other static sites so I needed some background on how to use Pelican. This blog
provided a good platform to learn how to do that.
