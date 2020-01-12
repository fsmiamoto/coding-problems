package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", &n)

	for i := 0; i < n; i++ {
		var positions, keys int
		fmt.Scanf("%d %d", &positions, &keys)

		h := ModFunc(positions)
		m := make(map[int][]int)

		for j := 0; j < keys; j++ {
			var x int
			fmt.Scanf("%d", &x)

			m[h(x)] = append(m[h(x)], x)
		}

		for j := 0; j < positions; j++ {
			fmt.Printf("%d -> ", j)
			PrintPosition(m[j])
		}

		// Não imprime linha em branco para o último caso
		if i == n-1 {
			continue
		}

		fmt.Println()
	}
}

func ModFunc(n int) func(int) int {
	return func(x int) int {
		return x % n
	}
}

func PrintPosition(nums []int) {
	for _, v := range nums {
		fmt.Printf("%d -> ", v)
	}
	fmt.Println("\\")
}
