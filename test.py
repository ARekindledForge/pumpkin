from userClass import UserProfile

# checkExpect -> Boolean
# check -> function call
# expectedResult -> expected output of function call
def checkExpect(check, expectedResult):
    print(check == expectedResult)
    return check == expectedResult

user1Blank = UserProfile()
user2Blank = UserProfile()

checkExpect(user1Blank, user2Blank)
checkExpect(user1Blank.__hash__, user2Blank.__hash__)