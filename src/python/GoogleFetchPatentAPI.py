import sys
import os

import etl.XmlChunkReader as xml
import PatentZephyr.src.python.CFPAPIconfig as config
import DownloadsFetcher as DF
import FileSystemSetup as FSS
import PatentZephyr.src.python.etl.parser.mfCurrentParser as mfParser

#  ************************************************************************
#  ************************************************************************
#  File Readers --> Parsers
#
#
#

def get_xml_files(year):
    walk = FSS.addBaseDir(config.subdirs['unziped_dir'])
    inputfiles = []
    for filename in os.listdir(walk):
        if '.xml' in filename:
            inputfiles.append(os.path.join(walk,filename))
    return inputfiles

def parseXML(year, type):
    data = set()
    if year > 2000:
        paths = get_xml_files(year)
        for path in paths:
            s = xml.chunk(path)
            data = set(list(data) + list(s))
    o = list(data)
    o.sort()
    fs = '%s/%s_%s.txt' % (FSS.getSchemaPath(), type, year)
    output = open(fs, 'w')
    for item in o:
        #print item
        output.write(item+'\n')
    output.close()


def parseMFees():
    # get the one txt file + one zip file
    walk = FSS.addBaseDir(config.subdirs['unziped_dir'])
    inputfiles = []
    for filename in os.listdir(walk):
        if '.txt' in filename:
            inputfiles.append(os.path.join(walk,filename))
    walk = FSS.addBaseDir(config.subdirs['download_dir'])
    for filename in os.listdir(walk):
        if '.txt' in filename:
            inputfiles.append(os.path.join(walk,filename))
    assert len(inputfiles) == 2

    for path in inputfiles:
        mfParser.parse(path)




def run_etl(year, is_hist, type):

    assert type in ['patent-grant',
                    'patent-application',
                    'trademark-application',
                    'trademark-assignment',
                    'trademark-tab',
                    'patent-assignment',
                    'patent-maint-fee'
                    ]
    FSS.setupFileSystem()

    # based on argv, download relevant patents or applications
    #urls = getUrlsToDownload(year, is_hist, is_grant, is_google_source?)
    urls = []
    #
    #  Patent grants
    #
    if type == 'patent-grant':
        urls = DF.getPatentUrlsToDownload(year, is_hist, True)
    #
    #  patent applications
    #
    if type == 'patent-application':
        urls = DF.getPatentApplicationUrlsToDownload(year, is_hist, True)
    #
    #  trademark applications
    #
    elif type == 'trademark-application':
        urls = DF.getTradeMarkApplicationUrlsToDownload(year, is_hist)
    #
    #  trademark assignments
    #
    elif type == 'trademark-assignment':
        urls = DF.getTradeMarkAssignmentUrlsToDownload(year, is_hist)
    #
    #  trademark Trial and Appeal board
    #
    elif type == 'trademark-tab':
        urls = DF.getTradeMarkTabUrlsToDownload(year, is_hist)
    #
    #  Patent assignments
    #
    elif type == 'patent-assignment':
        urls = DF.getPatentAssignmentUrlsToDownload(year, is_hist)
    #
    #  Patent maintence fees
    #
    elif type == 'patent-maint-fee':
        urls = DF.getPatentMaintFeeUrlsToDownload()
        print 'found %s urls' % str(len(urls))
        print urls
        DF.downloadUrls(urls)
        FSS.unzipData()
        parseMFees()
        sys.exit(0)

    print 'found %s urls' % str(len(urls))

    DF.downloadUrls(urls)
    FSS.unzipData()
    parseXML(year, type)




if __name__ == '__main__':


    #year, is_hist, type = 2015, False, 'patent-grant'
    year, is_hist, type = 2014, True, 'patent-application'
    #year, is_hist, type = 2015, True, 'trademark-application'
    #year, is_hist, type = 2013, True, 'trademark-assignment'
    #year, is_hist, type = 2012, True, 'trademark-tab'
    #year, is_hist, type = 2015, True, 'patent-assignment'
    #year, is_hist, type = 2014, True, 'patent-assignment'
    #year, is_hist, type = 2013, True, 'patent-assignment'

    #year, is_hist, type = 2015, False, 'patent-maint-fee'

    run_etl(year, is_hist, type)

    #for y in range(2005,2016):
    #    print y
    #    run_etl(y, is_hist, type)