package main

import "fmt"

func main() {
	var numOfTests int
	var message string
	fmt.Scanf("%d", &numOfTests)

	for i := 0; i < numOfTests; i++ {
		fmt.Scanf("%s", &message)
		var deslocatedBytes []byte
		for j := len(message) - 1; j >= 0; j-- {
			deslocatedBytes = append(deslocatedBytes, message[j]+3)
		}
		fmt.Println(string(deslocatedBytes))
	}
}
