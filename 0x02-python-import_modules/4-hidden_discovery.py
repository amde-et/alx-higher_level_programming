#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    temp = dir(hidden_4)
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if (temp[i][j] == '_' and temp[i][j+1] == '_'):
                break
            else:
                print(temp[i])
                break
