package main

import (
	"fmt"
	"sort"
)

func main() {
	for {
		var n, m int

		fmt.Scanf("%d %d", &n, &m)
		fmt.Printf("%d %d\n", n, m)
		if n == 0 && m == 0 {
			break
		}

		nums := make([]int, n)
		for i := 0; i < n; i++ {
			fmt.Scanf("%d", &nums[i])
		}

		mod := ModFunc(m)
		sort.Slice(nums, func(i, j int) bool {
			a, b := nums[i], nums[j]

			if mod(a) == mod(b) {
				aEven := a%2 == 0
				bEven := b%2 == 0

				switch {
				case !aEven && bEven:
					return true
				case aEven && !bEven:
					return false
				case aEven && bEven:
					if a < b {
						return true
					}
					return false
				case !aEven && !bEven:
					if a > b {
						return true
					}
					return false
				}
			}

			return mod(a) < mod(b)
		})

		for i := range nums {
			fmt.Println(nums[i])
		}
	}
}

func ModFunc(n int) func(int) int {
	return func(x int) int {
		return x % n
	}
}
