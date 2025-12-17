import os

BASE = "https://raw.githubusercontent.com/Darki68/Music/main/"
IMAGE = BASE + "IMG_1548.jpeg"

items = ""
for f in sorted(os.listdir(".")):
    if f.lower().endswith(".mp3"):
        title = os.path.splitext(f)[0]
        items += f"""
  <item>
    <title>{title}</title>
    <itunes:image href="{IMAGE}"/>
    <enclosure url="{BASE}{f}" type="audio/mpeg"/>
  </item>
"""

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
<channel>
  <title>Ma Zik Perso</title>
  <description>Playlist privée</description>
  <language>fr</language>

  <itunes:image href="{IMAGE}"/>
  <image>
    <url>{IMAGE}</url>
    <title>Ma Zik Perso</title>
    <link>https://darki68.github.io/Music/</link>
  </image>
{items}
</channel>
</rss>
"""

open("musique.xml", "w", encoding="utf-8").write(rss)
