class ReverseString:
    def reverse(self, s):
        return s[::-1]


rev = ReverseString()
print(rev.reverse("hello"))  