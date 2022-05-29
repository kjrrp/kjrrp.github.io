#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' A tool to create a travel index and travel page for each folder
The folder name become the page's title and filename
The pictures MUST be in the format: picN.xxx
The videos MUST be in the format: vidN.xxx, with .xxx = .avi or .mp4
The video thumbnail MUST be in the format: vidN.jpg
'''
import os
import sys
import time

header = '''<!DOCTYPE html>

<html lang="en-us">

<head>
    <title>K.</title>
    <meta charset="utf-8" />
    <link rel="stylesheet" type="text/css" href="/stylesheets/cantata-one.css">
    <link rel="stylesheet" type="text/css" media="screen" href="/stylesheets/style.css">
    <link rel="stylesheet" type="text/css" href="/stylesheets/lightbox.css">
    <!-- Definitely use these for development -->
    <script src="/js/jquery-1.11.0.min.js"></script>
    <script src="/js/jquery-ui-1.8.20.custom.min.js"></script>
	<script src="/js/language.js"></script>
    <!-- html5ightbox -->
    <script src="/js/html5lightbox.js"></script>
    <script>
        $(function () {
            $("#header").load("/header.html");
            $("#footer").load("/footer.html");
        });
    </script>
</head>

<body class='no-js' itemscope itemtype="https://schema.org/CreativeWork" style="background-color:#2B2B2B;">
    <div id="header"></div>
    <meta itemprop="name" content="kjrrp's website" />
    <meta itemprop="description" content="This is the personal site of Kévin Phemius." />
    <div class="" style="background-color:#2B2B2B;margin-bottom:-100px;">
        <h1 class="center" style="padding-top:50px;padding-bottom:130px;"><a itemprop="url" href="../index.html"
                style="color:#eee !important; text-decoration: none">K.</a></h1>
    </div>
    <div class="" style="background-color:#ddd;padding-left:10%;padding-right:10%">
        <div class="row-fluid">
            <div class="span8 offset5 pad-top">
                <br>
'''
footer = '''    <br><br>
    <!-- Social icons -->
    <div id="footer"></div>
</body>

</html>'''
first_item = '''                <h2 id="title" class="fr">%s</h2>
                <h2 id="title" class="en">%s</h2>
                <p class="en"><img class="ex_fr soc" src="../img/website/fr.png"/><img class="ex_fr soc-m" src="../img/website/fr.png"/></p>
                <p class="fr"><img class="ex_en soc" src="../img/website/en.png"/><img class="ex_en soc-m" src="../img/website/en.png"/></p>
                <p class="fr"></p>
                <p class="en"></p>
                <!-- 1st -->
                <div class="center">
                    <a href="https://kjrrp.tk/pics/travel/%s" class="html5lightbox"
                        data-group="mygroup" data-transition="slide" data-fullscreenmode="true" data-autoplay="false"
                        data-thumbnail="https://kjrrp.tk/pics/travel/%s" title=""
                        style="background: #ddd; text-decoration: none">
                        <img alt="kjrrp" src="../img/website/play.jpg" class="img-circle"
                            style="vertical-align:middle;">
                    </a>
                    <!-- Rest -->
'''
image = '''                    <a href="https://kjrrp.tk/pics/travel/%s" class="html5lightbox"
                        data-group="mygroup" style="display:none" data-transition="slide" data-fullscreenmode="true"
                        data-autoplay="false" data-thumbnail="https://kjrrp.tk/pics/travel/%s"
                        title=""></a>
'''
video = '''                    <a href="https://kjrrp.tk/pics/travel/%s" class="html5lightbox"
                        data-group="mygroup" style="display:none" data-transition="slide" data-fullscreenmode="true"
                        data-autoplay="false" data-thumbnail="https://kjrrp.tk/pics/travel/%s"
                        data-webm="https://kjrrp.tk/pics/travel/%s" title=""></a>
'''
last_item = '''                    <blockquote align="center">
                        <p class="fr"><cite>Cliquez sur l'icône pour lancer le slideshow.</cite></p>
                        <p class="en"><cite>Click on the play button to lauch the slideshow.</cite></p>
                    </blockquote>
                </div>
            </div>
        </div>
        <div class="center"><small><a href="./travel_index.html"> ¤ Index ¤ </a></small></div>
    </div>
'''
first_index = '''               <h2 id="title">Index</h2>
                <p style="padding-left:10%;padding-right:10%">
'''
index = '''                    <a href="./%s.html">%s</a><br>
'''
last_index = '''                </p>
            </div>
        </div>
        <div class="center">¤</div>
    </div>
'''

def main(argv):
    """Main function"""
    start = time.time()
    path = None
    try:
        path = argv[0]
    except Exception:
        pass
    if not path:
        print("Use make_travel_page.py path_to_picture_folder")
        sys.exit(1)
    folders = os.popen('ls %s' % path).read().split()
    if folders:
        pics = 0
        vids = 0
        with open("travel_index.html", "w") as f:
            f.write(header)
            f.write(first_index)
        for folder in folders:
            pictures = os.popen('ls -v %s%s/pic*' % (path, folder)).read().split()
            print("Parsing folder %s" % (folder))
            if pictures:
                pics += len(pictures)
                with open("travel_index.html", "a") as f:
                    f.write(index % (folder.lower(), folder))
                with open("%s.html" % (folder.lower()), "w") as f:
                    f.write(header)
                    name = pictures[0].split(path)[1]
                    f.write(first_item % (folder, folder, name, name))
                if len(pictures) > 1:
                    for item in pictures[1:]:
                        with open("%s.html" % (folder.lower()), "a") as f:
                            name = item.split(path)[1]
                            f.write(image % (name, name))
            videos = os.popen('ls -v %s%s/vid*.mp4 2> /dev/null' % (path, folder)).read().split()
            if videos:
                vids += len(videos)
                for item in videos:
                    with open("%s.html" % (folder.lower()), "a") as f:
                        name = item.split(path)[1]
                        if 'mp4' in name:
                            thumb = name.replace('mp4', 'jpg')
                        elif 'avi' in name:
                            thumb = name.replace('avi', 'jpg')
                        else:
                            thumb = ''
                        f.write(video % (name, thumb, name))
            with open("%s.html" % (folder.lower()), "a") as f:
                f.write(last_item)
                f.write(footer)
        with open("travel_index.html", "a") as f:
            f.write(last_index)
            f.write(footer)
    print("Made travel index with %s folders (%s pictures, %s videos)" % (len(folders), pics, vids))
    print("Finished in %ss" % round(time.time() - start, 2))

if __name__ == '__main__':
    main(sys.argv[1:])
