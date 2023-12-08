class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for p in paths:
            # 1. split the string by ' '
            path = p.split()
            # the first string is the directory path
            # the rest of them are just file names with content
            directoryPath, rest = path[0], path[1:]
            # for each file names with content
            for f in rest:
                # we retrieve the file name and the file content
                fileName, fileContent = f.split('(')[0], f.split('(')[1][:-1]
                # then group {directoryPath}/{fileName} by file content
                m[fileContent].append("{}/{}".format(directoryPath, fileName))
        # return the file list only when the size is greater than 1, meaning they are duplicate files
        return [m[k] for k in m.keys() if len(m[k]) > 1]
        