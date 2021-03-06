

def printMAT(mat):
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            print(mat[row][col],end=" ")
        print()
    


def targetSumSubset(arr,target_sum):
    ROW=len(arr)+1
    COL=target_sum+1
    dp=[[False for _ in range(COL)] for _ in range(ROW)]
    # print(dp)
    
    for row in range(ROW):
        for col in range(COL):
            if(row==0 and col==0):
                dp[row][col]=True
            elif(row==0):
                dp[row][col]=False
            elif(col==0):
                dp[row][col]=True
            else:
                if(dp[row-1][col]==True):
                    dp[row][col]=True
                else:
                    val=arr[row-1]
                    if(col>=val):
                        if(dp[row-1][col-val]==True):
                            dp[row][col]=True
    return dp[-1][-1]

        
def targetSumSubsetMemo(nums,target,index,memo={}):
    if target in memo:return memo[target]
    if target==0:return True
    if target<0:return False
    if index>=len(nums):return False
    print(target,index)
    if targetSumSubsetMemo(nums,target-nums[index],index+1):
        memo[target-nums[index]]=True
        return True
    if targetSumSubsetMemo(nums,target,index+1):
        memo[target]=True
        return True
    memo[target-nums[index]]=False
    memo[target]=False
    return False

arr=[4,2,7,1,3]

print(targetSumSubset(arr,10))
print(targetSumSubsetMemo(arr,10,0))
    
    
    