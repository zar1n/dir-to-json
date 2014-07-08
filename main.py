# -*- coding: utf-8 -*-
__author__ = "Kosovets Sergey @ Zar1n"

import os
import json
import hashlib


class Dirtojson:

    excludeFile = "exclude.txt"

    def walkdir(self, path):
        dirJson = []
        filesJson = []
        dirJson.append({'app_v': 1, 'dbv_v': 1, 'files': filesJson})

        fileEx = self.exclude()

        for dirRoot, dirDir, dirFile in os.walk(path):
            for file in dirFile:
                filePath = "%s/%s" % (dirRoot, file)
                fileHash = hashlib.md5(filePath).hexdigest()

                if file not in fileEx:
                    if dirDir:
                        filesJson.append({'name': file, 'directory': dirDir[0], 'hash': fileHash})
                    else:
                        filesJson.append({'name': file, 'hash': fileHash})

        print json.dumps(dirJson, indent=2, ensure_ascii=False)

    def exclude(self):
        exList = []
        exDesc = open(self.excludeFile, 'rb')
        for exLine in exDesc:
            exList.append(exLine.rstrip('\n'))
        return exList

main = Dirtojson()
main.walkdir("J:\@Movie")