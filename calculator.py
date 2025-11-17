#Calculator-1
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     if b==0:
#         raise ZeroDivisionError("Can't divided by zero")
#     return a/b
# def main():
#     print("Simple Calculator Type 'q' to quit.")
#     ops = {'+':add, '-':sub, '*':mul, '/':div}
#     while True:
#         op = input("Enter the op (+,-,*,/ or q to quit): ")
#         if op == 'q':    
#             print("Calculator stopped.")
#             break

#         s=int(input("Enter the a:"))
#         ss=int(input("Enter the b:"))
#         if op not in ops:
#             print("Supported format")
#             continue
#         print(ops[op](s,ss))
# main()

#Calculator-2
def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b):
    if b==0: raise ZeroDivisionError("Can't divide by zero")
    return a/b
def main():
    print("Simple Calculator.Type 'q' to quit")
    ops = {'+':add, '-':sub, '*':mul, '/':div}
    while True:
        s=input("Enter expression:").strip()
        if s.lower()=='q':
            break
        try:
            
            parts=s.split()
            if len(parts)!=3:
                print("Format:<num> <op> <num>")
                continue
            a=float(parts[0])
            op=parts[1]
            b=float(parts[2])
            if op not in ops:
                print("Supported ops:+ - * /")
                continue
            print("=",ops[op](a,b))
        except Exception as e:
            print("Error:",e)
        
if __name__=="__main__":
    main()