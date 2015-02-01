import os

import PatentZephyr.src.python.CFPAPIconfig as config
import ParserUtils as util


def parse_desc(path):


    outputFilePath = os.path.join(getOutputFilePath(), 'patent_maintenence_fee_desc.txt')
    inputfile = open(path, 'r')
    outputfile = open(outputFilePath,'w')


    headerstr = config.file_delimiter.join(['id', 'desc']) + config.file_newline
    outputfile.write(headerstr.decode('utf-8'))
    for line in inputfile:
        l = line.encode('utf-8')
        split = l.find(' ')
        id = util.clean(l[0 : split])
        desc = util.clean(l[split:])
        outstr = config.file_delimiter.join([id, desc]) + config.file_newline

        outputfile.write(outstr)

    inputfile.close()
    outputfile.close()


def parse_mnt(path):
    outputFilePath = os.path.join(getOutputFilePath(), 'patent_maintenence_fee_events.txt')
    inputfile = open(path, 'r')
    outputfile = open(outputFilePath,'w')

    headers = ['patent_no','application_no','small_entity','application_filing_date','grant_issue_date','mnt_fee_event_date','mnt_fee_event_code_id']

    headerstr = config.file_delimiter.join(headers) + config.file_newline
    outputfile.write(headerstr.decode('utf-8'))
    for line in inputfile:
        l = line.encode('utf-8').strip()

        patent_no = l[0:7]
        application_no = l[8:16]
        small_entity = l[17:18]
        application_filing_date = l[19:27]
        grant_issue_date = l[28:36]
        mnt_fee_event_date = l[37:45]
        mnt_fee_event_code_id = l[46:52]

        data = [patent_no,application_no,small_entity,application_filing_date,grant_issue_date,mnt_fee_event_date,mnt_fee_event_code_id]

        outstr = config.file_delimiter.join(data) + config.file_newline

        outputfile.write(outstr)

    inputfile.close()
    outputfile.close()

def getOutputFilePath():
    return os.path.join(os.path.expanduser(config.target_dir), config.subdirs['parsed_dir'])


def isDesc(path):
    if 'Desc' in path.split('/')[-1]:
        return True
    return False


def parse(path):

    if isDesc(path):

        parse_desc(path)
    else:
        parse_mnt(path)






if __name__ == '__main__':
    path = '/Users/matthewharrison/PatentDisplayBuild/download_tmp/MaintFeeEventsDesc_20140210.txt'
    path2 ='/Users/matthewharrison/PatentDisplayBuild/unzip_tmp/MaintFeeEvents_20150112.txt'
    parse(path)
    parse(path2)



