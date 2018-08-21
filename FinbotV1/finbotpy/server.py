from ..finbot.ttypes import ApplicationType
import re, json, requests, urllib

class Server(object):
    LINE_HOST_DOMAIN            = 'https://gwx.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://gwx.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://gwx.line.naver.jp/mh'
    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'
    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'
    CHANNEL_ID = {
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440'
    }

    #APP_TYPE    = ApplicationType.CHROMEOS
    APP_NAME = 'CHROMEOS\t2.1.5\tChrome_OS\t1UA : Line 2.1.5'
    #APP_VER     = '8.2.2'
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = 'FINBOT_V1'
    #SYSTEM_VER  = 'WINDOWS5.2.2-XP-x64'
    #SYSTEM_VER  = '12.0.2'
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    USER_AGENT = 'Line/2.1.5'

    _session        = requests.session()
    timelineHeaders = {}
    Headers         = {}

    def __init__(self):
        self.Headers = {}
        self.channelHeaders = {}

    def parseUrl(self, path):
        return self.LINE_HOST_DOMAIN + path

    def urlEncode(self, url, path, params=[]):
        try:
            return url + path + '?' + urllib.parse.urlencode(params)
        except:
            return url + path + '?' + urllib.urlencode(params)

    def getJson(self, url, allowHeader=False):
        if allowHeader is False:
            return json.loads(self._session.get(url).text)
        else:
            return json.loads(self._session.get(url, headers=self.Headers).text)

    def setHeadersWithDict(self, headersDict):
        self.Headers.update(headersDict)

    def setHeaders(self, argument, value):
        self.Headers[argument] = value

    def setTimelineHeadersWithDict(self, headersDict):
        self.timelineHeaders.update(headersDict)

    def setTimelineHeaders(self, argument, value):
        self.timelineHeaders[argument] = value

    def additionalHeaders(self, source, newSource):
        headerList={}
        headerList.update(source)
        headerList.update(newSource)
        return headerList

    def optionsContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.options(url, headers=headers, data=data)

    def postContent(self, url, data=None, files=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.post(url, headers=headers, data=data, files=files)

    def getContent(self, url, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.get(url, headers=headers, stream=True)

    def deleteContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.delete(url, headers=headers, data=data)

    def putContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.put(url, headers=headers, data=data)
