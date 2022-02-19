package main

import (
	"fmt"
)

func main() {
	for {
		var volume float32
		_, err := fmt.Scanf("%f", &volume)
		if err != nil {
			break
		}

		var diametro float32
		_, err = fmt.Scanf("%f", &diametro)
		if err != nil {
			break
		}

		altura := 4 * volume / (3.14 * diametro * diametro)
		area := volume / altura

		fmt.Printf("ALTURA = %.2f\n", altura)
		fmt.Printf("AREA = %.2f\n", area)
	}
}
