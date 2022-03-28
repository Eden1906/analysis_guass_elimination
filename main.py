#EDEN LEVY 208376095
import random as rnd
def mulMtrx(mat1, mat2):  # elementary mtrx in first place!
    matrixMUL = [[0,0,0], [0,0,0],[0,0,0]]
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            for k in range(len(mat1)):
                matrixMUL[i][j] += mat1[i][k] * mat2[k][j]
    return matrixMUL



def elementaryMtrx(pivot, i, j, element, size):
    matrix = []
    for k in range(size):
        matrix.append([])
        for l in range(size):
            matrix[k].append(0 if k != l else 1)
    matrix[i][j] = -(element / pivot)
    return matrix


def fixMatrix(a, size, col):
    if a[col][col] == 0:
        for j in range(col, size):
            if a[j][col] != 0:
                a[col], a[j] = a[j], a[col]
                return a
    return a


def createIdentityMatrix(size):
    mtrx = []
    for i in range(size):
        mtrx.append([])
        for j in range(size):
            if i == j:
                mtrx[i].append(1)
            else:
                mtrx[i].append(0)
    return mtrx


def prettyPrint(a, b):
    for i in range(len(a)):
        print(a[i], end='\t\t')
        print(b[i])
    print('##################################################')


def guass(a, size):
    l = createIdentityMatrix(size)
    u = a
    for col in range(size):
        u = fixMatrix(u, size, col)
        for row in range(size - 1, col, -1):
            if u[row][col] != 0:
                if (u[col][col] == 0):
                    print()
                elementary_matrix = elementaryMtrx(u[col][col], row, col, u[row][col], size)
                l[row][col] = u[row][col] / u[col][col]
                prettyPrint(elementary_matrix, u)
                u = mulMtrx(elementary_matrix, u)
    print('########     U #######')
    for row in u:
        print(row)
    print('########     l #######')
    for row in l:
        print(row)
    print()
    print()
    print("     L*U                 A")
    prettyPrint(mulMtrx(l, u), a)
    print("from here, invers lxu and mul it with vector b")
    b = [[7],[2],[5]]
    muluANDl=multiplierNonEqualMtrx(l,u)
    inverslANDu=invertMtrx(muluANDl,createIdentityMatrix(3))
    print(inverslANDu)
    print("the solution is :")
    print(multiplierNonEqualMtrx(inverslANDu,b))

def invertMtrx(a,I):
    for fd in range(len(a)):
        fdscalar = 1.0 / a[fd][fd]
        for j in range(len(a)):
            a[fd][j] *= fdscalar
            I[fd][j] *= fdscalar
        for i in list(range(len(a)))[0:fd] + list(range(len(a)))[fd+1:]:
            crscalar = a[i][fd]
            for j in range(len(a)):
                a[i][j] = a[i][j] = a[i][j] - crscalar * a[fd][j]
                I[i][j] = I[i][j] - crscalar * I[fd][j]
    return I


def multiplierNonEqualMtrx(a,b):
    r= []
    m = []
    for i in range(len(a)):
        for j in range(len(b[0])):
            sums = 0
            for k in range(len(b)):
                sums = sums +(a[i][k]*b[k][j])
            r.append(sums)
        m.append(r)
        r=[]
    return m



edenID = [2,0,8,3,7,6,0,9,5]
print("the question that been drawn : ")
print((rnd.choice(edenID)%30)+19)




A = [[1,2,-2],[1,1,1],[2,2,1]]
guass(A,3)










