class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            ordered = self.orderString(s)
            anagrams[ordered] = anagrams.get(ordered, [])
            anagrams[ordered].append(s)

        output = []
        for k in anagrams:
            output.append(anagrams[k])

        return output

    def orderString(self, text: str) -> str:
        return "".join(sorted(text))
        