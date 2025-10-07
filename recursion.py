def decodeString( s: str) -> str:
        # I think I would keep the numbers in one stack and the string in another
        # if it's a character and the prev element is '[' this we append it elese we
        # just extend the last element
        # but there are free strings that don's start with an opening brache

        numbers = [1]
        chars = [""]
        i = 0
        while i in range(len(s)):
            num = ''
            while s[i].isnumeric():
                num += s[i]
                i += 1
            if num:
                numbers.append(int(num))
            
            string = ''
            j = i
            while i < len(s) and s[i].isalpha():
                string += s[i]
                i += 1
                
            if string:
                if j - 1 >= 0 and s[j - 1] == '[':
                    chars.append(string)    
                else:
                    chars[-1] += string

            if i < len(s) and s[i] == "]":
                num = numbers.pop()
                string = chars.pop()
                print(num,string)
                chars[-1] += string * num
                i += 1

            if i < len(s) and s[i] == "[":
                chars.append("")
                i += 1

        return chars[0]


decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")