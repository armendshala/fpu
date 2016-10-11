import requests
import re
import csv

'''
REQUESTS LIBRARIES

urllib
urllib2

requests
grab
scrapy
unirest
mechanize

'''

 # KOMENTET JANE MARRUR NGA DOKUMENTACIONET PERKATESE.

session = requests.Session()

# CREATE CSV HEADER
with open('File.csv','ab') as a:
	csvwriter = csv.writer(a)
	csvwriter.writerow(['Name','Business id']) # []

# START
if __name__ == '__main__':
	
	main_url = 'http://permits.anaheim.net/tm_bin/tmw_cmd.pl?tmw_cmd=StatusViewCasebus_nbl&shl_caseno=NEWBUSLICENSE'
	response = session.get(main_url)
	if response.status_code == 200: # response

		'''
		https://docs.python.org/2/library/re.html
		re.findall(pattern, string, flags=0)

		Return all non-overlapping matches of pattern in string, as a list of strings.
		The string is scanned left-to-right, and matches are returned in the order found. 
		If one or more groups are present in the pattern, return a list of groups; this will be a list of tuples if the pattern has more than one group. 
		Empty matches are included in the result unless they touch the beginning of another match.
		'''
		lista_url = re.findall(r'<a href="(http://permits\.anaheim\.net/tm_bin/tmw_cmd\.pl\?tmw_cmd=StatusViewCaseBUS_NBL_\d+&shl_caseno=NEWBUSLICENSE)">',response.content,re.I|re.S)
		for link in lista_url:
			print link

			response_year = session.get(link)
			if response_year.status_code == 200:
				
				for business_number in re.findall(r'<a href="(tmw_cmd\.pl\?tmw_cmd=StatusViewCasebus&shl_caseno=[^"]+)"', # IGS
					response_year.content,re.I|re.S):
					
					business_number = 'http://permits.anaheim.net/tm_bin/%s' % business_number
					print business_number

					response_business = session.get(business_number)
					if response_business.status_code == 200:

						name = ''
						business_id = ''

						'''
						https://docs.python.org/2/library/re.html
						re.search(pattern, string, flags=0)
					
						Scan through string looking for a location where this regular expression produces a match, and return a corresponding MatchObject instance. 
						Return None if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.
						'''

						pattern_name = re.search(r'Name:</b></TD>\s*<td class="ReportCellBlank">[&nbsp;]+([^<]+)<',response_business.content,re.I|re.S) # NONE
						if pattern_name:
							name = pattern_name.group(1)

						pattern_businessId = re.search(r'(BUS\d{4}-\d{3,})',response_business.content,re.I|re.S) # NONE
						if pattern_businessId:
							business_id = pattern_businessId.group(1)

							print 'Name: %s ,Business id: %s' % (name,business_id)

							'''
							https://docs.python.org/3/library/csv.html
							csv.writer(csvfile, dialect='excel', **fmtparams)

							Return a writer object responsible for converting the user's data into delimited strings on the given file-like object. csvfile can be any object with a write() method. 
							If csvfile is a file object, it must be opened with the 'b' flag on platforms where that makes a difference.
							'''

							with open('File.csv','ab') as a:
								csvwriter = csv.writer(a)
								csvwriter.writerow([name,business_id])


# http://docs.python-requests.org/en/master/api/#requests.Response
'''
REQUEST REQUEST PARAMETERS:
-----------------------------------------------------------------------------------------------------
method -- method for the new Request object.
url -- URL for the new Request object.
params -- (optional) Dictionary or bytes to be sent in the query string for the Request.
data -- (optional) Dictionary, bytes, or file-like object to send in the body of the Request.
json -- (optional) json data to send in the body of the Request.
headers -- (optional) Dictionary of HTTP Headers to send with the Request.
cookies -- (optional) Dict or CookieJar object to send with the Request.
files -- (optional) Dictionary of 'name': file-like-objects (or {'name': file-tuple}) for multipart encoding upload. file-tuple can be a 2-tuple ('filename', fileobj), 3-tuple ('filename', fileobj, 'content_type') or a 4-tuple ('filename', fileobj, 'content_type', custom_headers), where 'content-type' is a string defining the content type of the given file and custom_headers a dict-like object containing additional headers to add for the file.
auth -- (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
timeout (float or tuple) -- (optional) How long to wait for the server to send data before giving up, as a float, or a (connect timeout, read timeout) tuple.
allow_redirects (bool) -- (optional) Boolean. Set to True if POST/PUT/DELETE redirect following is allowed.
proxies -- (optional) Dictionary mapping protocol to the URL of the proxy.
verify -- (optional) whether the SSL cert will be verified. A CA_BUNDLE path can also be provided. Defaults to True.
stream -- (optional) if False, the response content will be immediately downloaded.
cert -- (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.

Returns:Response object
'''



# http://docs.python-requests.org/en/master/api/#requests.Response
'''
Response object - The Response object, which contains a server's response to an HTTP request.
--------------------------------------------------------------------------------------------------------------

apparent_encoding - The apparent encoding, provided by the chardet library
close()[source] - Releases the connection back to the pool. Once this method has been called the underlying raw object must not be accessed again.
content - Content of the response, in bytes.
cookies = None - A CookieJar of Cookies the server sent back.
elapsed = None - The amount of time elapsed between sending the request and the arrival of the response (as a timedelta). This property specifically measures the time taken between sending the first byte of the request and finishing parsing the headers. It is therefore unaffected by consuming the response content or the value of the stream keyword argument.
encoding = None - Encoding to decode with when accessing r.text.
headers = None - Case-insensitive Dictionary of Response Headers. For example, headers['content-encoding'] will return the value of a 'Content-Encoding' response header.
history = None - A list of Response objects from the history of the Request. Any redirect responses will end up here. The list is sorted from the oldest to the most recent request.
is_permanent_redirect - True if this Response one of the permanent versions of redirect

is_redirect - True if this Response is a well-formed HTTP redirect that could have been processed automatically (by Session.resolve_redirects).

iter_content(chunk_size=1, decode_unicode=False)[source] - Iterates over the response data. When stream=True is set on the request, this avoids reading the content at once into memory for large responses. The chunk size is the number of bytes it should read into memory. This is not necessarily the length of each item returned as decoding can take place.
chunk_size must be of type int or None. A value of None will function differently depending on the value of stream. stream=True will read data as it arrives in whatever size the chunks are received. If stream=False, data is returned as a single chunk.
If decode_unicode is True, content will be decoded using the best available encoding based on the response.

iter_lines(chunk_size=512, decode_unicode=None, delimiter=None)[source] - 
Iterates over the response data, one line at a time. When stream=True is set on the request, this avoids reading the content at once into memory for large responses.

json(**kwargs)[source] - Returns the json-encoded content of a response, if any.
Parameters:	**kwargs -- Optional arguments that json.loads takes.

links - Returns the parsed header links of the response, if any.

raise_for_status()[source] - Raises stored HTTPError, if one occurred.

raw = None - File-like object representation of response (for advanced usage). Use of raw requires that stream=True be set on the request.

reason = None - Textual reason of responded HTTP Status, e.g. "Not Found" or "OK".

request = None - The PreparedRequest object to which this is a response.

status_code = None - Integer Code of responded HTTP Status, e.g. 404 or 200.

text - Content of the response, in unicode.

If Response.encoding is None, encoding will be guessed using chardet.
The encoding of the response content is determined based solely on HTTP headers, following RFC 2616 to the letter. If you can take advantage of non-HTTP knowledge to make a better guess at the encoding, you should set r.encoding appropriately before accessing this property.

url = None - Final URL location of Response.
'''