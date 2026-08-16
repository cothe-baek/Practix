# [level 3] 섬 연결하기 - 42861 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42861) 

---
### 피드백 (Kruskal & Union-Find)

이 문제는 최소 비용으로 모든 노드를 사이클 없이 연결하는 **최소 신장 트리(MST)** 문제로, **크루스칼(Kruskal) 알고리즘**을 사용해야 함 (N이 작아서 그냥 set 순회도 가능은 함)

컨셉은 비용 오름차순 정렬 후, cycle이 생기지 않게 간선을 연결하면서, 연결된 것들을 하나의 tree로 묶으면서 (제일 작은 번호가 root가 됨) N-1개의 간선을 만들기

#### 1. 오류: Root끼리 합치기
기존 `merge` 함수(Union 연산)에서 노드 간 병합 시, 그룹의 최상위 루트가 아닌 **입력된 노드 자체의 부모**를 변경하여 그룹이 온전히 합쳐지지 않고 끊어지는 오류 발생
*   **해결:** 두 노드의 그룹을 합칠 때는 반드시 각 노드의 **최상위 대장(Root)을 찾아서 대장끼리 연결**해야함

```python
# [수정 전] - leaf의 부모를 변경하는 오류
if a < b:
    root[y] = a 

# [수정 후] - 정석 방식: 진짜 root node끼리 연결
if a < b:
    root[b] = a 
```

#### 2. 핵심 최적화: 경로 압축 (Path Compression)
find_root 함수가 단순 재귀로 root를 찾기만 하면 안됨

처음 호출됐을 때 **탐색을 거친 모든 노드의 부모를 진짜 root로 갱신**해줘야 다음 호출부터 O(1)로 root 찾기 가능

```python
def find_root(x):
    if root[x] != x:
        root[x] = find_root(root[x]) # 마법의 1줄: 경로 압축
    return root[x]
```
*   **효과:** 깊었던 트리 구조가 완전히 납작해짐. 한 번 탐색한 이후에는 중간 단계를 모두 건너뛰고 탐색 시간을 $O(1)$에 가깝게 단축 가능
---


### 성능 요약

메모리: 11.5 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 탐욕법（Greedy）

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 08월 16일 21:09:42

### 문제 설명

<p>n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.</p>

<p>다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.</p>

<p><strong>제한사항</strong></p>

<ul>
<li>섬의 개수 n은 1 이상 100 이하입니다.</li>
<li>costs의 길이는 <code>((n-1) * n) / 2</code>이하입니다.</li>
<li>임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.</li>
<li>같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.</li>
<li>모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.</li>
<li>연결할 수 없는 섬은 주어지지 않습니다.</li>
</ul>

<p><strong>입출력 예</strong></p>
<table class="table">
        <thead><tr>
<th>n</th>
<th>costs</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>4</td>
<td>[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]</td>
<td>4</td>
</tr>
</tbody>
      </table>
<p><strong>입출력 예 설명</strong></p>

<p>costs를 그림으로 표현하면 다음과 같으며, 이때 초록색 경로로 연결하는 것이 가장 적은 비용으로 모두를 통행할 수 있도록 만드는 방법입니다.</p>

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/13e2952057/f2746a8c-527c-4451-9a73-42129911fe17.png" title="" alt="image.png"></p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
