import requests as req

site = req.get("http://jh2i.com:50011/site/flag.php",allow_redirects=False)
# print chunk
nextsite = site.headers['location']


content = ""
# print nextsite
try:
	content = site.text.split("flag is ")[1].strip('\n')
except:
	print "----------------------------------"
# print fchunk

flag = content



while content != "}":
	
	site = req.get("http://jh2i.com:50011"+nextsite,allow_redirects=False)
	nextsite = site.headers['location']
	# print chunk
	try:
		content = site.text.split("flag is ")[1].strip('\n')
	except:
		print "----------------------------------"
	print "----------------------------------"
	print content

	
	# print fchunk

	flag+=content


print "|----------------------------------|"
print "|          Flag done!              |"
print "|----------------------------------|"

print flag
# print "----------------------------------------------------------------------"
# print flag.decode('hex')
