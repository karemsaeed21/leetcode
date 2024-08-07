class Solution:
    def interpret(self, command: str) -> str:
        letter = ""
        for i in range(len(command)):
            if command[i] == "(" and command[i+1] == ")":
                letter += "o"
            elif command[i] == ")" or command[i] == "(":
                continue
            else:
                letter+= command[i]

        return letter