#!/usr/bin/python
# -*- coding: utf-8  -*-
import config
import httplib
import threading 
import terminal_interface
import excepts
import urllib
import re
import config

output_lock = threading.Lock()
input_lock = threading.Lock()

ui=terminal_interface.UI()


def urlEncode( query):
    """Encode a query so that it can be sent using an http POST request."""
    if not query:
        return None
    if hasattr(query, 'iteritems'):
        iterator = query.iteritems()
    else:
        iterator = iter(query)
    l = []
    wpEditToken = None
    for key, value in iterator:
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        key = urllib.quote(key)
        value = urllib.quote(value)
        if key == 'wpEditToken':
            wpEditToken = value
            continue
        l.append(key + '=' + value)

    # wpEditToken is explicitly added as last value.
    # If a premature connection abort occurs while putting, the server will
    # not have received an edit token and thus refuse saving the page
    if wpEditToken != None:
        l.append('wpEditToken=' + wpEditToken)
    return '&'.join(l)

def input(question, colors = None):
    return ui.input(question, colors)
#def input(question, password = False):
#    """Ask the user a question, return the user's answer.
#
#    Parameters:
#    * question - a unicode string that will be shown to the user. Don't add a
#                 space after the question mark/colon, this method will do this
#                 for you.
#    * password - if True, hides the user's input (for password entry).
#
#    Returns a unicode string.
#
#    """
#    input_lock.acquire()
#    try:
#        data = ui.input(question, password)
#    finally:
#        flush_output_cache()
#        input_lock.release()
#
#    return data

def decompress_gzip(data):
    # Use cStringIO if available
    # TODO: rewrite gzip.py such that it supports unseekable fileobjects.
    if data:
        try:
            from cStringIO import StringIO
        except ImportError:
            from StringIO import StringIO
        import gzip
        try:
            data = gzip.GzipFile(fileobj = StringIO(data)).read()
        except IOError:
            raise
    return data

def postData(address, data,
                 contentType='application/x-www-form-urlencoded',
                 compress=True, cookies=None):
        """Post encoded data to the given http address at this site.

        address is the absolute path without hostname.
        data is an ASCII string that has been URL-encoded.

        Returns a (response, data) tuple where response is the HTTP
        response object and data is a Unicode string containing the
        body of the response.
        """

	conn = httplib.HTTPConnection("es.wikipedia.org")

        conn.putrequest('POST', address)
        conn.putheader('Content-Length', str(len(data)))
        conn.putheader('Content-type', contentType)
        conn.putheader('User-agent', config.useragent)
        if cookies:
            conn.putheader('Cookie', cookies)
        if False: #self.persistent_http:
            conn.putheader('Connection', 'Keep-Alive')
        if compress:
            conn.putheader('Accept-encoding', 'gzip')
        conn.endheaders()
        conn.send(data)

        # Prepare the return values
        # Note that this can raise network exceptions which are not
        # caught here.
        try:
            response = conn.getresponse()
        except httplib.BadStatusLine:
            # Blub.
            conn.close()
            conn.connect()
	    print "error in Post"

        data = response.read()

        if compress and response.getheader('Content-Encoding') == 'gzip':
            data = decompress_gzip(data)

        data = data.decode("utf-8")
        response.close()

        if True: #not self.persistent_http:
            conn.close()

        # If a wiki page, get user data
        #self._getUserData(data, sysop = sysop)

        return response, data


class LoginManager:
    def __init__(self, password = None, site = None):
	self.site=config.site
	try:
       		self.username = config.username
	except:
		raise excepts.NoUsername(u'ERROR: Username is undefined.\nPlease add a line in config.py with the form:\nusername=\'myUsername\'')
        self.password = config.password

    def getCookie(self, remember=True):
        """
        Login to the site.

        remember    Remember login (default: True)

        Returns cookie data if succesful, None otherwise.
        """
        predata = {
            'action': 'login', 
            'lgname': self.username.toUtf8(),
            'lgpassword': self.password.toUtf8(),
        }
	address = "http://"+config.language+"."+config.project+".org/w/api.php"
        
        response, data = postData(address, urlEncode(predata))
        Reat=re.compile(': (.*?);')
        L = []

        for eat in response.msg.getallmatchingheaders('set-cookie'):
            m = Reat.search(eat)
            if m:
                L.append(m.group(1))

        got_token = got_user = False
        for Ldata in L:
            if 'Token=' in Ldata:
                got_token = True
            if 'User=' in Ldata or 'UserName=' in Ldata:
                got_user = True
        
        if got_token and got_user:
            return "\n".join(L)
	else:
	    captchaR = re.compile('<input type="hidden" name="wpCaptchaId" id="wpCaptchaId" value="(?P<id>\d+)" />')
            match = captchaR.search(data)
            if match:
                id = match.group('id')
                if not config.solve_captcha:
	    		print "Captcha error"
                url = self.site.protocol() + '://' + self.site.hostname() + self.site.captcha_image_address(id)
                answer = ui.askForCaptcha(url)
                return self.getCookie(remember = remember, captchaId = id, captchaAnswer = answer)

        return None

    def storecookiedata(self, data):
        """
        Stores cookie data.

        The argument data is the raw data, as returned by getCookie().

        Returns nothing."""
        filename = "login-data"
        f = open(filename, 'w')
        f.write(data)
        f.close()

    def cookies(self):
	f = open("login-data")
        cookies = '; '.join([x.strip() for x in f.readlines()])
        f.close()
	#print cookies
	return cookies

    def login(self, username, password, retry = False):
        #self.password = self.password.encode(self.site.encoding())
	self.password=password
	self.username=username
        ui.output(u"Logging in as %s\n" % (self.username))
        cookiedata = self.getCookie()
        if cookiedata:
            self.storecookiedata(cookiedata)
            ui.output(u"Should be logged in now\n")
            return True
        else:
            ui.output(u"Login failed. Wrong password?\n")
            if retry:
                self.password = None
                return self.login(retry = True)
            else:
                return False


