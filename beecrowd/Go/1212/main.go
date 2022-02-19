package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var a, b int
	for {
		fmt.Scanf("%d %d", &a, &b)

		if a == 0 && b == 0 {
			return
		}

		digitsOfA := strings.Split(strconv.Itoa(a), "")
		digitsOfB := strings.Split(strconv.Itoa(b), "")

		carryCount := 0
		carry := 0

		for i := 2; i >= 0; i-- {
			digitOfA, _ := strconv.Atoi(digitsOfA[i])
			digitOfB, _ := strconv.Atoi(digitsOfB[i])
			if sum := digitOfA + digitOfB + carry; sum > 9 {
				carryCount++
				carry = 1
			}

			carry = 0
		}

		if carryCount == 0 {
			fmt.Print("No carry ")
		} else {
			fmt.Printf("%d carry ", carryCount)
		}

		if carryCount < 2 {
			fmt.Println("operation")
		} else {
			fmt.Println("operations")
		}
	}
}
