#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Try to match subrip files names to corresponding video file."""

# Author: Ginko
# Date: 04/01/2013
# Version: 0.1

import os,  re

SRT = 'srt'
VID = 'vid'
SUB = 'sub'
EXTS = ('avi',  'mkv',  'wmv',  'mpg',  'mov')
PATS = {
    'ee.': r'^(\d\d)\. .+$', 
    'sxee': r'^.+\- \d+x(\d+) \-.+$', 
    'SssEee': r'^.+ S\d+E(\d+) .+$', }

def getNextExt():
    """Iterator that yields re patterns."""
    for pat in PATS.values():
        yield pat

class Name():
    """Parse file names."""
    def __init__(self,  raw_name):
        self.name,  self.ext = raw_name.rsplit('.',  1)
        self.fullname = raw_name
        if self.ext in EXTS: self.filetype = VID
        elif self.ext == SRT: self.filetype = SUB
        else: self.filetype = None
        pats = getNextExt()
        self.num = None
        while self.num is None:
            try: pat = pats.__next__()
            except StopIteration: break
            self.num = self.getNumber(pat)
    def getNumber(self, pat):
        mat = re.match(pat,  self.name)
        if mat:
            return mat.group(1)
        else:
            return  None
    def withAltExt(self, new):
        return '.'.join((self.name,  new))


def main():
    
    files = os.listdir(os.getcwd())
    video = {}
    subs =  {}

    for f in files:
        name = Name(f)
        if name.filetype == VID:
            video[name.num] = name
        elif name.filetype == SUB:
            subs[name.num] = name
        
    for num,  vid in video.items():
        try:
            os.rename(subs[num].fullname,  vid.withAltExt(SRT))
        except KeyError:
            pass

if __name__ == "__main__":
    main()
