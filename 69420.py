import sys, builtins, re, string, random
program = open(str(sys.argv[1]), 'rb').read().decode("utf-8")

def rand_string():
    return ''.join(random.choices(string.ascii_lowercase, k=10))

def sub_lists(l, largest=None, smallest=None):
    if largest is None:
        largest = len(l)
    if smallest is None:
        smallest = 0
    lists = []
    if smallest <= 0:
        lists.append([])
        smallest = 1
    l = list(l)
    for i in range(0, largest + 1):
        for j in range(0, i + 1 - smallest):
            lists.append(list(l[j: i]))
    return lists

def subsequences(l, largest=None, smallest=None): 
    def subsequences_helper(ind,ans,l):
        final_ans = []
        if len(ans) > largest:
            return None
        if ind == len(l):
            return [ans]
        else:
            seq = subsequences_helper(ind+1,ans + [l[ind]],l)
            if seq is not None:
                final_ans.extend(seq)
            final_ans.extend(subsequences_helper(ind+1,ans,l))
            return final_ans
    if largest is None:
        largest = len(l)
    if smallest is None:
        smallest = 0
    l = list(l)
    return list(filter(lambda x: len(x) >= smallest, subsequences_helper(0, [], l)))

def absolute(n):
    if isinstance(n, int):
        return abs(n)
    if hasattr(n, '__len__'):
        return len(n)
    raise Exception("Moduli is not defined for this entity: " + n)

def factorial(n):
    res = 1
    if isinstance(n, int):
        while n > 1:
            res *= n
            n -= 1
    else:
        try:
            for x in n:
                res *= x
        except:
            raise Exception("Factorial is not defined for this entity: " + n)
        
    return res

def derrange(n):
    return round(factorial(n) / 2.718281828459045)

program = re.sub(r'[a-zA-Z]+', '', program)
for h in re.findall(r'~\d+!?', program):
    program = program.replace(h, "chr(" + h[1:] + ")", 1)
program = program.replace("~£", " in subsequences( ")
program = program.replace("~$", " in sub_lists( ")
program = program.replace(" £ ", " in ")
program = program.replace("~|", "absolute(")
program = program.replace("~!!", "factorial(")
program = program.replace("~!", "derrange(")
program = program.replace("|~", ")")
program = program.replace("~.", ")")
program = program.replace(":|:", "for")
program = program.replace("&&", "and")
program = program.replace("||", "or")
program = program.replace("=>", "if")
program = program.replace("¬", "not ")

def getoffset(val):
    if "-" in val:
        return " - len([''])"
    return " + len([''])"

for h in re.findall(r'{ *-? *\d+!? *\.\.\. *-? *\d+!? *}', program):
    (first, last) = h.split("...")
    first = first[1:].strip()
    last = last[:-1].strip()
    program = program.replace(h, "set(range(" + first + ", " + last + getoffset(last) + "))")

for h in re.findall(r'\[ *-? *\d+!? *\.\.\. *-? *\d+!? *\]', program):
    (first, last) = h.split("...")
    first = first[1:].strip()
    last = last[:-1].strip()
    program = program.replace(h, "list(range(" + first + ", " + last + getoffset(last) + "))")

for h in re.findall(r'{ *-? *\d+!? *, *-? *\d+!? *\.\.\. *-? *\d+!? *}', program):
    (prefix, last) = h.split("...")
    prefix = prefix[1:].strip()
    (first, diff) = prefix.split(',')
    last = last[:-1].strip()
    
    program = program.replace(h, "set(range(" + first + ", " + last + getoffset(last) + ", (" + diff + ") - (" + first + ")))")

for h in re.findall(r'\[ *-? *\d+!? *, *-? *\d+!? *\.\.\. *-? *\d+!? *\]', program):
    (prefix, last) = h.split("...")
    prefix = prefix[1:].strip()
    (first, diff) = prefix.split(',')
    last = last[:-1].strip()
    program = program.replace(h, "list(range(" + first + ", " + last + getoffset(last) + ", " + diff + " - " + first + "))")

if program.strip().split('\n')[0].strip() == "69420":
    try:
        standard_library = open("standard_library.69420", "rb").read().decode("utf-8")
        program = standard_library + program
    except:
        raise Exception("69420 standard library failed to load")

nums = sorted([int(i) for i in set(re.findall(r'\d+', program))])
nums.reverse()
prefix = ""
num_map = {}
for n in nums:
    name = rand_string()
    num_map[n] = name
    program = program.replace(str(n), name)
    prefix += name + " = " + str(n) + "\n"

exec(prefix)
expressions = re.findall(r'\[\<(.*?)\>\]', program)
for e in expressions:
    if len(e.split(' = ', 1)) > 1:
        (before, after) = e.split(' = ', 1)
        before = before.strip() + '!'
        evaluated = eval(after)
        if isinstance(evaluated, object) and hasattr(evaluated, "__name__"):
            program = program.replace(before, str(evaluated.__name__))
        else:
            program = program.replace(before, str(evaluated))
    exec(e)
    try:
        new = eval(e)
        if isinstance(new, int):
            if new not in num_map.keys():
                name = rand_string()
                num_map[new] = name
            program = program.replace("[<"+e+">]", num_map[new], 1)
        elif isinstance(new, str) or isinstance(new, list):
            program = program.replace("[<"+e+">]", new, 1)
        else:
            program = program.replace("[<"+e+">]", "", 1)
    except:
        program = program.replace("[<"+e+">]", "", 1)

exec(program.strip())
