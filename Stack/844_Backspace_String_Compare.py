class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack = []
        tStack = []

        for ch in s:
            if ch == "#" and not sStack:
                continue
            if ch == "#":
                sStack.pop()
            else:
                sStack.append(ch)

        for ch in t:
            if ch == "#" and not tStack:
                continue
            if ch == "#":
                tStack.pop()
            else:
                tStack.append(ch)
        return sStack == tStack
