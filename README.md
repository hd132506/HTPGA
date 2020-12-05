# HTPGA
GA for solving HTP

## Concept

![concept](.\img\concept.png)

- NxN개 육각형의 마름모꼴 모양
- 1차원 배열 세 개 형태의 표현형
  - 꼭짓점에 맞닿은 육각형의 개수에 따라 Level(Contact Level)로 분할
  - 육각형과 맵핑되어 Fitness 계산/지역성을 반영한 변이 연산 등에 활용



## Class description

### VerticeSpace

- 지수귀문도 꼭짓점의 실제 값들을 세 개의 일차원 배열로 담고 있는 클래스
- 값 get/set, swap 등의 연산 및 부가정보를 위한 속성들
- Verification(값들이 순열의 성질을 유지하는지)

### Hexagon

- VerticeSpace의 각각 값들의 위치와 맵핑되는 6개의 튜플을 담고 있는 육각형 자료구조
  - 각 튜플은 (level, position)으로 VerticeSpace의 element에 접근하는 포인터 역할을 함

- Tortoise 클래스에 의해 이차원 배열 형태로 사용됨
- 위치 정보 튜플의 get/set(set은 초기 tortoise 구성에만 사용) 및 이차원배열에서의 좌표 정보

### Tortoise

- length를 파라미터로 받아 length*length 크기의 VerticesSpace와 대응되는 Hexagon 클래스들을 구성하는 클래스
- 지역적으로 인접한 값들, 육각형 값의 합/평균/분산 등 유전 연산을 돕는 operation 제공

![class](.\img\class.png)



