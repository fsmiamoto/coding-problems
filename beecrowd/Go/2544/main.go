package main

import (
	"fmt"
)

func main() {
	for {
		var n int64

		_, err := fmt.Scanf("%d", &n)
		if err != nil {
			break
		}

		var i int
		for i = 0; n > 1; i++ {
			n = n >> 1
		}

		fmt.Println(i)
	}
}
