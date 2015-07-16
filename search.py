from urllib2 import urlopen
from json import load

apiUrl = "http://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json"

print apiUrl

response = urlopen(apiUrl)
json_obj = load(response)

for drug in json_obj["data"]:
	print drug["data"]




#Load the Result from the JSON response
#print "---------"
#print    Results
#print "---------"
#for objectCollection in json_obj['Results']:
#	for drug_nameAttribute, drug_nameValue in objectCollection.iteritems():
#		print drug_nameAttribute, ": ", drug_nameValue

#value = 0
#for line in source.splitlines():
#    if not line.strip():  continue
#    if line.startswith("value="):
#        try:
#            value = line.split("=")
#        except IndexError:
#            pass
#    if value > 0:
#        break
#
#open("some.html", "w").write("value is: %d" % value)
