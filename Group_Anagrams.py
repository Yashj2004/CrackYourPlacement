class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict=defaultdict(list)
        for word in strs:
            key=''.join(sorted(word))
            ana_dict[key].append(word)
        return list(ana_dict.values())
