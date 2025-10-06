def greet(name = None):
    if name == None:
        return "Hello my friend"
    
    elif type(name) == list:
        names = [str(n).strip() for n in name if str(n).strip()]
        if not names:
            return "Hello my friend"
        if len(names) == 1:
            return f"Hello, {names[0]}"
        if len(names) == 2:
            return f"Hello, {names[0]} and {names[1]}"
        return f"Hello, {', '.join(names[:-1])}, and {names[-1]}"
  
    elif name.isupper() == True:
        return f"HELLO, {name}"
    
    else:
        return f"Hello, {name}"

if __name__ == "__main__":
    print(greet(["Bob","Jim","Linda","Peter"]))