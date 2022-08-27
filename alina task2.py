#LAB ASSIGNMENT 4--------------------------------------------------------------
#Name: Alina Hasan
#ID: 20101301
#Section: 3
#------------------------------------------------------------------------------

#[2]---------------------------------------------------------------------------
with open('task2_input.txt','r') as f:
    with open('task2_ouput.txt','w') as f1:
        R,S = [],[]
        NM = next(f).split()
        M = int(NM[1])
        for line in f.readlines():
            s,f = line.split()
            R.append((int(s),int(f)))
        R.sort(key = lambda x:x[1])
        for s in R:
            S.append(s[0])

        maxN = 0
        x = R.pop(0)
        S.pop(0)
        A = []
        for n in range(M):
            A.append(x)
            f = x[1]
            maxN += 1
            for r in R:
                if r[0]>=f:
                    A.append(r)
                    f = r[1]
                    maxN += 1
                    R.remove(r)
                    S.remove(r[0])
            if R != []:
                x = R.pop(0)

        f1.write(f'{maxN}\n')
        print(maxN)

#[END]-------------------------------------------------------------------------