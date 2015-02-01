import os
import subprocess

import PatentZephyr.src.python.CFPAPIconfig as config





#  ************************************************************************
#  ************************************************************************
#
#  setup the filesystem main function setupFileSystem()
#
#



def forceUnzipDir(from_dir, to_dir):
    cmd = 'unzip %s/\*.zip -d %s' % (addBaseDir(from_dir), addBaseDir(to_dir))
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()


def unzipData():
    print 'unzipping files..............'
    forceUnzipDir(config.subdirs['download_dir'], config.subdirs['unziped_dir'])

def addBaseDir(dir):
    return os.path.join(os.path.expanduser(config.target_dir), dir)

def forceCreateRefreshDirectory(directory_path):
    if os.path.isdir(directory_path):
        fileList = os.listdir(directory_path)
        for fileName in fileList:
            os.remove(os.path.join(directory_path,fileName))
    else:
        os.mkdir(directory_path)

def CreateRefreshDirectory(directory_path):
    if os.path.isdir(directory_path):
        pass
    else:
        os.mkdir(directory_path)

def getSchemaPath():
    return os.path.join(os.path.expanduser(config.target_dir), config.schema_dir)

def setupFileSystem():
    print 'checking filesystem..............'
    path = os.path.expanduser(config.target_dir)
    for item in config.subdirs.values():
        forceCreateRefreshDirectory(os.path.join(path,item))
    CreateRefreshDirectory(os.path.join(path,config.schema_dir))