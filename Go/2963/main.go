package main

import "fmt"

func main() {
	var NumDeParticipantes int

	fmt.Scanf("%d", &NumDeParticipantes)

	var votosDoCarlos int
	fmt.Scanf("%d", &votosDoCarlos)

	carlosVenceu := true

	for i := 0; i < NumDeParticipantes-1; i++ {
		var votosDeOutro int
		fmt.Scanf("%d", &votosDeOutro)

		if votosDeOutro > votosDoCarlos {
			carlosVenceu = false
		}
	}

	if carlosVenceu {
		fmt.Println("S")
	} else {
		fmt.Println("N")
	}
}
