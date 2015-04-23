import re
import urllib
import itertools
from multiprocessing import Pool
import os
import subprocess

import FileSystemSetup as FSS
import PatentZephyr.src.python.CFPAPIconfig as config

#
#  ************************************************************************
#  ************************************************************************
#  Downloaders
#
#
#
#
#


#
#   Patent Grant URLS
#
def getPatentUrlsToDownload(year, is_hist, google_url=False):
    print 'fetching patent grants urls..............'
    if google_url == False:
        year = str(year)
        if int(year) > 2000 :
            pattern = re.compile("downloads/GrantRedBookText/"+year+"/.+\.zip")
        else:
            return []
        htmlsource = urllib.urlopen("http://patents.reedtech.com/parbft.php")
        htmlstring = htmlsource.read()
        urls = pattern.findall(htmlstring)
        # if is_hist = true return everything for given year else return latest file
        output_urls =[]
        for u in urls:
            output_urls.append('http://patents.reedtech.com/'+u.split('">')[0])
            #print 'http://patents.reedtech.com/'+u.split('">')[0]
        if is_hist:
            return output_urls
        else:
            return [output_urls[0]]
    else:
        year = str(year)
        pattern = re.compile("storage.googleapis.com/patents/grant_full_text/"+year+"/.+\.zip")

        htmlsource = urllib.urlopen("http://www.google.com/googlebooks/uspto-patents-grants-text.html")
        htmlstring = htmlsource.read()
        urls = pattern.findall(htmlstring)
        # if is_hist = true return everything for given year else return latest file
        output_urls =[]
        for u in urls:
            output_urls.append('http://'+u)
            #print 'http://patents.reedtech.com/'+u.split('">')[0]
        print output_urls
        if is_hist:
            return output_urls
        else:
            return [output_urls[-1]]


#
#   Patent Applications URLS
#

#http://storage.googleapis.com/patents/appl_full_text/2015/ipa150115.zip
def getPatentApplicationUrlsToDownload(year, is_hist, google_url=False):
    print 'fetching Patent Application urls'
    if google_url == False:
        year = str(year)
        if int(year) > 2000 :
            pattern = re.compile("downloads/ApplicationFullText/"+year+"/.+\.zip")
        else:
            return []
        htmlsource = urllib.urlopen("http://patents.reedtech.com/parbft.php")
        htmlstring = htmlsource.read()
        urls = pattern.findall(htmlstring)
        # if is_hist = true return everything for given year else return latest file
        output_urls =[]
        for u in urls:
            output_urls.append('http://patents.reedtech.com/'+u.split('">')[0])
            #print 'http://patents.reedtech.com/'+u.split('">')[0]
        if is_hist:
            return output_urls
        else:
            return [output_urls[0]]
    else:
        year = str(year)

        pattern = re.compile("storage.googleapis.com/patents/appl_full_text/"+year+"/.+\.zip")

        htmlsource = urllib.urlopen("http://www.google.com/googlebooks/uspto-patents-applications-text.html")
        htmlstring = htmlsource.read()
        urls = pattern.findall(htmlstring)
        # if is_hist = true return everything for given year else return latest file
        output_urls =[]
        for u in urls:
            output_urls.append('http://'+u)
            #print 'http://patents.reedtech.com/'+u.split('">')[0]
        print output_urls
        if is_hist:
            return output_urls
        else:
            return [output_urls[-1]]


#
#   Trademark Application URLS
#

def getTradeMarkApplicationUrlsToDownload(year, is_hist, google_url=False):
    if google_url ==False:
        print 'fetching trademark applications urls'
        year = str(year)
        if int(year) > 2014:
            pattern = re.compile("downloads/TrademarkDailyXML/"+year+"/.+\.zip")
        else:
            pattern = re.compile("downloads/TrademarkDailyXML/1884-2014/.+\.zip")
        htmlsource = urllib.urlopen("http://patents.reedtech.com/tmappxml.php")
        htmlstring = htmlsource.read()
        urls = pattern.findall(htmlstring)
        # if is_hist = true return everything for given year else return latest file
        output_urls =[]
        for u in urls:
            output_urls.append('http://patents.reedtech.com/'+u.split('">')[0])
            #print 'http://patents.reedtech.com/'+u.split('">')[0]
        if is_hist:
            return output_urls
        else:
            return [output_urls[0]]
    else:

        year = str(year)
        if int(year) < 2013:

            pattern = re.compile("storage.googleapis.com/trademarks/retro/2012/.+\.zip")
        else:
            pattern = re.compile("storage.googleapis.com/trademarks/applications/"+year+"/.+\.zip")


        htmlsource = urllib.urlopen("http://www.google.com/googlebooks/uspto-trademarks-recent-applications.html")
        htmlstring = htmlsource.read()
        urls = pattern.findall(htmlstring)
        print urls
        # if is_hist = true return everything for given year else return latest file
        output_urls =[]
        for u in urls:
            output_urls.append('http://'+u)
            #print 'http://patents.reedtech.com/'+u.split('">')[0]
        print output_urls
        if is_hist:
            return output_urls
        else:
            return [output_urls[-1]]

#
#   Trademark Assignment URLS
#

def getTradeMarkAssignmentUrlsToDownload(year, is_hist):
    print 'fetching trademark applications urls'
    year = str(year)
    if int(year) > 2013:
        pattern = re.compile("downloads/TrademarkAssignments/"+year+"/.+\.zip")
    else:
        pattern = re.compile("downloads/TrademarkAssignments/1980-2013/.+\.zip")
    htmlsource = urllib.urlopen("http://patents.reedtech.com/tmassign.php")
    htmlstring = htmlsource.read()
    urls = pattern.findall(htmlstring)
    # if is_hist = true return everything for given year else return latest file
    output_urls =[]
    for u in urls:
        output_urls.append('http://patents.reedtech.com/'+u.split('">')[0])
        #print 'http://patents.reedtech.com/'+u.split('">')[0]
    if is_hist:
        return output_urls
    else:
        return [output_urls[0]]

#
#   Trademark Trials & Appeals URLS
#

def getTradeMarkTabUrlsToDownload(year, is_hist):
    print 'fetching trademark tab urls'
    year = str(year)
    if int(year) > 2013:
        pattern = re.compile("downloads/TrademarkTTAB/"+year+"/.+\.zip")
    else:
        pattern = re.compile("downloads/TrademarkTTAB/1955-2013/.+\.zip")
    htmlsource = urllib.urlopen("http://patents.reedtech.com/tmttab.php")
    htmlstring = htmlsource.read()
    urls = pattern.findall(htmlstring)
    # if is_hist = true return everything for given year else return latest file
    output_urls =[]
    for u in urls:
        output_urls.append('http://patents.reedtech.com/'+u.split('">')[0])
        #print 'http://patents.reedtech.com/'+u.split('">')[0]
    if is_hist:
        return output_urls
    else:
        return [output_urls[0]]

#
#   Patent Assignment URLS
#
def getPatentAssignmentUrlsToDownload(year, is_hist):
    print 'fetching Patent Assignment urls'
    year = str(year)
    if int(year) > 2014:
        pattern = re.compile("downloads/PatentAssignmentText/"+year+"/.+\.zip")
    else:
        pattern = re.compile("downloads/PatentAssignmentText/1980-2014/.+\.zip")
    htmlsource = urllib.urlopen("http://patents.reedtech.com/assignment.php")
    htmlstring = htmlsource.read()
    urls = pattern.findall(htmlstring)
    # if is_hist = true return everything for given year else return latest file
    output_urls =[]
    for u in urls:
        output_urls.append('http://patents.reedtech.com/'+u.split('">')[0])
        #print 'http://patents.reedtech.com/'+u.split('">')[0]
    if is_hist:
        return output_urls
    else:
        return [output_urls[0]]


#
#   Patent Maint Fees URLS
#




def getPatentMaintFeeUrlsToDownload():
    print 'fetching Maintence Fees urls'
    # only 2 files updated weekly
    # first one is text file, is updated from time to time

    pattern = re.compile("downloads/PatentMaintFeeEvents/1981-present/MaintFeeEventsDesc_.*txt")

    htmlsource = urllib.urlopen("http://patents.reedtech.com/maintfee.php")
    htmlstring = htmlsource.read()
    tmpurl = pattern.findall(htmlstring)
    assert len(tmpurl) == 1
    url1 = 'http://patents.reedtech.com/'+tmpurl[0].split('">')[0]

    # if is_hist = true return everything for given year else return latest file
    url2 = 'http://patents.reedtech.com/downloads/PatentMaintFeeEvents/1981-present/MaintFeeEvents.zip'

    return [url1, url2]



#  This is how we can queue file download threads
#
def _download(urllocation,location):
    filename = urllocation.split('/')[-1]
    fullpath = os.path.join(location,filename)
    print urllocation, fullpath
    urllib.urlretrieve(urllocation,fullpath)
def download(a_b):
    "converts F([1,2]) --> F(1,2)"
    return _download(*a_b)

#
# cURL instead of shitty python download libraries that fail in weird ways
#
# Make sure to use -L to process redirects!!
#
def _download2(urllocation,location):
    filename = urllocation.split('/')[-1]
    fullpath = os.path.join(location,filename)
    print urllocation, fullpath
    p = subprocess.Popen(["curl", "-o", fullpath,"-L", urllocation,"--retry","999"], stdout=subprocess.PIPE)
    p.communicate()
def download2(a_b):
    "converts F([1,2]) --> F(1,2)"
    return _download2(*a_b)


def downloadUrls( urls):
    print 'downloading urls..............'
    pool = Pool(processes=config.download_thread_pool_number)
    target_dir = FSS.addBaseDir(config.subdirs['download_dir'])
    pool.map(download2, itertools.izip(urls, itertools.repeat(target_dir)))