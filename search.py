from urllib2 import urlopen
from json import load

apiUrl = "http://dailymed.nlm.nih.gov/dailymed/services/v2/spls"
apiParam = "dea_schedule_code/C48675"
outputFormat = "?format=json"

response = urlopen(apiUrl + apiParam + outputFormat)

json_obj = load(response)

#Load the Result from the JSON response
print "---------"
print    Result
print "---------"
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
