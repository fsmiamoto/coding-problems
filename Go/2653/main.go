package main

import "fmt"

func main() {

	joias := make(map[string]int)
	for {
		var j string
		_, err := fmt.Scanf("%s", &j)

		if err != nil {
			break
		}

		joias[j]++
	}

	fmt.Println(len(joias))

}
