def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    d = defaultdict(list)     
    for i in strs:
        d[''.join(sorted(i))] = []
    for i in strs:
        if ''.join(sorted(i)) in d:
            d[''.join(sorted(i))].append(i)
    
    return [i for i in d.values()]