class Solution(object):
                
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #initialize string format
        s = "(" + s + ")"
        s = s.replace(" ","")
        print(s)
        
        #until no more ")" left
        while s.find(")") != -1:
            ind_2 = s.find(")")
            ind_1 = s[0:ind_2].rfind("(")         
            
            #simplify specific part and exchange part of string for ans
            s = s[0:ind_1] + Solution.simplifyPart(s[ind_1:ind_2+1]) + s[ind_2 + 1:]
            s = s.replace("--","+")
            print(s)
        
        return int(s)
    
    @staticmethod
    def simplifyPart(s):
        exp = []
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
        index = 0
        while index < len(s):
            temp = ""
            offset = 0

            #if found a number
            if s[index] in nums:
                
                #retrieving number value
                while s[index + offset] in nums:
                    temp += s[index + offset]
                    offset += 1
                if s[index - 1] == "-":
                    temp = "-" + temp
                    
                #adding number to expression string
                exp.append(int(temp))

                #skip forward when searching for next number
                index = index + offset
            index += 1
            
        return str(sum(exp))
