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
    <!-- meta stuff -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="description" content="This is the personal website of Kévin Phemius." />
    <meta property="og:title" content="kjrrp's Site" />
    <meta property="og:type" content="website" />
    <meta property="og:image" content="../img/website/apple-touch-icon-114x114.png" />
    <meta property="og:url" content="https://kjrrp.github.io" />
    <meta property="og:description" content="This is the personal website of Kévin Phemius." />
    <meta name="twitter:creator" content="@kjrrp" />
    <meta name="twitter:site" content="@kjrrp" />
    <meta name="twitter:url" content="https://kjrrp.github.io" />
    <meta name="twitter:title" content="kjrrp's site" />
    <meta name="twitter:description" content="This is the personal website of Kévin Phemius." />
    <meta name="twitter:image" content="../img/website/apple-touch-icon-114x114.png" />
    <!-- stylesheets and icons -->
    <link href='../stylesheets/cantata-one.css' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" media="screen" href="../stylesheets/style.css">
    <link rel="stylesheet" type="text/css" href="../stylesheets/lightbox.css">
    <link rel="shortcut icon" href="../img/website/favicon.png">
    <link rel="apple-touch-icon" sizes="57x57" href="../img/website/apple-touch-icon.png">
    <link rel="apple-touch-icon" sizes="72x72" href="../img/website/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="114x114" href="../img/website/apple-touch-icon-114x114.png">
    <!-- Definitely use these for development -->
    <script src="../js/jquery-1.11.0.min.js"></script>
    <script src="../js/jquery-ui-1.8.20.custom.min.js"></script>
    <script src="../js/language.js"></script>
    <!-- html5ightbox -->
    <script src="../js/html5lightbox.js"></script>
</head>

<body class='no-js' itemscope itemtype="https://schema.org/CreativeWork" style="background-color:#2B2B2B;">
    <meta itemprop="name" content="kjrrp's site" />
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
    <div class="center" style="color:#fff;line-height:normal;">
        <a href="../index.html" title="by kjrrp" itemprop="author"><img alt="kjrrp" src="../img/website/kjrrp.jpg"
                class="img-circle" style="vertical-align:middle;"></a>
        <br><br>
        <a target="_blank" title="Find me on LinkedIn."
            href="https://www.linkedin.com/pub/k%C3%A9vin-phemius/41/7a9/41a/en"><img class="soc-m" alt="ln"
                src="../img/soc/lnh.png" /><img class="soc" alt="ln" src="../img/soc/ln.png"
                onmouseover="this.src='../img/soc/lnh.png'" onmouseout="this.src='../img/soc/ln.png'" /></a>
        <a target="_blank" title="Send me a Tweet." href="https://twitter.com/home/?status=@kjrrp&nbsp;"><img
                class="soc-m" alt="tw" src="../img/soc/twh.png" /><img class="soc" alt="tw" src="../img/soc/tw.png"
                onmouseover="this.src='../img/soc/twh.png'" onmouseout="this.src='../img/soc/tw.png'" /></a>
        <a target="_blank" title="Find me on Facebook." href="https://www.facebook.com/kjrrp"><img class="soc-m"
                alt="fb" src="../img/soc/fbh.png" /><img class="soc" alt="fb" src="../img/soc/fb.png"
                onmouseover="this.src='../img/soc/fbh.png'" onmouseout="this.src='../img/soc/fb.png'" /></a>
        <a target="_blank" title="Find me on Github." href="https://github.com/kjrrp"><img class="soc-m" alt="ghb"
                src="../img/soc/ghh.png" /><img class="soc" alt="ghb" src="../img/soc/gh.png"
                onmouseover="this.src='../img/soc/ghh.png'" onmouseout="this.src='../img/soc/gh.png'" /></a>
        <a target="_blank" title="Find me on Instagram." href="https://instagram.com/kjrrp"><img class="soc-m" alt="ig"
                src="../img/soc/igh.png" /><img class="soc" alt="ig" src="../img/soc/ig.png"
                onmouseover="this.src='../img/soc/igh.png'" onmouseout="this.src='../img/soc/ig.png'" /></a>
    </div>
    <footer>
        <div class="center">
            <xsmall>
                Copyright ©
                <script>document.write(new Date().getFullYear())</script> Kévin Phemius.<br> All rights reserved.
            </xsmall>
        </div>
    </footer>
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
