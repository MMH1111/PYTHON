class Solution(object):
   def rotateString(self, A, B):
      if not A and not B:
         return True
      if len(A) != len(B):
         return False
      A = A*2
      i = 0
      j=0
      #print(A,B)
      while i < len(A):
         if len(A)-i+1<len(B):
            return False
         while i<len(A) and j < len(B) and A[i] == B[j]:
            #print("Here!",i,j)
            i+=1
            j+=1
         if j == len(B):
            return True
         if j:
            i-=1
         j=0
         i+=1
ob1 = Solution()
print(ob1.rotateString("abcde", "cdeab"))