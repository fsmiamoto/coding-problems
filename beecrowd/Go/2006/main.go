package main

import "fmt"

func main() {
	var escolhaCerta int
	fmt.Scanf("%d\n", &escolhaCerta)

	respostasCertas := 0
	for i := 0; i < 5; i++ {
		var escolha int
		fmt.Scanf("%d", &escolha)

		if escolha == escolhaCerta {
			respostasCertas++
		}
	}

	fmt.Println(respostasCertas)
}
