class Solution:
    def interpret(self, command: str) -> str:
        
        string = ''
        for i in range(len(command)):
            if command[i] == "G":
                string += "G"
            elif command[i:i+2] == "()":
                string +="o"
                i +=2
                
            elif command[i:i+4] == '(al)':
                string +="al"
                i = i+4
        return string