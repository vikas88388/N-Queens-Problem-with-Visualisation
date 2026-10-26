"""N-Queens bitmask solver. Counts solutions for N up to 20 (runtime grows rapidly)."""
import argparse, time

def count_solutions(n: int) -> int:
    mask=(1<<n)-1
    def solve(cols,diag1,diag2):
        if cols==mask: return 1
        total=0
        available=mask & ~(cols|diag1|diag2)
        while available:
            bit=available & -available
            available-=bit
            total += solve(cols|bit, ((diag1|bit)<<1)&mask, (diag2|bit)>>1)
        return total
    return solve(0,0,0)

def first_solution(n: int):
    cols=set(); d1=set(); d2=set(); q=[]
    def bt(r):
        if r==n:return True
        for c in range(n):
            if c not in cols and r-c not in d1 and r+c not in d2:
                q.append(c);cols.add(c);d1.add(r-c);d2.add(r+c)
                if bt(r+1):return True
                q.pop();cols.remove(c);d1.remove(r-c);d2.remove(r+c)
        return False
    return q if bt(0) else None

def show(q):
    if q is None: print('No solution'); return
    n=len(q)
    for c in q: print(' '.join('Q' if j==c else '.' for j in range(n)))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('n',type=int,nargs='?',default=8);p.add_argument('--all',action='store_true');a=p.parse_args()
    if not 1<=a.n<=20: raise SystemExit('N must be between 1 and 20')
    t=time.perf_counter()
    if a.all: print(f'N={a.n}, solutions={count_solutions(a.n)}')
    else: show(first_solution(a.n))
    print(f'Time: {time.perf_counter()-t:.6f}s')
