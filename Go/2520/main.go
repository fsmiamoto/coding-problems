package main

import (
	"fmt"
	"math"
)

const (
	Ash     = 1
	Pikachu = 2
)

func main() {
	for {
		var n, m int

		_, err := fmt.Scanf("%d %d", &n, &m)
		if err != nil {
			break
		}

		matrix := new2DMatrix(n, m)

		var ashPosition, pikachuPosition [2]int

		for i := 0; i < n; i++ {
			for j := 0; j < m; j++ {
				var x int
				fmt.Scanf("%d", &x)

				if x == Ash {
					ashPosition = [2]int{i, j}
				}

				if x == Pikachu {
					pikachuPosition = [2]int{i, j}
				}
				matrix[i][j] = x
			}
		}

		time := math.Abs(float64(ashPosition[0]-pikachuPosition[0])) +
			math.Abs(float64(ashPosition[1]-pikachuPosition[1]))

		fmt.Println(time)
	}
}

func new2DMatrix(n, m int) [][]int {
	matrix := make([][]int, n)
	for i := range matrix {
		matrix[i] = make([]int, m)
	}
	return matrix
}
