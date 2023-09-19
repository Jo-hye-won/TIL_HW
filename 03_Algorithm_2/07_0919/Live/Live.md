# 백트래킹
> 여러 가지 선택지(옵션)들이 존재하는 상황에서 한가지를 선택한다.

- 선택이 이루어지면 새로운 선택지들의 집합이 생성된다.
- 이런 선택을 반복 하면서 최종 상태에 도달한다. 
 - 올바른 선택을 계속하면 목표 상태(goal state)에 도달한다.

## 당첨 리프 노드 찾기
- 루트에서 갈 수 있는 노드를 선택한다.
- 꽝 노드까지 도달하면 최근의 선택으로 되돌아와서 다시 시작한다.
- 더 이상의 선택지가 없다면 이전의 선택지로 돌아가서 다른 선택을 한다. 
- 루트까지 돌아갔을 경우 더 이상 선택지가 없다면 찾는 답이 없다. 

## 백트래킹과 깊이 우선 탐색과의 차이
- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 다라가지 않음으로써 시도의 횟수를 줄임(Prunning 가지치기)
- 깊이 우선 탐색이 모든 경로를 추적하는데 비해  백트래킹은 불필요한 경로를 조기에 차단.
- 깊이 우선탐색을 가하기에는 경우의 수가 너무나 많음. 즉, N!가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색을 가하면 당연히 처리 불가능한 문제
- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간을 요하므로 처리 불가능

- 루트 노드에서 리프노드까지의 경로는 해답후보가 되는데, 깊이우선 검색을 하여 그 해답후보 중에서 해답을 찾을 수 있다. 
- 그러나 이 방법을 사용하면 해답이 될 가능성이 전혀 없는 노드의 후손 노드들도 모두 검색해야 하므로 비효율적이다.

### 백트래킹 기법
- 어떤 노드의 유망성을 점검한 후에 유망하지 않다고 결정되면 그 노드의 부모로 되돌가 다음 자식 노드로 감.
- 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다. 
- 가지치기(prunning) : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다. 

> 백트래킹을 이용한 알고리즘은 다음과 같은 절차로 진행된다.(p.46)
1. 상태 공간 트리의 깊이 우선 검색을 실시한다.
2. 각 노드가 유망한지를 점검한다.
3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다.

### 일반 백트래킹 알고리즘
```markdown
def checknode(node v)
    IF promising(v)
        if there is a solution at v
            write the solution
        ELSE
            FOR each child u of v
                checknode(u)
```

### 상태공간트리를 구축하여 문제를 해결
```text
bool bactrack(선택 집합, 선택한 수, 모든 선택수)
{
    if (선택한 수 == 모든 선택수) //  더 이상 탐색할 노드가 없다.
    {
       찾는 솔루션인지 체크;
       return 결과;
    }
    현재 선택한 상태집합에 포함되지 않는 후보 선택들(노드) 생성
    
    모든 후보 선택들에 대해
    {
       선택 집합에 하나의 후보선택을 추가
       선택한 수 = 선택한 수 + 1
       결과 = backtrack 호출(선택집합, 선택한 수, 모든 선택수)
       
       if (결과 == 성공)
            return 성공; // 성공한 경우 상위로 전달
    }
    return 실패;
}
```

### {1, 2, 3}의 powerset을 구하는 백트래킹 알고리즘
```text
def backtrack(a[], k, input):
    c[MAXCANDIDATES]
    ncands

    IF k == input : process_solution(a[], k):
    ELSE
        k ++
        make_candidates(a[], k, input, c[], ncands)
        FOR i in 0 -> ncnads - 1
            a[k] <- c[i]
            backtrack(a, k, input)
            
main()
    a[MAX]  // powerset을 저장할 배열
    backtrack(a[], 0, 3)   // 3개의 원소를 가지는 powerset
    
    
def make_candidates(a[], k, n, c[], ncands)
    c[0] <- TRUE
    c[1] <- FALSE
    ncands <- 2
    
def process_solution(a[], k)
    FOR i in 1 -> k
        IF a[i] = TRUE : print(i)
```

### 백트래킹을 이용하여 순열 구하기
- 접근방법은 앞의 부분집합 구하는 방법과 유사함
```text
backtrack(a[], k, input)
    c[MAXCANDIDATES]
    ncands

    IF k == input : process_solution(a[], k):
    ELSE
        k ++
        make_candidates(a[], k, input, c[], ncands)
        FOR i in 0 -> ncnads - 1
            a[k] <- c[i]
            backtrack(a, k, input)
main()
    a[MAX]  // 순열을 저장할 배열
    backtrack(a[], 0, 3)   // 3개의 원소를 가지는 순열

def make_candidates(a[], k, n, c[], ncands)
    in_perm[NMAX] <- FALSE
    
    FOR i in 1 -> k - 1
        in_perm[a[i]] <- TRUE
       
    ncands <- 0
    FOR i in 1 -> n
        IF in_perm[i] == FALSE
            c[ncands] <- i
            ncands ++    
        
def process_solution(a[], k)
    FOR i in 1 -> k : print(a[i])
```

# 트리
- 사이클이 없는 연결 그래프
- 연결그래프 : 모든 꼭지점이 서로 갈 수 있다!

- 이진 트리 : 모든 자녀 노드가 둘 이하인 트리    
    0. 이진 트리 종류
       - 완전 이진 트리
         - 마지막 레벨을 제외한 모든 레벨은 꽉 차있어야 한다.
         - 마지막 레벨 노드는 왼쪽부터 채워져야 한다. 
       - 포화 이진 트리
         - 모든 레벨이 꽉 차있는 것
       - 나머지 이진 트리 
        
    1. 순회방법
        1. 전위(부모 -> 좌 -> 우)
        2. 중위(좌 -> 부모 -> 우)
        3. 후위(좌 -> 우 -> 부모)
      
    2. 트리 저장 방법
 