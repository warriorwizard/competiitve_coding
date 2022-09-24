class Solution:
	def concatenatedBinary(self, n: int) -> int:
		string="0b"
		b=10**9+7
		for i in range(1,n+1):
			temp=bin(i)
			temp=temp[2:]
			string+=str(temp)
			# print()
			# print("--------")
			# print(string)
		# return string
		return int(string,2)%b
	
a=Solution()
print(a.concatenatedBinary(12))