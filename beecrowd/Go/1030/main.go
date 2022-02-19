package main

import "fmt"

// Removes element from slice
func remove(s []int, i int) []int {
	s[i] = s[len(s)-1]
	// We do not need to put s[i] at the end, as it will be discarded anyway
	return s[:len(s)-1]
}

func main() {
	var numOfTests int
	fmt.Scanf("%d", &numOfTests)

	for i := 0; i < numOfTests; i++ {
		var numOfMen, step int
		fmt.Scanf("%d %d", &numOfMen, &step)

		men := make([]int, numOfMen, numOfMen)

		for index, _ := range men {
			men[index] = index + 1
		}

		nextDeadMan := 0

		for deadMen := 0; deadMen < numOfMen-1; deadMen++ {
			nextDeadMan += step

			if nextDeadMan > len(men) {
				nextDeadMan -= len(men)
			}

			men = remove(men, nextDeadMan)
		}

		fmt.Println(men)

	}
}
