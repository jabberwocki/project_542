import urllib
import urllib2
url = "http://dailymed.nlm.nih.gov/dailymed/services/v2/spls"
post = urllib.urlencode({})

request = urllib2.Request(url, post)
socket = urllib2.urlopen(request)

hdrs = socket.headers
source = socket.read()
socket.close()

print "---- Headers -----"
print hdrs
print "---- Source HTML -----"
print source
print "---- END -----"

value = 0
for line in source.splitlines():
    if not line.strip():  continue
    if line.startswith("value="):
        try:
            value = line.split("=")
        except IndexError:
            pass
    if value > 0:
        break

open("some.html", "w").write("value is: %d" % value)
