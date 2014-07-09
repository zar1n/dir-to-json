# -*- coding: utf-8 -*-
__author__ = "Kosovets Sergey @ Zar1n"

import os
import json
import hashlib


class Dirtojson:

    configExclude       = "exclude.txt"
    configExportJson    = "export.json"

    def walkdir(self, path):
        dirJson = []
        filesJson = []
        dirJson.append({'app_v': 1, 'dbv_v': 1, 'files': filesJson})

        fileEx = self.exclude()

        for dirRoot, dirDir, dirFile in os.walk(path, topdown=True):
            dirDir[:] = [d for d in dirDir if d not in fileEx]
            for file in dirFile:
                filePath = "%s/%s" % (dirRoot, file)
                fileHash = hashlib.md5(filePath).hexdigest()

                if file not in fileEx:
                    if os.path.basename(dirRoot):
                        filesJson.append({'name': file, 'directory': os.path.basename(dirRoot), 'hash': fileHash})
                    else:
                        filesJson.append({'name': file, 'hash': fileHash})

        self.writeToFile(json.dumps(dirJson, indent=2, ensure_ascii=False))

    def exclude(self):
        exList = []
        exDesc = open(self.configExclude, 'rb')
        for exLine in exDesc:
            exList.append(exLine.rstrip('\n'))
        return exList

    def writeToFile(self, jsonDumps):
        exportFileDesc = open(self.configExportJson, 'wb')
        exportFileDesc.write(jsonDumps)

main = Dirtojson()
main.walkdir("J:\@Movie\\")