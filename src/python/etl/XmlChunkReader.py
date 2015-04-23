import codecs
from collections import Iterator

from PatentZephyr.src.python.etl.parser.schema import paCurrent as pgCurrent
from PatentZephyr.src.python.etl.parser.schema import paCurrent as pg2014
from PatentZephyr.src.python.etl.parser.schema import paCurrent as pa2006
import PatentZephyr.src.python.etl.parser.aCurrentParser as aCurrent
import PatentZephyr.src.python.etl.parser.paCurrentParser as paCurrent
import PatentZephyr.src.python.etl.parser.taCurrentParser as taCurrent
import PatentZephyr.src.python.etl.parser.tasCurrentParser as tasCurrent
import PatentZephyr.src.python.etl.parser.ttaCurrentParser as ttaCurrent

import XMLSchemaBuilder as XMLSB




#
# This class reads a given xml bolb as a file and greps the actual individual xml documents out of it and decides which
# parser to use
#
#


class reader(Iterator):

    def __init__(self,path):
        self.f = codecs.open(path,'rb','utf-8')
        self.tmp_data = None
        self.counter = 0
        self.versions = set()
        self.current_version = None

    def check_current_version(self, data):
        if '<!DOCTYPE' in data:
            if 'us-patent-grant' in data or 'PATDOC' in data:
                #
                #  Patent Grants
                #
                if 'us-patent-grant-v45-2014-04-03.dtd' in data:
                    self.current_version = 'pgCurrent'
                    self.versions.add(self.current_version)
                elif 'us-patent-grant-v44-2013-05-16.dtd' in data or 'us-patent-grant-v43-2012-12-04.dtd' in data:
                    self.current_version = 'pg2014'
                    self.versions.add(self.current_version)
                elif 'us-patent-grant-v42-2006-08-23.dtd' in data or 'us-patent-grant-v41-2005-08-25.dtd' in data or 'us-patent-grant-v40-2004-12-02.dtd' in data:
                    self.current_version = 'pg2006'
                    self.versions.add(self.current_version)
                elif 'ST32-US-Grant-025xml.dtd' in data:
                    self.current_version = 'pg2004'
                    self.versions.add(self.current_version)


                else:
                    print data
                    self.versions.add(self.current_version)
            elif 'us-patent-application' in data or 'patent-application-publication' in data:
                #
                #  Patent Applications
                #
                if 'us-patent-application-v44-2014-04-03.dtd' in data:
                    self.current_version = 'aCurrent'
                    self.versions.add(self.current_version)
                elif 'us-patent-application-v43-2012-12-04.dtd' in data:
                    self.current_version = 'aCurrent'
                    self.versions.add(self.current_version)



                elif 'us-patent-application-v42-2006-08-23.dtd' in data:
                    self.current_version = 'a2006'
                    self.versions.add(self.current_version)
                elif 'us-patent-application-v41-2005-08-25.dtd' in data:
                    self.current_version = 'a2005'
                    self.versions.add(self.current_version)
                elif 'us-patent-application-v40-2004-12-02.dtd' in data:
                    self.current_version = 'a2004'
                    self.versions.add(self.current_version)
                elif 'pap-v16-2002-01-01.dtd' in data:
                    self.current_version = 'a2002'
                    self.versions.add(self.current_version)
                elif 'pap-v15-2001-01-31.dtd' in data:
                    self.current_version = 'a2001'
                    self.versions.add(self.current_version)

                else:
                    print data
                    self.versions.add(self.current_version)

                #
                #  Application sequence list
                #
            elif 'us-sequence-listing.dtd' in data:
                self.current_version = 'seqCurrent'
                self.versions.add(self.current_version)
            else:
                print data
                self.versions.add(self.current_version)
        #
        #  Trademark Applications
        #

        elif 'DTD TRADEMARK-APPLICATIONS-DAILY V2.0 2005-04-01' in data:
            self.current_version = 'taCurrent'
            self.versions.add(self.current_version)
        elif 'DTD TRADEMARK_ASSIGNMENTS V1.0 2013-09-05' in data:
            self.current_version = 'tasCurrent'
            self.versions.add(self.current_version)
        elif 'DTD TTAB PROCEEDINGS V1.0 2004-02-13' in data:
            self.current_version = 'ttaCurrent'
            self.versions.add(self.current_version)

        #
        #  Patent Assignments
        #
        elif 'us-patent-assignments' in data:
            self.current_version = 'paCurrent'
            self.versions.add(self.current_version)





    def check_line(self,data):
        flags = '<?xml'
        if flags in str(data).lower():
            return True
        else:
            return False

    def next(self):
        if self.counter % 1000 ==0:
            print self.counter
        #if self.counter == 3:
        #    print self.counter
        #    raise StopIteration
        data = self.tmp_data
        #initial line
        if data == None:
            data = self.f.next().encode('utf-8')
            self.check_current_version(data)
        for line in self.f:
            line = line.encode('utf-8')
            self.check_current_version(line)

            if self.check_line(line):

                self.tmp_data = line
                self.counter += 1

                assert self.current_version != None

                return [data, self.current_version]
            else:
                data += line
        # set to zero again
        self.tmp_data = None
        self.counter += 1
        assert self.current_version != None

        return [data, self.current_version]

    def close(self):
        self.f.close()
        print self.versions


#
#   Chunk takes in a path and then attempts to parse both the templates + data from a filepath
#
#       It works like a state machine, it greps for a for an xml <! DOCTYPE templates DTD file, and
#       then routes the xml to the relevant parser
#
#


def chunk(path):
    print "parsing",path
    r = reader(path)
    tmp = []

    aCurrentParser = None

    pg2004parser = None
    pg2014parser = None
    pg2006parser = None

    taCurrentParser = None
    tasCurrentParser = None
    ttaCurrentParser = None
    tParser = None

    paCurrentParser = None
    xmlSchemaBuilder = XMLSB.tree_builder()

    for item in r:
        #patents can have many patents in a file so we have to read them 1 at a time
        cv = item[1]
        data = item[0]

        if cv == 'pgCurrent':
            xmlSchemaBuilder.parser(data, cv)
        elif cv == 'pg2014':
            xmlSchemaBuilder.parser(data, cv)
            #if pg2014parser != None:
            #    pg2014parser.parse(data)
            #else:
            #    pg2014parser = pg2014.parser(path, cv)
        elif cv == 'pg2006':
            xmlSchemaBuilder.parser(data, cv)
            #if pg2006parser != None:
            #    pg2006parser.parse(data)
            #    xmlSchemaBuilder.parser(data, cv)
            #else:
            #    pg2006parser = pg2006.parser(path, cv)
        elif cv == 'pg2004':
            xmlSchemaBuilder.parser(data, cv)
        elif cv == 'aCurrent':
            if aCurrentParser != None:
                aCurrentParser.parse(data)
            else:
                aCurrentParser = aCurrent.parser(path, cv)
                aCurrentParser.parse(data)
            xmlSchemaBuilder.parser(data, cv)
        elif cv == 'a2012':
            xmlSchemaBuilder.parser(data, cv)
        elif cv == 'a2006':
            xmlSchemaBuilder.parser(data, cv)
        elif cv == 'a2005':
            xmlSchemaBuilder.parser(data, cv)
        elif cv == 'a2004':
            xmlSchemaBuilder.parser(data, cv)
        elif cv == 'a2002':
            xmlSchemaBuilder.parser(data, cv)
        elif cv == 'a2001':
            xmlSchemaBuilder.parser(data, cv)




        # Trade marks are one big xml file so we just care about its DTD

        elif cv == 'taCurrent':
            if taCurrentParser == None:
                print 'DTD for TrademarkApplications found'
                tParser = taCurrent.parser(path, cv)

        elif cv == 'tasCurrent':
            if tasCurrentParser == None:
                print 'DTD for TrademarkAssignments found'
                tParser =tasCurrent.parser(path, cv)

        elif cv == 'ttaCurrent':
            if ttaCurrentParser == None:
                print 'DTD for TrademarkTrialsAppeals found'
                tParser = ttaCurrent.parser(path, cv)

        elif cv == 'paCurrent':
            if paCurrentParser == None:
                print 'DTD for PatentAssignments found'
                paCurrentParser = paCurrent.parser(path, cv)


    if tParser != None:
        # parsing trademarks!
        print 'Parsing!'
        tParser.parse(path)


    if paCurrentParser != None:
        # patent assignments!
        print 'Parsing!'
        paCurrentParser.parse(path)


    # print templates builder
    #xmlSchemaBuilder.finish()
    data = xmlSchemaBuilder.getset()

        #tmp.append(item)
    r.close()
    return data

#chunk('/Users/matthewharrison/PatentDisplayBuild/unzip_tmp/ipa150129.xml')