# 배열 요소에 접근

- 배열 인덱싱은 배열 요소에 접근하는 것과 동일합니다.
- 인덱스 번호를 참조하여 배열 요소에 접근할 수 있습니다.
- 넘파이 배열의 인덱스는 0으로 시작합니다.
- 첫 번째 요소의 인덱스는 0이고 두 번째 요소는 인덱스 1입니다.

```python
# Example
# Get the first element from the following array:
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])

# Example
# Get the second element from the following array
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[1])

# Example
# Get third and fourth elements from the following array and add them.
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[2])
```

# 2차원 배열에 접근하기

- 2차원 배열의 요소에 접근하려면 요소의 차원과 인덱스를 나타내는 쉼표로 구분된 정수를 사용할 수 있습니다.
- 행과 열이 있는 테이블과 같은 2차원 배열을 생각해 보십시오.
- 여기서 행은 차원을 나타내고 인덱스는 열을 나타냅니다.

```python
# Example
# Access the element on the first now, second column:
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('2nd element on 1st row: ', arr[0, 1])
# Example
# Access the element on the 2nd row, 5th column:
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('5th element on 2nd row: ', arr[1, 4])
```

# 3차월 배열에 접근하기

3차원 배열의 요소에 접근하려면 요소의 차워노가 인덱스를 나타내는 쉼표로 구분된 정수를 사용할 수 있습니다.

```python
# Example
# Access the third element of the second array of the first array
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6], [[7, 8, 9], [10, 11, 12]]]])
print(arr[0, 1, 2])
```

# Negative Indexing

음수 인덱싱을 사용하면 끝에서 배열에 접근할 수 있습니다.

``` python
# Example
# Print the last element from the 2nd dim:
import numpy as np
arr = np.array([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
print("Last element from 2nd dim: ", arr[1, -1])
```

# REFERENCE
https://www.w3schools.com/python/numpy/numpy_array_indexing.asp