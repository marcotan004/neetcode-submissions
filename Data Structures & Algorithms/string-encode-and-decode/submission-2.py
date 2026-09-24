class Solution:

    def encode(self, strs: List[str]) -> str:
        returned = ""

        for s in strs:
            returned += "/z/" + s
        
        return returned
    def decode(self, s: str) -> List[str]:
        return s.split("/z/")[1:]
