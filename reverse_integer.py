class Solution:
    def reverse(self, x: int) -> int:
        if x.bit_length() >= 32 or x.bit_length() <= -32: return 0
        else:  
            self.x = str(x)
            if not self.x.startswith('-'):
                reversed = self.x[::-1]
            elif self.x.startswith('-'):
                unsigned_x = self.x[1:]
                reversed = '-' + unsigned_x[::-1]
            if int(reversed).bit_length() >= 32 or int(reversed).bit_length() <= -32: return 0
            else: return int(reversed)
